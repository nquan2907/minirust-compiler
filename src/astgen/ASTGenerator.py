from ast import expr
import sys
import os
from antlr4 import *

# Add grammar path to sys.path so we can import grammar classes cleanly
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "grammar"))

from MiniRustVisitor import MiniRustVisitor
from MiniRustParser import MiniRustParser
from utils.AST import *

class ASTGenerator(MiniRustVisitor):

    def visitProgram(self, ctx: MiniRustParser.ProgramContext):
        structs = [self.visit(s) for s in ctx.struct_expr()]   
        funcs = [self.visit(f) for f in ctx.funcDecl()]
        return Program(structs + funcs)

    def visitStruct_expr(self, ctx: MiniRustParser.Struct_exprContext):
        name = Id(ctx.ID().getText())
        fields = self._visit_field_decl_list(ctx.fieldDeclList())
        return StructDecl(name, fields)
    
    def visitFuncDecl(self, ctx: MiniRustParser.FuncDeclContext):
        name = Id(ctx.ID().getText())
        params = self._visit_param_list(ctx.paramList())  
        return_type = self.visit(ctx.typeExpr()) if ctx.typeExpr() else VoidType()
        body = self.visit(ctx.block())
        return FuncDecl(name, params, return_type, body)

# TYPE
    def visitTypeExpr(self, ctx: MiniRustParser.TypeExprContext):
        if ctx.I32():
            return IntType()
        elif ctx.F32():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        else:
            return StructType(Id(ctx.ID().getText()))
        
    def visitArrayType(self, ctx: MiniRustParser.ArrayTypeContext):
        elem = self.visit(ctx.typeExpr())
        size = int(ctx.INT_LIT().getText())
        return ArrayType(elem, size)

