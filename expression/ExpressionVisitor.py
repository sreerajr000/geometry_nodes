# Generated from .\Expression.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#program.
    def visitProgram(self, ctx:ExpressionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#statement.
    def visitStatement(self, ctx:ExpressionParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#assignment.
    def visitAssignment(self, ctx:ExpressionParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#expression.
    def visitExpression(self, ctx:ExpressionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#additiveExp.
    def visitAdditiveExp(self, ctx:ExpressionParser.AdditiveExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#multiplicativeExp.
    def visitMultiplicativeExp(self, ctx:ExpressionParser.MultiplicativeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#unaryExp.
    def visitUnaryExp(self, ctx:ExpressionParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#binaryExp.
    def visitBinaryExp(self, ctx:ExpressionParser.BinaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#factor.
    def visitFactor(self, ctx:ExpressionParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#unaryOp.
    def visitUnaryOp(self, ctx:ExpressionParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#binaryOp.
    def visitBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        return self.visitChildren(ctx)



del ExpressionParser