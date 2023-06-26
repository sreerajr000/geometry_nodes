# Generated from .\Expression.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#program.
    def enterProgram(self, ctx:ExpressionParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExpressionParser#program.
    def exitProgram(self, ctx:ExpressionParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExpressionParser#statement.
    def enterStatement(self, ctx:ExpressionParser.StatementContext):
        pass

    # Exit a parse tree produced by ExpressionParser#statement.
    def exitStatement(self, ctx:ExpressionParser.StatementContext):
        pass


    # Enter a parse tree produced by ExpressionParser#assignment.
    def enterAssignment(self, ctx:ExpressionParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExpressionParser#assignment.
    def exitAssignment(self, ctx:ExpressionParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExpressionParser#expression.
    def enterExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#expression.
    def exitExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#additiveExp.
    def enterAdditiveExp(self, ctx:ExpressionParser.AdditiveExpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#additiveExp.
    def exitAdditiveExp(self, ctx:ExpressionParser.AdditiveExpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#multiplicativeExp.
    def enterMultiplicativeExp(self, ctx:ExpressionParser.MultiplicativeExpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#multiplicativeExp.
    def exitMultiplicativeExp(self, ctx:ExpressionParser.MultiplicativeExpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#unaryExp.
    def enterUnaryExp(self, ctx:ExpressionParser.UnaryExpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#unaryExp.
    def exitUnaryExp(self, ctx:ExpressionParser.UnaryExpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#binaryExp.
    def enterBinaryExp(self, ctx:ExpressionParser.BinaryExpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#binaryExp.
    def exitBinaryExp(self, ctx:ExpressionParser.BinaryExpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#factor.
    def enterFactor(self, ctx:ExpressionParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpressionParser#factor.
    def exitFactor(self, ctx:ExpressionParser.FactorContext):
        pass


    # Enter a parse tree produced by ExpressionParser#unaryOp.
    def enterUnaryOp(self, ctx:ExpressionParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#unaryOp.
    def exitUnaryOp(self, ctx:ExpressionParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#binaryOp.
    def enterBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#binaryOp.
    def exitBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        pass



del ExpressionParser