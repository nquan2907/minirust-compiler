from utils.AST import *
from utils.Visitor import BaseVisitor
from checker.StaticError import *
from typing import Any


BUILTIN_FUNCS = {
    "print_i32":     ([IntType()], VoidType()),
    "println_i32":   ([IntType()], VoidType()),
    "print_f32":     ([FloatType()], VoidType()),
    "println_f32":   ([FloatType()], VoidType()),
    "print_bool":    ([BoolType()], VoidType()),
    "println_bool":  ([BoolType()], VoidType()),
    "print_string":  ([StringType()], VoidType()),
    "println_string":([StringType()], VoidType()),
    "println":       ([], VoidType()),
}


class StaticChecker(BaseVisitor):
    def __init__(self, ast_obj=None):
        self.ast = ast_obj
        self.structs = {}          # name -> StructDecl
        self.funcs = dict(BUILTIN_FUNCS)   # name -> (param_types, return_type)
        # context of the function currently being checked
        self.param_names = set()
        self.return_type = None
        self.loop_depth = 0
        self.switch_depth = 0

    def check(self):
        self.visitProgram(self.ast, None)

    # ---------------------------------------------------------------
    # small shared checks (kept minimal, reused a lot)
    # ---------------------------------------------------------------
    def _check_type_valid(self, t):
        if type(t) is StructType:
            if t.name.name not in self.structs:
                raise UndeclaredStruct(t.name.name)
        elif type(t) is ArrayType:
            self._check_type_valid(t.element_type)

    def _assignable(self, target, source):
        if target is None or source is None:
            return False
        return target == source

    def _coercible(self, target, source):
        # only used for vardecl-with-explicit-type, assignment (`x = ...`),
        # function-call arguments, and struct-init field values.
        if target is None or source is None:
            return False
        if target == source:
            return True
        if type(target) is FloatType and type(source) is IntType:
            return True
        if type(target) is ArrayType and type(source) is ArrayType and target.size == source.size:
            return self._coercible(target.element_type, source.element_type)
        return False

    # ---------------------------------------------------------------
    # Program / declarations
    # ---------------------------------------------------------------
    def visitProgram(self, ast: Program, o: Any) -> Any:
        struct_decls = [d for d in ast.decls if type(d) is StructDecl]
        func_decls = [d for d in ast.decls if type(d) is FuncDecl]

        # register structs
        for s in struct_decls:
            if s.name.name in self.structs:
                raise Redeclared("Struct", s.name.name)
            self.structs[s.name.name] = s

        # field name uniqueness
        for s in struct_decls:
            seen = set()
            for f in s.fields:
                if f.name.name in seen:
                    raise Redeclared("Member", f.name.name)
                seen.add(f.name.name)

        # direct / indirect recursive struct detection: for each struct (in
        # declaration order) check each field (in order) - error is raised
        # at the first field whose type chain leads back to that struct.
        def reaches(t, target_name, visited):
            if type(t) is ArrayType:
                return reaches(t.element_type, target_name, visited)
            if type(t) is not StructType:
                return False
            dep = t.name.name
            if dep == target_name:
                return True
            if dep not in self.structs or dep in visited:
                return False
            visited.add(dep)
            return any(reaches(f.var_type, target_name, visited) for f in self.structs[dep].fields)

        for s in struct_decls:
            for f in s.fields:
                if reaches(f.var_type, s.name.name, set()):
                    raise TypeMismatchInStatement(f)

        # validate field types (struct references must exist)
        for s in struct_decls:
            for f in s.fields:
                self._check_type_valid(f.var_type)

        # register functions
        for fn in func_decls:
            if fn.name.name in self.funcs:
                raise Redeclared("Function", fn.name.name)
            pnames = set()
            for p in fn.params:
                if p.name.name in pnames:
                    raise Redeclared("Parameter", p.name.name)
                pnames.add(p.name.name)
                self._check_type_valid(p.var_type)
            self._check_type_valid(fn.return_type)
            self.funcs[fn.name.name] = ([p.var_type for p in fn.params], fn.return_type)

        main_decls = [f for f in func_decls if f.name.name == "main"]
        if not main_decls:
            raise UndeclaredFunction("main")
        main_fn = main_decls[0]

        for fn in func_decls:
            self.visit(fn, None)

        if len(main_fn.params) != 0 or type(main_fn.return_type) is not VoidType:
            raise TypeMismatchInStatement(main_fn)

        return None

    def visitStructDecl(self, ast: StructDecl, o: Any) -> Any:
        return None  # fully handled in visitProgram

    def visitFuncDecl(self, ast: FuncDecl, o: Any) -> Any:
        self.param_names = {p.name.name for p in ast.params}
        self.return_type = ast.return_type
        self.loop_depth = 0
        self.switch_depth = 0

        scope = [{}]
        for p in ast.params:
            scope[-1][p.name.name] = (p.var_type, False)
        self.visit(ast.body, scope)
        return None

    # ---------------------------------------------------------------
    # Types (return themselves)
    # ---------------------------------------------------------------
    def visitIntType(self, ast, o): return ast
    def visitFloatType(self, ast, o): return ast
    def visitBoolType(self, ast, o): return ast
    def visitStringType(self, ast, o): return ast
    def visitVoidType(self, ast, o): return ast
    def visitArrayType(self, ast, o): return ast
    def visitStructType(self, ast, o): return ast

    # ---------------------------------------------------------------
    # Statements
    # ---------------------------------------------------------------
    def visitBlock(self, ast: Block, o: list) -> Any:
        o.append({})
        for s in ast.stmts:
            self.visit(s, o)
        o.pop()
        return None

    def visitVarDecl(self, ast: VarDecl, o: list) -> Any:
        name = ast.name.name

        if name in self.param_names or name in o[-1]:
            raise Redeclared("Variable", name)

        if ast.var_type is not None:
            self._check_type_valid(ast.var_type)

        if ast.init is None:
            if ast.var_type is None:
                raise TypeCannotBeInferred(ast)
            var_type = ast.var_type
        elif type(ast.init) is ArrayLiteral and len(ast.init.elements) == 0 and ast.var_type is not None:
            # empty array literal with an explicit target type: no inference
            # needed, just check the declared size matches.
            if type(ast.var_type) is not ArrayType or ast.var_type.size != 0:
                raise TypeMismatchInStatement(ast)
            var_type = ast.var_type
        else:
            init_type = self.visit(ast.init, o)
            if ast.var_type is None:
                if type(init_type) is VoidType:
                    raise TypeCannotBeInferred(ast.init)
                var_type = init_type
            else:
                if not self._coercible(ast.var_type, init_type):
                    raise TypeMismatchInStatement(ast)
                var_type = ast.var_type

        o[-1][name] = (var_type, ast.is_mut)
        return None

    def visitIf(self, ast: If, o: list) -> Any:
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.then_stmt, o)
        if ast.else_stmt is not None:
            self.visit(ast.else_stmt, o)
        return None

    def visitWhile(self, ast: While, o: list) -> Any:
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.loop_depth += 1
        self.visit(ast.body, o)
        self.loop_depth -= 1
        return None

    def visitFor(self, ast: For, o: list) -> Any:
        start_t = self.visit(ast.start, o)
        end_t = self.visit(ast.end, o)
        if type(start_t) is not IntType or type(end_t) is not IntType:
            raise TypeMismatchInStatement(ast)

        o.append({ast.var_name.name: (IntType(), False)})
        self.loop_depth += 1
        self.visit(ast.body, o)
        self.loop_depth -= 1
        o.pop()
        return None

    def visitSwitch(self, ast: Switch, o: list) -> Any:
        expr_type = self.visit(ast.expr, o)
        if type(expr_type) not in (IntType, BoolType):
            raise TypeMismatchInStatement(ast)
        seen_vals = []
        self.switch_depth += 1
        for case in ast.cases:
            if case.val is not None:
                val_type = self.visit(case.val, o)
                if val_type != expr_type:
                    raise TypeMismatchInStatement(ast)
                if case.val in seen_vals:
                    raise TypeMismatchInStatement(ast)
                seen_vals.append(case.val)
            o.append({})
            for s in case.body:
                self.visit(s, o)
            o.pop()
        self.switch_depth -= 1
        return None

    def visitCase(self, ast: Case, o: Any) -> Any:
        return None  # handled inline in visitSwitch

    def visitBreak(self, ast: Break, o: Any) -> Any:
        if self.loop_depth == 0 and self.switch_depth == 0:
            raise MustInLoop(ast)
        return None

    def visitContinue(self, ast: Continue, o: Any) -> Any:
        if self.loop_depth == 0:
            raise MustInLoop(ast)
        return None

    def visitReturn(self, ast: Return, o: list) -> Any:
        if ast.expr is None:
            if type(self.return_type) is not VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            expr_type = self.visit(ast.expr, o)
            if not self._coercible(self.return_type, expr_type):
                raise TypeMismatchInStatement(ast)
        return None

    def visitExprStmt(self, ast: ExprStmt, o: list) -> Any:
        self.visit(ast.expr, o)
        return None

    # ---------------------------------------------------------------
    # Expressions (each returns its Type)
    # ---------------------------------------------------------------
    def visitBinaryOp(self, ast: BinaryOp, o: list) -> Any:
        lt = self.visit(ast.left, o)
        rt = self.visit(ast.right, o)
        op = ast.op

        if op in ("&&", "||"):
            if type(lt) is not BoolType or type(rt) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        if op in ("==", "!=", "<", "<=", ">", ">="):
            if type(lt) not in (IntType, FloatType) or type(rt) not in (IntType, FloatType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        if op == "%":
            if type(lt) is not IntType or type(rt) is not IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()

        if op in ("+", "-", "*", "/"):
            if type(lt) is IntType and type(rt) is IntType:
                return IntType()
            if type(lt) in (IntType, FloatType) and type(rt) in (IntType, FloatType):
                return FloatType()
            raise TypeMismatchInExpression(ast)

        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast: UnaryOp, o: list) -> Any:
        t = self.visit(ast.body, o)
        if ast.op == "-":
            if type(t) not in (IntType, FloatType):
                raise TypeMismatchInExpression(ast)
            return t
        if ast.op == "!":
            if type(t) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast: CallExpr, o: list) -> Any:
        fname = ast.name.name
        if fname not in self.funcs:
            raise UndeclaredFunction(fname)
        param_types, return_type = self.funcs[fname]
        arg_types = [self.visit(a, o) for a in ast.args]
        if len(arg_types) != len(param_types):
            raise TypeMismatchInExpression(ast)
        for at, pt in zip(arg_types, param_types):
            if not self._coercible(pt, at):
                raise TypeMismatchInExpression(ast)
        return return_type

    def visitId(self, ast: Id, o: list) -> Any:
        for frame in reversed(o):
            if ast.name in frame:
                return frame[ast.name][0]
        raise UndeclaredIdentifier(ast.name)

    def visitArrayCell(self, ast: ArrayCell, o: list) -> Any:
        arr_t = self.visit(ast.arr, o)
        idx_t = self.visit(ast.idx, o)
        if type(arr_t) is not ArrayType or type(idx_t) is not IntType:
            raise TypeMismatchInExpression(ast)
        return arr_t.element_type

    def visitFieldAccess(self, ast: FieldAccess, o: list) -> Any:
        obj_t = self.visit(ast.obj, o)
        if type(obj_t) is not StructType:
            raise TypeMismatchInExpression(ast)
        if obj_t.name.name not in self.structs:
            raise UndeclaredStruct(obj_t.name.name)
        for f in self.structs[obj_t.name.name].fields:
            if f.name.name == ast.field.name:
                return f.var_type
        raise TypeMismatchInExpression(ast)

    def visitStructInit(self, ast: StructInit, o: list) -> Any:
        struct_name = ast.name.name
        if struct_name not in self.structs:
            raise UndeclaredStruct(struct_name)
        decl_fields = {f.name.name: f.var_type for f in self.structs[struct_name].fields}

        given_names = [fi.name.name for fi in ast.initializers]
        if set(given_names) != set(decl_fields.keys()) or len(given_names) != len(decl_fields):
            raise TypeMismatchInExpression(ast)

        for fi in ast.initializers:
            val_t = self.visit(fi.expr, o)
            if not self._assignable(decl_fields[fi.name.name], val_t):
                raise TypeMismatchInExpression(ast)

        return StructType(Id(struct_name))

    def visitFieldInit(self, ast: FieldInit, o: Any) -> Any:
        return self.visit(ast.expr, o)

    def visitIntLiteral(self, ast, o): return IntType()
    def visitFloatLiteral(self, ast, o): return FloatType()
    def visitBoolLiteral(self, ast, o): return BoolType()
    def visitStringLiteral(self, ast, o): return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, o: list) -> Any:
        if len(ast.elements) == 0:
            raise TypeCannotBeInferred(ast)
        elem_type = self.visit(ast.elements[0], o)
        for e in ast.elements[1:]:
            t = self.visit(e, o)
            if t != elem_type:
                raise TypeMismatchInExpression(ast)
        return ArrayType(elem_type, len(ast.elements))

    def visitAssign(self, ast: Assign, o: list) -> Any:
        lhs_type = self._check_lvalue(ast.lhs, o)
        rhs_type = self.visit(ast.rhs, o)
        if not self._coercible(lhs_type, rhs_type):
            raise TypeMismatchInExpression(ast)
        return VoidType()

    def _check_lvalue(self, expr, o: list) -> Any:
        # `expr` is always the left-hand side expression itself,
        # which is what CannotAssignToConstant must report.
        if type(expr) is Id:
            for frame in reversed(o):
                if expr.name in frame:
                    typ, mutable = frame[expr.name]
                    if not mutable:
                        raise CannotAssignToConstant(expr)
                    return typ
            raise UndeclaredIdentifier(expr.name)

        if type(expr) is ArrayCell:
            self._check_root_mutable(expr.arr, o, expr)
            return self.visitArrayCell(expr, o)

        if type(expr) is FieldAccess:
            self._check_root_mutable(expr.obj, o, expr)
            return self.visitFieldAccess(expr, o)

        raise TypeMismatchInExpression(expr)

    def _check_root_mutable(self, expr, o: list, lhs_expr):
        cur = expr
        while type(cur) in (ArrayCell, FieldAccess):
            cur = cur.arr if type(cur) is ArrayCell else cur.obj
        if type(cur) is Id:
            for frame in reversed(o):
                if cur.name in frame:
                    if not frame[cur.name][1]:
                        raise CannotAssignToConstant(lhs_expr)
                    return
            raise UndeclaredIdentifier(cur.name)