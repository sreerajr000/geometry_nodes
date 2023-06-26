# Generated from gn.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .gnParser import gnParser
else:
    from gnParser import gnParser

# This class defines a complete generic visitor for a parse tree produced by gnParser.

class gnVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gnParser#program.
    def visitProgram(self, ctx:gnParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#group.
    def visitGroup(self, ctx:gnParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#parameters.
    def visitParameters(self, ctx:gnParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#parameter.
    def visitParameter(self, ctx:gnParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#type.
    def visitType(self, ctx:gnParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#value.
    def visitValue(self, ctx:gnParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#block.
    def visitBlock(self, ctx:gnParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#statement.
    def visitStatement(self, ctx:gnParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#expr.
    def visitExpr(self, ctx:gnParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#exprList.
    def visitExprList(self, ctx:gnParser.ExprListContext):
        return self.visitChildren(ctx)



del gnParser