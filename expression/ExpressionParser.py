# Generated from .\Expression.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,
        4,5,4,44,8,4,10,4,12,4,47,9,4,1,5,1,5,1,5,5,5,52,8,5,10,5,12,5,55,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,73,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,9,1,9,1,10,
        1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,4,5,1,0,6,7,
        1,0,11,25,1,0,26,34,83,0,25,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,
        38,1,0,0,0,8,40,1,0,0,0,10,48,1,0,0,0,12,62,1,0,0,0,14,72,1,0,0,
        0,16,80,1,0,0,0,18,82,1,0,0,0,20,84,1,0,0,0,22,24,3,2,1,0,23,22,
        1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,
        27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,33,3,4,2,0,31,33,3,6,
        3,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,0,35,36,
        5,3,0,0,36,37,3,6,3,0,37,5,1,0,0,0,38,39,3,8,4,0,39,7,1,0,0,0,40,
        45,3,10,5,0,41,42,7,0,0,0,42,44,3,10,5,0,43,41,1,0,0,0,44,47,1,0,
        0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,9,1,0,0,0,47,45,1,0,0,0,48,53,
        3,12,6,0,49,50,7,1,0,0,50,52,3,12,6,0,51,49,1,0,0,0,52,55,1,0,0,
        0,53,51,1,0,0,0,53,54,1,0,0,0,54,11,1,0,0,0,55,53,1,0,0,0,56,57,
        3,18,9,0,57,58,5,8,0,0,58,59,3,6,3,0,59,60,5,9,0,0,60,63,1,0,0,0,
        61,63,3,14,7,0,62,56,1,0,0,0,62,61,1,0,0,0,63,13,1,0,0,0,64,65,3,
        20,10,0,65,66,5,8,0,0,66,67,3,6,3,0,67,68,5,10,0,0,68,69,3,6,3,0,
        69,70,5,9,0,0,70,73,1,0,0,0,71,73,3,16,8,0,72,64,1,0,0,0,72,71,1,
        0,0,0,73,15,1,0,0,0,74,81,5,2,0,0,75,81,5,1,0,0,76,77,5,8,0,0,77,
        78,3,8,4,0,78,79,5,9,0,0,79,81,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,
        0,80,76,1,0,0,0,81,17,1,0,0,0,82,83,7,2,0,0,83,19,1,0,0,0,84,85,
        7,3,0,0,85,21,1,0,0,0,7,25,32,45,53,62,72,80
    ]

