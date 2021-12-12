# Generated from python.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\3\3\3\3\4\3\4\5\4\23\n\4\3\4\3\4\5\4\27\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\36\n\4\3\4\2\2\5\2\4\6\2\2\2!\2\13")
        buf.write("\3\2\2\2\4\16\3\2\2\2\6\20\3\2\2\2\b\n\5\4\3\2\t\b\3\2")
        buf.write("\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2")
        buf.write("\r\13\3\2\2\2\16\17\5\6\4\2\17\5\3\2\2\2\20\22\7\6\2\2")
        buf.write("\21\23\7\3\2\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\26\7\4\2\2\25\27\7\3\2\2\26\25\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\35\3\2\2\2\30\31\7\5\2\2\31\32\7\t\2\2\32\36\7")
        buf.write("\5\2\2\33\36\7\7\2\2\34\36\7\6\2\2\35\30\3\2\2\2\35\33")
        buf.write("\3\2\2\2\35\34\3\2\2\2\36\7\3\2\2\2\6\13\22\26\35")
        return buf.getvalue()


class pythonParser ( Parser ):

    grammarFileName = "python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'='", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "NUMBER", "LETTER", "STRING", "DIGIT", "LOWER", 
                      "UPPER", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_expression = 1
    RULE_variableExpression = 2

    ruleNames =  [ "prog", "expression", "variableExpression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    NUMBER=5
    LETTER=6
    STRING=7
    DIGIT=8
    LOWER=9
    UPPER=10
    WS=11
    COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pythonParser.ExpressionContext,i)


        def getRuleIndex(self):
            return pythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = pythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pythonParser.VAR:
                self.state = 6
                self.expression()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def variableExpression(self):
            return self.getTypedRuleContext(pythonParser.VariableExpressionContext,0)


        def getRuleIndex(self):
            return pythonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = pythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.variableExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonParser.VAR)
            else:
                return self.getToken(pythonParser.VAR, i)

        def STRING(self):
            return self.getToken(pythonParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(pythonParser.NUMBER, 0)

        def getRuleIndex(self):
            return pythonParser.RULE_variableExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpression" ):
                listener.enterVariableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpression" ):
                listener.exitVariableExpression(self)




    def variableExpression(self):

        localctx = pythonParser.VariableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(pythonParser.VAR)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.T__0:
                self.state = 15
                self.match(pythonParser.T__0)


            self.state = 18
            self.match(pythonParser.T__1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.T__0:
                self.state = 19
                self.match(pythonParser.T__0)


            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pythonParser.T__2]:
                self.state = 22
                self.match(pythonParser.T__2)
                self.state = 23
                self.match(pythonParser.STRING)
                self.state = 24
                self.match(pythonParser.T__2)
                pass
            elif token in [pythonParser.NUMBER]:
                self.state = 25
                self.match(pythonParser.NUMBER)
                pass
            elif token in [pythonParser.VAR]:
                self.state = 26
                self.match(pythonParser.VAR)
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





