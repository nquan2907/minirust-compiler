# Generated from E:/PPL BTL/minirust-assignment-2453063/src/grammar/MiniRust.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniRustParser import MiniRustParser
else:
    from MiniRustParser import MiniRustParser

# This class defines a complete listener for a parse tree produced by MiniRustParser.
class MiniRustListener(ParseTreeListener):

    # Enter a parse tree produced by MiniRustParser#program.
    def enterProgram(self, ctx:MiniRustParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniRustParser#program.
    def exitProgram(self, ctx:MiniRustParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniRustParser#typeExpr.
    def enterTypeExpr(self, ctx:MiniRustParser.TypeExprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#typeExpr.
    def exitTypeExpr(self, ctx:MiniRustParser.TypeExprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:MiniRustParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by MiniRustParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:MiniRustParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by MiniRustParser#array_list.
    def enterArray_list(self, ctx:MiniRustParser.Array_listContext):
        pass

    # Exit a parse tree produced by MiniRustParser#array_list.
    def exitArray_list(self, ctx:MiniRustParser.Array_listContext):
        pass


    # Enter a parse tree produced by MiniRustParser#arrayType.
    def enterArrayType(self, ctx:MiniRustParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MiniRustParser#arrayType.
    def exitArrayType(self, ctx:MiniRustParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MiniRustParser#funcDecl.
    def enterFuncDecl(self, ctx:MiniRustParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MiniRustParser#funcDecl.
    def exitFuncDecl(self, ctx:MiniRustParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MiniRustParser#paramList.
    def enterParamList(self, ctx:MiniRustParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniRustParser#paramList.
    def exitParamList(self, ctx:MiniRustParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniRustParser#paramListPrime.
    def enterParamListPrime(self, ctx:MiniRustParser.ParamListPrimeContext):
        pass

    # Exit a parse tree produced by MiniRustParser#paramListPrime.
    def exitParamListPrime(self, ctx:MiniRustParser.ParamListPrimeContext):
        pass


    # Enter a parse tree produced by MiniRustParser#param.
    def enterParam(self, ctx:MiniRustParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniRustParser#param.
    def exitParam(self, ctx:MiniRustParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniRustParser#block.
    def enterBlock(self, ctx:MiniRustParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniRustParser#block.
    def exitBlock(self, ctx:MiniRustParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniRustParser#statementList.
    def enterStatementList(self, ctx:MiniRustParser.StatementListContext):
        pass

    # Exit a parse tree produced by MiniRustParser#statementList.
    def exitStatementList(self, ctx:MiniRustParser.StatementListContext):
        pass


    # Enter a parse tree produced by MiniRustParser#statement.
    def enterStatement(self, ctx:MiniRustParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniRustParser#statement.
    def exitStatement(self, ctx:MiniRustParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniRustParser#callExpr.
    def enterCallExpr(self, ctx:MiniRustParser.CallExprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#callExpr.
    def exitCallExpr(self, ctx:MiniRustParser.CallExprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#expr.
    def enterExpr(self, ctx:MiniRustParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#expr.
    def exitExpr(self, ctx:MiniRustParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#assign_expr.
    def enterAssign_expr(self, ctx:MiniRustParser.Assign_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#assign_expr.
    def exitAssign_expr(self, ctx:MiniRustParser.Assign_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#or_expr.
    def enterOr_expr(self, ctx:MiniRustParser.Or_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#or_expr.
    def exitOr_expr(self, ctx:MiniRustParser.Or_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#and_expr.
    def enterAnd_expr(self, ctx:MiniRustParser.And_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#and_expr.
    def exitAnd_expr(self, ctx:MiniRustParser.And_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#eq_expr.
    def enterEq_expr(self, ctx:MiniRustParser.Eq_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#eq_expr.
    def exitEq_expr(self, ctx:MiniRustParser.Eq_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#rel_expr.
    def enterRel_expr(self, ctx:MiniRustParser.Rel_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#rel_expr.
    def exitRel_expr(self, ctx:MiniRustParser.Rel_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#add_expr.
    def enterAdd_expr(self, ctx:MiniRustParser.Add_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#add_expr.
    def exitAdd_expr(self, ctx:MiniRustParser.Add_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#mul_expr.
    def enterMul_expr(self, ctx:MiniRustParser.Mul_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#mul_expr.
    def exitMul_expr(self, ctx:MiniRustParser.Mul_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#una_expr.
    def enterUna_expr(self, ctx:MiniRustParser.Una_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#una_expr.
    def exitUna_expr(self, ctx:MiniRustParser.Una_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#primary_expr.
    def enterPrimary_expr(self, ctx:MiniRustParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#primary_expr.
    def exitPrimary_expr(self, ctx:MiniRustParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#argList.
    def enterArgList(self, ctx:MiniRustParser.ArgListContext):
        pass

    # Exit a parse tree produced by MiniRustParser#argList.
    def exitArgList(self, ctx:MiniRustParser.ArgListContext):
        pass


    # Enter a parse tree produced by MiniRustParser#argListprime.
    def enterArgListprime(self, ctx:MiniRustParser.ArgListprimeContext):
        pass

    # Exit a parse tree produced by MiniRustParser#argListprime.
    def exitArgListprime(self, ctx:MiniRustParser.ArgListprimeContext):
        pass


    # Enter a parse tree produced by MiniRustParser#struct_expr.
    def enterStruct_expr(self, ctx:MiniRustParser.Struct_exprContext):
        pass

    # Exit a parse tree produced by MiniRustParser#struct_expr.
    def exitStruct_expr(self, ctx:MiniRustParser.Struct_exprContext):
        pass


    # Enter a parse tree produced by MiniRustParser#fieldDeclList.
    def enterFieldDeclList(self, ctx:MiniRustParser.FieldDeclListContext):
        pass

    # Exit a parse tree produced by MiniRustParser#fieldDeclList.
    def exitFieldDeclList(self, ctx:MiniRustParser.FieldDeclListContext):
        pass


    # Enter a parse tree produced by MiniRustParser#fieldDec.
    def enterFieldDec(self, ctx:MiniRustParser.FieldDecContext):
        pass

    # Exit a parse tree produced by MiniRustParser#fieldDec.
    def exitFieldDec(self, ctx:MiniRustParser.FieldDecContext):
        pass


    # Enter a parse tree produced by MiniRustParser#structLiteral.
    def enterStructLiteral(self, ctx:MiniRustParser.StructLiteralContext):
        pass

    # Exit a parse tree produced by MiniRustParser#structLiteral.
    def exitStructLiteral(self, ctx:MiniRustParser.StructLiteralContext):
        pass


    # Enter a parse tree produced by MiniRustParser#initializerList.
    def enterInitializerList(self, ctx:MiniRustParser.InitializerListContext):
        pass

    # Exit a parse tree produced by MiniRustParser#initializerList.
    def exitInitializerList(self, ctx:MiniRustParser.InitializerListContext):
        pass


    # Enter a parse tree produced by MiniRustParser#initializerDec.
    def enterInitializerDec(self, ctx:MiniRustParser.InitializerDecContext):
        pass

    # Exit a parse tree produced by MiniRustParser#initializerDec.
    def exitInitializerDec(self, ctx:MiniRustParser.InitializerDecContext):
        pass


    # Enter a parse tree produced by MiniRustParser#vardecl.
    def enterVardecl(self, ctx:MiniRustParser.VardeclContext):
        pass

    # Exit a parse tree produced by MiniRustParser#vardecl.
    def exitVardecl(self, ctx:MiniRustParser.VardeclContext):
        pass


    # Enter a parse tree produced by MiniRustParser#ifStmt.
    def enterIfStmt(self, ctx:MiniRustParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#ifStmt.
    def exitIfStmt(self, ctx:MiniRustParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#elsePart.
    def enterElsePart(self, ctx:MiniRustParser.ElsePartContext):
        pass

    # Exit a parse tree produced by MiniRustParser#elsePart.
    def exitElsePart(self, ctx:MiniRustParser.ElsePartContext):
        pass


    # Enter a parse tree produced by MiniRustParser#switchStmt.
    def enterSwitchStmt(self, ctx:MiniRustParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#switchStmt.
    def exitSwitchStmt(self, ctx:MiniRustParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#switchBody.
    def enterSwitchBody(self, ctx:MiniRustParser.SwitchBodyContext):
        pass

    # Exit a parse tree produced by MiniRustParser#switchBody.
    def exitSwitchBody(self, ctx:MiniRustParser.SwitchBodyContext):
        pass


    # Enter a parse tree produced by MiniRustParser#switchClause.
    def enterSwitchClause(self, ctx:MiniRustParser.SwitchClauseContext):
        pass

    # Exit a parse tree produced by MiniRustParser#switchClause.
    def exitSwitchClause(self, ctx:MiniRustParser.SwitchClauseContext):
        pass


    # Enter a parse tree produced by MiniRustParser#caseClause.
    def enterCaseClause(self, ctx:MiniRustParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by MiniRustParser#caseClause.
    def exitCaseClause(self, ctx:MiniRustParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by MiniRustParser#defaultClause.
    def enterDefaultClause(self, ctx:MiniRustParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by MiniRustParser#defaultClause.
    def exitDefaultClause(self, ctx:MiniRustParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by MiniRustParser#literal.
    def enterLiteral(self, ctx:MiniRustParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniRustParser#literal.
    def exitLiteral(self, ctx:MiniRustParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniRustParser#whileStmt.
    def enterWhileStmt(self, ctx:MiniRustParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#whileStmt.
    def exitWhileStmt(self, ctx:MiniRustParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#forStmt.
    def enterForStmt(self, ctx:MiniRustParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#forStmt.
    def exitForStmt(self, ctx:MiniRustParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#breakStmt.
    def enterBreakStmt(self, ctx:MiniRustParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#breakStmt.
    def exitBreakStmt(self, ctx:MiniRustParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#continueStmt.
    def enterContinueStmt(self, ctx:MiniRustParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#continueStmt.
    def exitContinueStmt(self, ctx:MiniRustParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by MiniRustParser#returnStmt.
    def enterReturnStmt(self, ctx:MiniRustParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MiniRustParser#returnStmt.
    def exitReturnStmt(self, ctx:MiniRustParser.ReturnStmtContext):
        pass



del MiniRustParser