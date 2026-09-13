# Generated from E:/PPL BTL/minirust-assignment-2453063/src/grammar/MiniRust.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniRustParser import MiniRustParser
else:
    from MiniRustParser import MiniRustParser

# This class defines a complete generic visitor for a parse tree produced by MiniRustParser.

class MiniRustVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniRustParser#program.
    def visitProgram(self, ctx:MiniRustParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#typeExpr.
    def visitTypeExpr(self, ctx:MiniRustParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MiniRustParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#array_list.
    def visitArray_list(self, ctx:MiniRustParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#arrayType.
    def visitArrayType(self, ctx:MiniRustParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniRustParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#paramList.
    def visitParamList(self, ctx:MiniRustParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#paramListPrime.
    def visitParamListPrime(self, ctx:MiniRustParser.ParamListPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#param.
    def visitParam(self, ctx:MiniRustParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#block.
    def visitBlock(self, ctx:MiniRustParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#statementList.
    def visitStatementList(self, ctx:MiniRustParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#statement.
    def visitStatement(self, ctx:MiniRustParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#callExpr.
    def visitCallExpr(self, ctx:MiniRustParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#expr.
    def visitExpr(self, ctx:MiniRustParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#assign_expr.
    def visitAssign_expr(self, ctx:MiniRustParser.Assign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#or_expr.
    def visitOr_expr(self, ctx:MiniRustParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#and_expr.
    def visitAnd_expr(self, ctx:MiniRustParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#eq_expr.
    def visitEq_expr(self, ctx:MiniRustParser.Eq_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#rel_expr.
    def visitRel_expr(self, ctx:MiniRustParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#add_expr.
    def visitAdd_expr(self, ctx:MiniRustParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#mul_expr.
    def visitMul_expr(self, ctx:MiniRustParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#una_expr.
    def visitUna_expr(self, ctx:MiniRustParser.Una_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniRustParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#argList.
    def visitArgList(self, ctx:MiniRustParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#argListprime.
    def visitArgListprime(self, ctx:MiniRustParser.ArgListprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#struct_expr.
    def visitStruct_expr(self, ctx:MiniRustParser.Struct_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#fieldDeclList.
    def visitFieldDeclList(self, ctx:MiniRustParser.FieldDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#fieldDec.
    def visitFieldDec(self, ctx:MiniRustParser.FieldDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#structLiteral.
    def visitStructLiteral(self, ctx:MiniRustParser.StructLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#initializerList.
    def visitInitializerList(self, ctx:MiniRustParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#initializerDec.
    def visitInitializerDec(self, ctx:MiniRustParser.InitializerDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#vardecl.
    def visitVardecl(self, ctx:MiniRustParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#ifStmt.
    def visitIfStmt(self, ctx:MiniRustParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#elsePart.
    def visitElsePart(self, ctx:MiniRustParser.ElsePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#switchStmt.
    def visitSwitchStmt(self, ctx:MiniRustParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#switchBody.
    def visitSwitchBody(self, ctx:MiniRustParser.SwitchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#switchClause.
    def visitSwitchClause(self, ctx:MiniRustParser.SwitchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#caseClause.
    def visitCaseClause(self, ctx:MiniRustParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#defaultClause.
    def visitDefaultClause(self, ctx:MiniRustParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#literal.
    def visitLiteral(self, ctx:MiniRustParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#whileStmt.
    def visitWhileStmt(self, ctx:MiniRustParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#forStmt.
    def visitForStmt(self, ctx:MiniRustParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniRustParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#continueStmt.
    def visitContinueStmt(self, ctx:MiniRustParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRustParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniRustParser.ReturnStmtContext):
        return self.visitChildren(ctx)



del MiniRustParser