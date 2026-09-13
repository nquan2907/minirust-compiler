"""
Code Generator for MiniRust - compiles the checked AST into JVM bytecode (Jasmin).
"""

from typing import Any
from utils.AST import *
from utils.Visitor import BaseVisitor
from codegen.Emitter import (
    Emitter, is_int_type, is_float_type, is_bool_type,
    is_string_type, is_void_type, is_struct_type,
)
from codegen.Frame import Frame
from codegen.Io import IO_SYMBOL_LIST
from codegen.Utils import Symbol, FunctionType, StructType as CGStructType, CName, SubBody, Access, Index


class StringArrayType:
    """Marker type for JVM main(String[] args)."""
    pass


def uw(x):
    """
    Unwrap a name field that may be either a plain str (e.g. hand-written
    test ASTs) or an Id node (e.g. real ASTGenerator output). Id.name is
    always a plain str, so a single unwrap is sufficient.
    """
    return x if type(x) is str else x.name


def lookup(name, sym_list):
    """Look up a variable by name, most-recently-declared (innermost) first."""
    for sym in reversed(sym_list):
        if sym.name == name:
            return sym
    return None


def struct_name_of(t):
    """Get the plain string struct name from either an AST.StructType or a
    codegen.Utils.StructType instance."""
    raw = t.struct_name if hasattr(t, 'struct_name') else t.name
    return uw(raw)


# Jasmin's assembler reserves these bare words for its own directives
# (".field", ".inner", ".method", etc.) and chokes if a user identifier
# (e.g. a MiniRust struct field named "inner") happens to match one, even
# when it appears as a plain field/method name rather than a directive.
# We mangle any such colliding name before emitting it into .j text.
_JASMIN_RESERVED = {
    "class", "field", "method", "end", "limit", "var", "source", "super",
    "interface", "implements", "throws", "catch", "line", "deprecated",
    "signature", "inner", "outer", "enclosing", "annotation", "bytecode",
    "stack", "locals", "public", "private", "protected", "static", "final",
    "synchronized", "volatile", "transient", "native", "abstract",
    "strict", "bridge", "varargs", "enum", "synthetic", "default", "const",
}


def safe_name(name):
    """Mangle a user-chosen identifier if it collides with a Jasmin keyword."""
    return name + "_f" if name.lower() in _JASMIN_RESERVED else name