class ExpressionParser ( Parser ):

    grammarFileName = "Expression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'", "','", "'sin'", 
                     "'cos'", "'tan'", "'asin'", "'acos'", "'atan'", "'abs'", 
                     "'floor'", "'ceil'", "'fract'", "'inverse'", "'sign'", 
                     "'exp'", "'rad'", "'deg'", "'pow'", "'log'", "'min'", 
                     "'max'", "'round'", "'lt'", "'gt'", "'mod'", "'sqrt'" ]

    symbolicNames = [ "<INVALID>", "ID", "NUMBER", "ASSIGN", "PLUS", "MINUS", 
                      "TIMES", "DIV", "LPAREN", "RPAREN", "COMMA", "SIN", 
                      "COS", "TAN", "ASIN", "ACOS", "ATAN", "ABS", "FLOOR", 
                      "CEIL", "FRACT", "INVERSE", "SIGN", "EXP", "RAD", 
                      "DEG", "POW", "LOG", "MIN", "MAX", "ROUND", "LT", 
                      "GT", "MOD", "SQRT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_additiveExp = 4
    RULE_multiplicativeExp = 5
    RULE_unaryExp = 6
    RULE_binaryExp = 7
    RULE_factor = 8
    RULE_unaryOp = 9
    RULE_binaryOp = 10

    ruleNames =  [ "program", "statement", "assignment", "expression", "additiveExp", 
                   "multiplicativeExp", "unaryExp", "binaryExp", "factor", 
                   "unaryOp", "binaryOp" ]

    EOF = Token.EOF
    ID=1
    NUMBER=2
    ASSIGN=3
    PLUS=4
    MINUS=5
    TIMES=6
    DIV=7
    LPAREN=8
    RPAREN=9
    COMMA=10
    SIN=11
    COS=12
    TAN=13
    ASIN=14
    ACOS=15
    ATAN=16
    ABS=17
    FLOOR=18
    CEIL=19
    FRACT=20
    INVERSE=21
    SIGN=22
    EXP=23
    RAD=24
    DEG=25
    POW=26
    LOG=27
    MIN=28
    MAX=29
    ROUND=30
    LT=31
    GT=32
    MOD=33
    SQRT=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExpressionParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExpressionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359736582) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(ExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ExpressionParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExpressionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExpressionParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExpressionParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ExpressionParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ExpressionParser.ID)
            self.state = 35
            self.match(ExpressionParser.ASSIGN)
            self.state = 36
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExp(self):
            return self.getTypedRuleContext(ExpressionParser.AdditiveExpContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ExpressionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.additiveExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.MultiplicativeExpContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.MultiplicativeExpContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.PLUS)
            else:
                return self.getToken(ExpressionParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.MINUS)
            else:
                return self.getToken(ExpressionParser.MINUS, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_additiveExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExp" ):
                listener.enterAdditiveExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExp" ):
                listener.exitAdditiveExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExp" ):
                return visitor.visitAdditiveExp(self)
            else:
                return visitor.visitChildren(self)




    def additiveExp(self):

        localctx = ExpressionParser.AdditiveExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_additiveExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.multiplicativeExp()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 41
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                self.multiplicativeExp()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.UnaryExpContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.UnaryExpContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.TIMES)
            else:
                return self.getToken(ExpressionParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.DIV)
            else:
                return self.getToken(ExpressionParser.DIV, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_multiplicativeExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExp" ):
                listener.enterMultiplicativeExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExp" ):
                listener.exitMultiplicativeExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExp" ):
                return visitor.visitMultiplicativeExp(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExp(self):

        localctx = ExpressionParser.MultiplicativeExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiplicativeExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.unaryExp()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50
                self.unaryExp()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOp(self):
            return self.getTypedRuleContext(ExpressionParser.UnaryOpContext,0)


        def LPAREN(self):
            return self.getToken(ExpressionParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionParser.RPAREN, 0)

        def binaryExp(self):
            return self.getTypedRuleContext(ExpressionParser.BinaryExpContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_unaryExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExp" ):
                listener.enterUnaryExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExp" ):
                listener.exitUnaryExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExp" ):
                return visitor.visitUnaryExp(self)
            else:
                return visitor.visitChildren(self)




    def unaryExp(self):

        localctx = ExpressionParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unaryExp)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.unaryOp()
                self.state = 57
                self.match(ExpressionParser.LPAREN)
                self.state = 58
                self.expression()
                self.state = 59
                self.match(ExpressionParser.RPAREN)
                pass
            elif token in [1, 2, 8, 26, 27, 28, 29, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.binaryExp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryOp(self):
            return self.getTypedRuleContext(ExpressionParser.BinaryOpContext,0)


        def LPAREN(self):
            return self.getToken(ExpressionParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(ExpressionParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(ExpressionParser.RPAREN, 0)

        def factor(self):
            return self.getTypedRuleContext(ExpressionParser.FactorContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_binaryExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExp" ):
                listener.enterBinaryExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExp" ):
                listener.exitBinaryExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExp" ):
                return visitor.visitBinaryExp(self)
            else:
                return visitor.visitChildren(self)




    def binaryExp(self):

        localctx = ExpressionParser.BinaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binaryExp)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.binaryOp()
                self.state = 65
                self.match(ExpressionParser.LPAREN)
                self.state = 66
                self.expression()
                self.state = 67
                self.match(ExpressionParser.COMMA)
                self.state = 68
                self.expression()
                self.state = 69
                self.match(ExpressionParser.RPAREN)
                pass
            elif token in [1, 2, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExpressionParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ExpressionParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExpressionParser.LPAREN, 0)

        def additiveExp(self):
            return self.getTypedRuleContext(ExpressionParser.AdditiveExpContext,0)


        def RPAREN(self):
            return self.getToken(ExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ExpressionParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ExpressionParser.NUMBER)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(ExpressionParser.ID)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(ExpressionParser.LPAREN)
                self.state = 77
                self.additiveExp()
                self.state = 78
                self.match(ExpressionParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(ExpressionParser.SIN, 0)

        def COS(self):
            return self.getToken(ExpressionParser.COS, 0)

        def TAN(self):
            return self.getToken(ExpressionParser.TAN, 0)

        def ASIN(self):
            return self.getToken(ExpressionParser.ASIN, 0)

        def ACOS(self):
            return self.getToken(ExpressionParser.ACOS, 0)

        def ATAN(self):
            return self.getToken(ExpressionParser.ATAN, 0)

        def ABS(self):
            return self.getToken(ExpressionParser.ABS, 0)

        def FLOOR(self):
            return self.getToken(ExpressionParser.FLOOR, 0)

        def CEIL(self):
            return self.getToken(ExpressionParser.CEIL, 0)

        def FRACT(self):
            return self.getToken(ExpressionParser.FRACT, 0)

        def INVERSE(self):
            return self.getToken(ExpressionParser.INVERSE, 0)

        def SIGN(self):
            return self.getToken(ExpressionParser.SIGN, 0)

        def EXP(self):
            return self.getToken(ExpressionParser.EXP, 0)

        def RAD(self):
            return self.getToken(ExpressionParser.RAD, 0)

        def DEG(self):
            return self.getToken(ExpressionParser.DEG, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = ExpressionParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67106816) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POW(self):
            return self.getToken(ExpressionParser.POW, 0)

        def LOG(self):
            return self.getToken(ExpressionParser.LOG, 0)

        def MIN(self):
            return self.getToken(ExpressionParser.MIN, 0)

        def MAX(self):
            return self.getToken(ExpressionParser.MAX, 0)

        def ROUND(self):
            return self.getToken(ExpressionParser.ROUND, 0)

        def LT(self):
            return self.getToken(ExpressionParser.LT, 0)

        def GT(self):
            return self.getToken(ExpressionParser.GT, 0)

        def MOD(self):
            return self.getToken(ExpressionParser.MOD, 0)

        def SQRT(self):
            return self.getToken(ExpressionParser.SQRT, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = ExpressionParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34292629504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