# STATEMENTS
    def visitBlock(self, ctx: MiniRustParser.BlockContext):
        return Block(self._visit_statement_list(ctx.statementList()))
    
    def visitStatement(self, ctx: MiniRustParser.StatementContext):
        if ctx.callExpr():
            return ExprStmt(self.visit(ctx.callExpr()))
        elif ctx.expr():
            return ExprStmt(self.visit(ctx.expr()))
        for get_sub in (ctx.vardecl, ctx.ifStmt, ctx.switchStmt, ctx.whileStmt,
                         ctx.forStmt, ctx.breakStmt, ctx.continueStmt,
                         ctx.returnStmt, ctx.block):
            sub = get_sub()
            if sub:
                return self.visit(sub)   
        
    def visitVardecl(self, ctx: MiniRustParser.VardeclContext):
        # 1 generic handler covers all 5 vardecl alternatives in the grammar
        name = Id(ctx.ID().getText())
        is_mut = ctx.MUT() is not None
        var_type = self.visit(ctx.typeExpr()) if ctx.typeExpr() else None
        init = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(name, var_type, init, is_mut)
    

    def visitIfStmt(self, ctx: MiniRustParser.IfStmtContext):
        cond = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.block())
        else_stmt = self.visit(ctx.elsePart()) if ctx.elsePart() else None
        return If(cond, then_stmt, else_stmt)
 
    def visitElsePart(self, ctx: MiniRustParser.ElsePartContext):
        if ctx.block():
            return self.visit(ctx.block())
        return self.visit(ctx.ifStmt())
 
    def visitSwitchStmt(self, ctx: MiniRustParser.SwitchStmtContext):
        expr = self.visit(ctx.expr())
        cases = self._visit_switch_body(ctx.switchBody())
        return Switch(expr, cases)
 
    def visitCaseClause(self, ctx: MiniRustParser.CaseClauseContext):
        value = self.visit(ctx.literal())
        body = self._visit_statement_list(ctx.statementList())
        return Case(value, body)          # body là list, không Block
 
    def visitDefaultClause(self, ctx: MiniRustParser.DefaultClauseContext):
        body = self._visit_statement_list(ctx.statementList())
        return Case(None, body) 
 
    def visitWhileStmt(self, ctx: MiniRustParser.WhileStmtContext):
        return While(self.visit(ctx.expr()), self.visit(ctx.block()))
 
    def visitForStmt(self, ctx: MiniRustParser.ForStmtContext):
        var_name = Id(ctx.ID().getText())
        start = self.visit(ctx.expr(0))
        end = self.visit(ctx.expr(1))
        return For(var_name, start, end, self.visit(ctx.block()))
 
    def visitBreakStmt(self, ctx): return Break()
 
    def visitContinueStmt(self, ctx): return Continue()
 
    def visitReturnStmt(self, ctx: MiniRustParser.ReturnStmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)
    
   # ---------- Expressions ----------
 
    def visitExpr(self, ctx: MiniRustParser.ExprContext):
        return self.visit(ctx.assign_expr())
 
    def visitAssign_expr(self, ctx: MiniRustParser.Assign_exprContext):
        if ctx.ASSIGN() and not ctx.or_expr():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.assign_expr()))
        if ctx.ASSIGN() and ctx.LBRACK():
            arr = self.visit(ctx.or_expr())
            idx = self.visit(ctx.expr())
            return Assign(ArrayCell(arr, idx), self.visit(ctx.assign_expr()))
        if ctx.ASSIGN() and ctx.or_expr():
            obj = self.visit(ctx.or_expr())
            return Assign(FieldAccess(obj, Id(ctx.ID().getText())), self.visit(ctx.assign_expr()))
        return self.visit(ctx.or_expr())
 
    def visitOr_expr(self, ctx: MiniRustParser.Or_exprContext):
        if ctx.or_expr():
            return BinaryOp('||', self.visit(ctx.or_expr()), self.visit(ctx.and_expr()))
        return self.visit(ctx.and_expr())
 
    def visitAnd_expr(self, ctx: MiniRustParser.And_exprContext):
        if ctx.and_expr():
            return BinaryOp('&&', self.visit(ctx.and_expr()), self.visit(ctx.eq_expr()))
        return self.visit(ctx.eq_expr())
 
    def visitEq_expr(self, ctx: MiniRustParser.Eq_exprContext):
        rels = ctx.rel_expr()
        if len(rels) == 1:
            return self.visit(rels[0])
        op = '==' if ctx.EQ() else '!='
        return BinaryOp(op, self.visit(rels[0]), self.visit(rels[1]))
 
    def visitRel_expr(self, ctx: MiniRustParser.Rel_exprContext):
        adds = ctx.add_expr()
        if len(adds) == 1:
            return self.visit(adds[0])
        if ctx.LTE(): op = '<='
        elif ctx.GTE(): op = '>='
        elif ctx.GT(): op = '>'
        else: op = '<'
        return BinaryOp(op, self.visit(adds[0]), self.visit(adds[1]))
 
    def visitAdd_expr(self, ctx: MiniRustParser.Add_exprContext):
        if ctx.add_expr():
            op = '+' if ctx.ADD() else '-'
            return BinaryOp(op, self.visit(ctx.add_expr()), self.visit(ctx.mul_expr()))
        return self.visit(ctx.mul_expr())
 
    def visitMul_expr(self, ctx: MiniRustParser.Mul_exprContext):
        if ctx.mul_expr():
            op = '*' if ctx.MUL() else ('/' if ctx.DIV() else '%')
            return BinaryOp(op, self.visit(ctx.mul_expr()), self.visit(ctx.una_expr()))
        return self.visit(ctx.una_expr())
 
    def visitUna_expr(self, ctx: MiniRustParser.Una_exprContext):
        if ctx.SUB():
            return UnaryOp('-', self.visit(ctx.una_expr()))
        if ctx.NOT():
            return UnaryOp('!', self.visit(ctx.una_expr()))
        return self.visit(ctx.primary_expr())
 
    def visitPrimary_expr(self, ctx: MiniRustParser.Primary_exprContext):
        if ctx.LBRACK() and ctx.primary_expr():
            return ArrayCell(self.visit(ctx.primary_expr()), self.visit(ctx.expr()))
        if ctx.DOT():
            return FieldAccess(self.visit(ctx.primary_expr()), Id(ctx.ID().getText()))
        if ctx.LPAREN() and ctx.ID():
            args = self._visit_arg_list(ctx.argList())
            return CallExpr(Id(ctx.ID().getText()), args)
        if ctx.LPAREN():
            return self.visit(ctx.expr())
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.TRUE():
            return BoolLiteral(True)
        if ctx.FALSE():
            return BoolLiteral(False)
        if ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        if ctx.structLiteral():
            return self.visit(ctx.structLiteral())
        return Id(ctx.ID().getText())


    # Handle call expressions
    def visitCallExpr(self, ctx: MiniRustParser.CallExprContext):
        args = self._visit_arg_list(ctx.argList())
        return CallExpr(Id(ctx.ID().getText()), args)

    def visitStructLiteral(self, ctx: MiniRustParser.StructLiteralContext):
        name = Id(ctx.ID().getText())
        inits = self._visit_initializer_list(ctx.initializerList())
        return StructInit(name, inits)
 
    def visitArrayLiteral(self, ctx: MiniRustParser.ArrayLiteralContext):
        if ctx.array_list():
            return ArrayLiteral(self._visit_array_list(ctx.array_list()))
        return ArrayLiteral([])
 
    def visitLiteral(self, ctx: MiniRustParser.LiteralContext):
        if ctx.INT_LIT(): return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT(): return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.TRUE(): return BoolLiteral(True)
        if ctx.FALSE(): return BoolLiteral(False)
        return StringLiteral(ctx.STRING_LITERAL().getText())
 
    # ---------- Helpers: flatten left-recursive list rules ----------
 
    def _visit_statement_list(self, ctx):
        stmts = []
        while ctx and ctx.statement():
            stmts.append(self.visit(ctx.statement()))
            ctx = ctx.statementList()
        return stmts
 
    def _visit_param_list(self, ctx):
        params = []
        if ctx is None or ctx.paramListPrime() is None:
            return params
        prime = ctx.paramListPrime()
        while prime:
            p = prime.param()
            params.append(VarDecl(Id(p.ID().getText()), self.visit(p.typeExpr()), None, False))
            prime = prime.paramListPrime()
        return params
 
    def _visit_arg_list(self, ctx):
        args = []
        if ctx is None or ctx.argListprime() is None:
            return args
        prime = ctx.argListprime()
        while prime:
            args.append(self.visit(prime.expr()))
            prime = prime.argListprime()
        return args
 
    def _visit_field_decl_list(self, ctx):
        fields = []
        while ctx:
            fd = ctx.fieldDec()
            fields.append(VarDecl(Id(fd.ID().getText()), self.visit(fd.typeExpr()), None, False))
            ctx = ctx.fieldDeclList()
        return fields
 
    def _visit_initializer_list(self, ctx):
        inits = []
        while ctx:
            d = ctx.initializerDec()
            inits.append(FieldInit(Id(d.ID().getText()), self.visit(d.expr())))
            ctx = ctx.initializerList()
        return inits
 
    def _visit_array_list(self, ctx):
        elems = []
        while ctx:
            elems.append(self.visit(ctx.expr()))
            ctx = ctx.array_list()
        return elems

    def _visit_switch_body(self, ctx):
        """Gộp case + default, sắp xếp lại theo đúng vị trí xuất hiện trong code."""
        clauses = list(ctx.caseClause())
        default_ctx = ctx.defaultClause()
        if default_ctx:
            clauses.append(default_ctx)

        # sort theo token index 
        clauses.sort(key=lambda c: c.start.tokenIndex)

        return [self.visit(c) for c in clauses]