class CodeGenerator(BaseVisitor):
    def __init__(self):
        self.emit = None
        self.class_name = "MiniRustProgram"
        self.functions = {}          # name -> Symbol(FunctionType)
        self.structs = {}            # name -> list[Symbol] (fields, in decl order)
        self.struct_emitters = {}    # name -> Emitter

    # ------------------------------------------------------------------
    # Program / top-level declarations
    # ------------------------------------------------------------------

    def visitProgram(self, node: Program, o: Any = None):
        struct_decls = [d for d in node.decls if type(d) is StructDecl]
        func_decls = [d for d in node.decls if type(d) is FuncDecl]

        list(map(lambda sym: self.functions.update({sym.name: sym}), IO_SYMBOL_LIST))
        list(map(lambda d: self.functions.update({
            uw(d.name): Symbol(
                uw(d.name),
                FunctionType([p.var_type for p in d.params], d.return_type),
                CName(self.class_name),
            )
        }), func_decls))

        list(map(self._register_struct, struct_decls))
        list(map(self._gen_struct_class, struct_decls))

        self.emit = Emitter(f"{self.class_name}.j")
        self.emit.print_out(self.emit.emit_prolog(self.class_name))
        list(map(lambda d: self.visit(d, None), func_decls))
        self.emit.emit_epilog()
        return o

    def _register_struct(self, node: StructDecl):
        fields = [Symbol(uw(f.name), f.var_type, Index(i)) for i, f in enumerate(node.fields)]
        self.structs[uw(node.name)] = fields

    def _gen_struct_class(self, node: StructDecl):
        struct_name = uw(node.name)
        emitter = Emitter(f"{struct_name}.j")
        emitter.print_out(emitter.emit_prolog(struct_name))
        for field in node.fields:
            emitter.print_out(emitter.emit_attribute(safe_name(uw(field.name)), field.var_type))
        emitter.print_out(emitter.emit_default_constructor())
        emitter.emit_epilog()
        self.struct_emitters[struct_name] = emitter

    def visitStructDecl(self, node: StructDecl, o: Any = None):
        # struct classes are generated up-front in visitProgram
        return o

    def visitFuncDecl(self, node: FuncDecl, o: Any = None):
        func_name = uw(node.name)
        is_main = func_name == "main"
        frame = Frame(func_name, node.return_type)
        frame.enter_scope(True)

        param_types = [p.var_type for p in node.params]
        mtype = FunctionType([StringArrayType()], VoidType()) if is_main \
            else FunctionType(param_types, node.return_type)

        self.emit.print_out(self.emit.emit_method(func_name, mtype, True))

        start_label = frame.get_start_label()
        end_label = frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label, frame))

        sym_list = []
        if is_main:
            args_idx = frame.get_new_index()
            self.emit.print_out(self.emit.emit_var(args_idx, safe_name("args"), StringArrayType(), start_label, end_label))
        else:
            for p in node.params:
                idx = frame.get_new_index()
                sym_list.append(Symbol(uw(p.name), p.var_type, Index(idx)))
                self.emit.print_out(self.emit.emit_var(idx, safe_name(uw(p.name)), p.var_type, start_label, end_label))

        body_o = SubBody(frame, sym_list)
        list(map(lambda s: self.visit(s, body_o), node.body.stmts))

        if type(node.return_type) is VoidType:
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))
        else:
            # Unreachable if the source is well-typed (every path in a
            # non-void function must already return), but without it,
            # dead-code labels from if/else chains where every branch
            # returns can end up pointing at the literal end of the
            # method's bytecode, which the JVM verifier rejects as an
            # "Illegal target of jump or branch".
            if is_float_type(node.return_type):
                self.emit.print_out(self.emit.emit_push_fconst("0.0", frame))
            elif is_int_type(node.return_type) or is_bool_type(node.return_type):
                self.emit.print_out(self.emit.emit_push_iconst(0, frame))
            else:
                self.emit.print_out(self.emit.emit_push_null(frame))
            self.emit.print_out(self.emit.emit_return(node.return_type, frame))

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        frame.exit_scope()
        self.emit.print_out(self.emit.emit_end_method(frame))
        return o

    # ------------------------------------------------------------------
    # Type inference for expressions (needed for coercion / instruction choice)
    # ------------------------------------------------------------------

    def get_expr_type(self, node, sym_list):
        t = type(node)
        if t is IntLiteral:
            return IntType()
        if t is FloatLiteral:
            return FloatType()
        if t is BoolLiteral:
            return BoolType()
        if t is StringLiteral:
            return StringType()
        if t is Id:
            sym = lookup(uw(node.name), sym_list)
            return sym.type if sym else None
        if t is BinaryOp:
            if node.op in ('&&', '||', '==', '!=', '<', '<=', '>', '>='):
                return BoolType()
            lt = self.get_expr_type(node.left, sym_list)
            rt = self.get_expr_type(node.right, sym_list)
            if is_float_type(lt) or is_float_type(rt):
                return FloatType()
            return IntType()
        if t is UnaryOp:
            if node.op == '!':
                return BoolType()
            return self.get_expr_type(node.body, sym_list)
        if t is CallExpr:
            sym = self.functions.get(uw(node.name))
            return sym.type.return_type if sym else None
        if t is ArrayCell:
            arr_t = self.get_expr_type(node.arr, sym_list)
            return arr_t.element_type if arr_t else None
        if t is FieldAccess:
            obj_t = self.get_expr_type(node.obj, sym_list)
            if obj_t is None:
                return None
            fields = self.structs.get(struct_name_of(obj_t), [])
            f = next((f for f in fields if f.name == uw(node.field)), None)
            return f.type if f else None
        if t is StructInit:
            return CGStructType(uw(node.name))
        if t is ArrayLiteral:
            elem_t = self.get_expr_type(node.elements[0], sym_list) if node.elements else IntType()
            return ArrayType(elem_t, len(node.elements))
        if t is Assign:
            return self.get_expr_type(node.lhs, sym_list)
        return None

    # ------------------------------------------------------------------
    # Statements
    # ------------------------------------------------------------------

    def visitBlock(self, node: Block, o: SubBody):
        frame = o.frame
        frame.enter_scope(False)
        self.emit.print_out(self.emit.emit_label(frame.get_start_label(), frame))
        block_o = SubBody(frame, list(o.sym))
        list(map(lambda s: self.visit(s, block_o), node.stmts))
        self.emit.print_out(self.emit.emit_label(frame.get_end_label(), frame))
        frame.exit_scope()
        return o

    def visitVarDecl(self, node: VarDecl, o: SubBody):
        frame = o.frame
        name = uw(node.name)
        idx = frame.get_new_index()

        if node.init is not None:
            init_code, init_type = self.visit(node.init, Access(frame, o.sym))
            var_type = node.var_type if node.var_type is not None else init_type
            code = init_code
            if is_float_type(var_type) and is_int_type(init_type):
                code += self.emit.emit_i2f(frame)
            code += self.emit.emit_write_var(name, var_type, idx, frame)
        else:
            var_type = node.var_type
            code = ""

        self.emit.print_out(code)
        start_label = frame.get_start_label()
        end_label = frame.get_end_label()
        self.emit.print_out(self.emit.emit_var(idx, safe_name(name), var_type, start_label, end_label))

        o.sym.append(Symbol(name, var_type, Index(idx)))
        return o

    def visitIf(self, node: If, o: SubBody):
        frame = o.frame
        cond_code, _ = self.visit(node.cond, Access(frame, o.sym))
        label_false = frame.get_new_label()
        label_end = frame.get_new_label()

        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(label_false, frame))
        self.visit(node.then_stmt, o)
        if node.else_stmt is not None:
            self.emit.print_out(self.emit.emit_goto(label_end, frame))
            self.emit.print_out(self.emit.emit_label(label_false, frame))
            self.visit(node.else_stmt, o)
            self.emit.print_out(self.emit.emit_label(label_end, frame))
        else:
            self.emit.print_out(self.emit.emit_label(label_false, frame))
        return o

    def visitWhile(self, node: While, o: SubBody):
        frame = o.frame
        frame.enter_loop()
        label_cont = frame.get_continue_label()
        label_brk = frame.get_break_label()

        self.emit.print_out(self.emit.emit_label(label_cont, frame))
        cond_code, _ = self.visit(node.cond, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(label_brk, frame))
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_goto(label_cont, frame))
        self.emit.print_out(self.emit.emit_label(label_brk, frame))

        frame.exit_loop()
        return o

    def visitFor(self, node: For, o: SubBody):
        # for var in start..end { body }  (end exclusive, end evaluated ONCE)
        frame = o.frame
        frame.enter_scope(False)
        self.emit.print_out(self.emit.emit_label(frame.get_start_label(), frame))
        var_name = uw(node.var_name)
        idx = frame.get_new_index()

        start_code, _ = self.visit(node.start, Access(frame, o.sym))
        self.emit.print_out(start_code)
        self.emit.print_out(self.emit.emit_write_var(var_name, IntType(), idx, frame))
        start_label = frame.get_start_label()
        end_label = frame.get_end_label()
        self.emit.print_out(self.emit.emit_var(idx, safe_name(var_name), IntType(), start_label, end_label))

        # Evaluate the range's end bound exactly once (before the loop body
        # runs at all) and stash it in a hidden local var, so a side-effecting
        # end expression (e.g. a function call) isn't re-run every iteration.
        end_idx = frame.get_new_index()
        end_code, _ = self.visit(node.end, Access(frame, o.sym))
        self.emit.print_out(end_code)
        self.emit.print_out(self.emit.emit_write_var("$for_end", IntType(), end_idx, frame))

        loop_o = SubBody(frame, o.sym + [Symbol(var_name, IntType(), Index(idx))])

        frame.enter_loop()
        label_cont = frame.get_continue_label()   # continue jumps here: right before the increment
        label_brk = frame.get_break_label()
        label_check = frame.get_new_label()        # loop-back point for the condition test

        self.emit.print_out(self.emit.emit_label(label_check, frame))

        cmp_code = self.emit.emit_read_var(var_name, IntType(), idx, frame)
        cmp_code += self.emit.emit_read_var("$for_end", IntType(), end_idx, frame)
        cmp_code += self.emit.emit_re_op('<', IntType(), frame)
        self.emit.print_out(cmp_code)
        self.emit.print_out(self.emit.emit_if_false(label_brk, frame))

        self.visit(node.body, loop_o)

        self.emit.print_out(self.emit.emit_label(label_cont, frame))
        self.emit.print_out(self.emit.emit_iinc(idx, 1, frame))
        self.emit.print_out(self.emit.emit_goto(label_check, frame))
        self.emit.print_out(self.emit.emit_label(label_brk, frame))

        frame.exit_loop()
        self.emit.print_out(self.emit.emit_label(frame.get_end_label(), frame))
        frame.exit_scope()
        return o

    def visitSwitch(self, node: Switch, o: SubBody):
        frame = o.frame
        expr_code, expr_type = self.visit(node.expr, Access(frame, o.sym))

        # Only manage a break label here (append directly to frame's break
        # stack). We deliberately do NOT use frame.enter_loop(), because that
        # also pushes a new continue label, which would incorrectly shadow
        # the continue label of an enclosing for/while loop.
        label_brk = frame.get_new_label()
        frame.brk_label.append(label_brk)

        case_labels = []
        default_label = None
        for case in node.cases:
            lbl = frame.get_new_label()
            case_labels.append(lbl)
            if case.val is None:
                default_label = lbl

        dispatch = expr_code
        for case, lbl in zip(node.cases, case_labels):
            if case.val is None:
                continue
            skip_lbl = frame.get_new_label()
            dispatch += self.emit.emit_dup(frame)
            val_code, _ = self.visit(case.val, Access(frame, o.sym))
            dispatch += val_code
            dispatch += self.emit.emit_re_op('==', expr_type, frame)
            dispatch += self.emit.emit_if_false(skip_lbl, frame)
            # match: discard the leftover duplicated switch value before jumping in
            dispatch += self.emit.emit_pop(frame)
            dispatch += self.emit.emit_goto(lbl, frame)
            dispatch += self.emit.emit_label(skip_lbl, frame)
        # no case matched: discard switch value, go to default (or break out)
        dispatch += self.emit.emit_pop(frame)
        dispatch += self.emit.emit_goto(default_label if default_label is not None else label_brk, frame)
        self.emit.print_out(dispatch)

        for case, lbl in zip(node.cases, case_labels):
            self.emit.print_out(self.emit.emit_label(lbl, frame))
            case_o = SubBody(frame, list(o.sym))
            list(map(lambda s: self.visit(s, case_o), case.body))

        self.emit.print_out(self.emit.emit_label(label_brk, frame))
        frame.brk_label.pop()
        return o

    def visitCase(self, node: Case, o: SubBody):
        list(map(lambda s: self.visit(s, o), node.body))
        return o

    def visitBreak(self, node: Break, o: SubBody):
        self.emit.print_out(self.emit.emit_goto(o.frame.get_break_label(), o.frame))
        return o

    def visitContinue(self, node: Continue, o: SubBody):
        self.emit.print_out(self.emit.emit_goto(o.frame.get_continue_label(), o.frame))
        return o

    def visitReturn(self, node: Return, o: SubBody):
        frame = o.frame
        if node.expr is not None:
            expr_code, expr_type = self.visit(node.expr, Access(frame, o.sym))
            self.emit.print_out(expr_code)
            if is_float_type(frame.return_type) and is_int_type(expr_type):
                self.emit.print_out(self.emit.emit_i2f(frame))
            self.emit.print_out(self.emit.emit_return(frame.return_type, frame))
        else:
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))
        return o

    def visitExprStmt(self, node: ExprStmt, o: SubBody):
        frame = o.frame
        code, typ = self.visit(node.expr, Access(frame, o.sym))
        if typ is not None and not is_void_type(typ):
            code += self.emit.emit_pop(frame)
        self.emit.print_out(code)
        return o

    # ------------------------------------------------------------------
    # Expressions  (each visit*() returns a tuple: (code: str, type))
    # ------------------------------------------------------------------

    def _emit_operands_coerced(self, left_node, right_node, o):
        frame = o.frame
        left_code, left_t = self.visit(left_node, o)
        right_code, right_t = self.visit(right_node, o)
        use_float = is_float_type(left_t) or is_float_type(right_t)

        code = left_code
        if use_float and not is_float_type(left_t):
            code += self.emit.emit_i2f(frame)
        code += right_code
        if use_float and not is_float_type(right_t):
            code += self.emit.emit_i2f(frame)

        common_type = FloatType() if use_float else left_t
        return code, common_type

    def visitBinaryOp(self, node: BinaryOp, o: Access):
        frame = o.frame
        op = node.op
        if op == '&&':
            return self._emit_and(node, o)
        if op == '||':
            return self._emit_or(node, o)

        code, common_type = self._emit_operands_coerced(node.left, node.right, o)
        if op in ('==', '!=', '<', '<=', '>', '>='):
            code += self.emit.emit_re_op(op, common_type, frame)
            return code, BoolType()
        if op == '%':
            code += self.emit.emit_mod(frame)
            return code, IntType()
        if op in ('+', '-'):
            code += self.emit.emit_add_op(op, common_type, frame)
            return code, common_type
        # '*' or '/'
        code += self.emit.emit_mul_op(op, common_type, frame)
        return code, common_type

    def _emit_and(self, node, o):
        frame = o.frame
        label_false = frame.get_new_label()
        label_end = frame.get_new_label()
        left_code, _ = self.visit(node.left, o)
        code = left_code
        code += self.emit.emit_if_false(label_false, frame)
        right_code, _ = self.visit(node.right, o)
        code += right_code
        code += self.emit.emit_goto(label_end, frame)
        code += self.emit.emit_label(label_false, frame)
        code += self.emit.emit_push_iconst(0, frame)
        code += self.emit.emit_label(label_end, frame)
        return code, BoolType()

    def _emit_or(self, node, o):
        frame = o.frame
        label_true = frame.get_new_label()
        label_end = frame.get_new_label()
        left_code, _ = self.visit(node.left, o)
        code = left_code
        code += self.emit.emit_if_true(label_true, frame)
        right_code, _ = self.visit(node.right, o)
        code += right_code
        code += self.emit.emit_goto(label_end, frame)
        code += self.emit.emit_label(label_true, frame)
        code += self.emit.emit_push_iconst(1, frame)
        code += self.emit.emit_label(label_end, frame)
        return code, BoolType()

    def visitUnaryOp(self, node: UnaryOp, o: Access):
        frame = o.frame
        code, t = self.visit(node.body, o)
        if node.op == '-':
            code += self.emit.emit_neg_op(t, frame)
            return code, t
        # '!'
        label_false = frame.get_new_label()
        label_end = frame.get_new_label()
        code += self.emit.emit_if_false(label_false, frame)
        code += self.emit.emit_push_iconst(0, frame)
        code += self.emit.emit_goto(label_end, frame)
        code += self.emit.emit_label(label_false, frame)
        code += self.emit.emit_push_iconst(1, frame)
        code += self.emit.emit_label(label_end, frame)
        return code, BoolType()

    def visitCallExpr(self, node: CallExpr, o: Access):
        frame = o.frame
        fn_name = uw(node.name)
        fn_sym = self.functions[fn_name]
        code = ""
        for i, arg in enumerate(node.args):
            arg_code, arg_type = self.visit(arg, o)
            code += arg_code
            param_type = fn_sym.type.param_types[i]
            if is_float_type(param_type) and is_int_type(arg_type):
                code += self.emit.emit_i2f(frame)
        lexeme = f"{fn_sym.value.value}/{fn_name}"
        code += self.emit.emit_invoke_static(lexeme, fn_sym.type, frame)
        return code, fn_sym.type.return_type

    def visitId(self, node: Id, o: Access):
        sym = lookup(uw(node.name), o.sym)
        return self.emit.emit_read_var(uw(node.name), sym.type, sym.value.value, o.frame), sym.type

    def visitArrayCell(self, node: ArrayCell, o: Access):
        frame = o.frame
        arr_code, arr_type = self.visit(node.arr, o)
        idx_code, _ = self.visit(node.idx, o)
        elem_type = arr_type.element_type
        code = arr_code + idx_code + self.emit.emit_aload(elem_type, frame)
        return code, elem_type

    def visitFieldAccess(self, node: FieldAccess, o: Access):
        frame = o.frame
        obj_code, obj_type = self.visit(node.obj, o)
        s_name = struct_name_of(obj_type)
        field_name = uw(node.field)
        field_sym = next(f for f in self.structs[s_name] if f.name == field_name)
        lexeme = f"{s_name}/{safe_name(field_name)}"
        code = obj_code + self.emit.emit_get_field(lexeme, field_sym.type, frame)
        return code, field_sym.type

    def visitStructInit(self, node: StructInit, o: Access):
        frame = o.frame
        s_name = uw(node.name)
        code = self.emit.emit_new_instance(s_name, frame)
        for init in node.initializers:
            f_name = uw(init.name)
            field_sym = next(f for f in self.structs[s_name] if f.name == f_name)
            code += self.emit.emit_dup(frame)
            val_code, val_type = self.visit(init.expr, o)
            code += val_code
            if is_float_type(field_sym.type) and is_int_type(val_type):
                code += self.emit.emit_i2f(frame)
            lexeme = f"{s_name}/{safe_name(f_name)}"
            code += self.emit.emit_put_field(lexeme, field_sym.type, frame)
        return code, CGStructType(s_name)

    def visitFieldInit(self, node: FieldInit, o: Access):
        # handled inline by visitStructInit; provided for completeness of dispatch
        return self.visit(node.expr, o)

    def visitArrayLiteral(self, node: ArrayLiteral, o: Access):
        frame = o.frame
        elem_type = self.get_expr_type(node.elements[0], o.sym) if node.elements else IntType()
        code = self.emit.emit_push_iconst(len(node.elements), frame)
        code += self.emit.emit_new_array(elem_type, frame)
        for i, elem in enumerate(node.elements):
            code += self.emit.emit_dup(frame)
            code += self.emit.emit_push_iconst(i, frame)
            val_code, val_type = self.visit(elem, o)
            code += val_code
            if is_float_type(elem_type) and is_int_type(val_type):
                code += self.emit.emit_i2f(frame)
            code += self.emit.emit_astore(elem_type, frame)
        return code, ArrayType(elem_type, len(node.elements))

    def visitAssign(self, node: Assign, o: Access):
        frame = o.frame
        lhs = node.lhs

        if type(lhs) is Id:
            rhs_code, rhs_type = self.visit(node.rhs, o)
            sym = lookup(uw(lhs.name), o.sym)
            code = rhs_code
            if is_float_type(sym.type) and is_int_type(rhs_type):
                code += self.emit.emit_i2f(frame)
            code += self.emit.emit_dup(frame)
            code += self.emit.emit_write_var(uw(lhs.name), sym.type, sym.value.value, frame)
            return code, sym.type

        if type(lhs) is ArrayCell:
            arr_code, arr_type = self.visit(lhs.arr, o)
            idx_code, _ = self.visit(lhs.idx, o)
            rhs_code, rhs_type = self.visit(node.rhs, o)
            elem_type = arr_type.element_type
            code = arr_code + idx_code + rhs_code
            if is_float_type(elem_type) and is_int_type(rhs_type):
                code += self.emit.emit_i2f(frame)
            code += self.emit.emit_dup_x2(frame)
            code += self.emit.emit_astore(elem_type, frame)
            return code, elem_type

        # FieldAccess
        obj_code, obj_type = self.visit(lhs.obj, o)
        rhs_code, rhs_type = self.visit(node.rhs, o)
        s_name = struct_name_of(obj_type)
        field_name = uw(lhs.field)
        field_sym = next(f for f in self.structs[s_name] if f.name == field_name)
        code = obj_code + rhs_code
        if is_float_type(field_sym.type) and is_int_type(rhs_type):
            code += self.emit.emit_i2f(frame)
        code += self.emit.emit_dup_x1(frame)
        lexeme = f"{s_name}/{safe_name(field_name)}"
        code += self.emit.emit_put_field(lexeme, field_sym.type, frame)
        return code, field_sym.type

    def visitIntLiteral(self, node: IntLiteral, o: Access):
        return self.emit.emit_push_iconst(node.value, o.frame), IntType()

    def visitFloatLiteral(self, node: FloatLiteral, o: Access):
        return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()

    def visitBoolLiteral(self, node: BoolLiteral, o: Access):
        return self.emit.emit_push_iconst(1 if node.value else 0, o.frame), BoolType()

    def visitStringLiteral(self, node: StringLiteral, o: Access):
        return self.emit.emit_push_const(node.value, StringType(), o.frame), StringType()