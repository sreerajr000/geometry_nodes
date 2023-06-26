# Generated from gn.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .gnParser import gnParser
else:
    from gnParser import gnParser

# This class defines a complete listener for a parse tree produced by gnParser.
class gnListener(ParseTreeListener):

    # Enter a parse tree produced by gnParser#program.
    def enterProgram(self, ctx:gnParser.ProgramContext):
        pass

    # Exit a parse tree produced by gnParser#program.
    def exitProgram(self, ctx:gnParser.ProgramContext):
        pass


    # Enter a parse tree produced by gnParser#group.
    def enterGroup(self, ctx:gnParser.GroupContext):
        pass

    # Exit a parse tree produced by gnParser#group.
    def exitGroup(self, ctx:gnParser.GroupContext):
        pass


    # Enter a parse tree produced by gnParser#parameters.
    def enterParameters(self, ctx:gnParser.ParametersContext):
        pass

    # Exit a parse tree produced by gnParser#parameters.
    def exitParameters(self, ctx:gnParser.ParametersContext):
        pass


    # Enter a parse tree produced by gnParser#parameter.
    def enterParameter(self, ctx:gnParser.ParameterContext):
        pass

    # Exit a parse tree produced by gnParser#parameter.
    def exitParameter(self, ctx:gnParser.ParameterContext):
        pass


    # Enter a parse tree produced by gnParser#type.
    def enterType(self, ctx:gnParser.TypeContext):
        pass

    # Exit a parse tree produced by gnParser#type.
    def exitType(self, ctx:gnParser.TypeContext):
        pass


    # Enter a parse tree produced by gnParser#value.
    def enterValue(self, ctx:gnParser.ValueContext):
        pass

    # Exit a parse tree produced by gnParser#value.
    def exitValue(self, ctx:gnParser.ValueContext):
        pass


    # Enter a parse tree produced by gnParser#block.
    def enterBlock(self, ctx:gnParser.BlockContext):
        pass

    # Exit a parse tree produced by gnParser#block.
    def exitBlock(self, ctx:gnParser.BlockContext):
        pass


    # Enter a parse tree produced by gnParser#statement.
    def enterStatement(self, ctx:gnParser.StatementContext):
        pass

    # Exit a parse tree produced by gnParser#statement.
    def exitStatement(self, ctx:gnParser.StatementContext):
        pass


    # Enter a parse tree produced by gnParser#expr.
    def enterExpr(self, ctx:gnParser.ExprContext):
        pass

    # Exit a parse tree produced by gnParser#expr.
    def exitExpr(self, ctx:gnParser.ExprContext):
        pass


    # Enter a parse tree produced by gnParser#exprList.
    def enterExprList(self, ctx:gnParser.ExprListContext):
        pass

    # Exit a parse tree produced by gnParser#exprList.
    def exitExprList(self, ctx:gnParser.ExprListContext):
        pass



del gnParser