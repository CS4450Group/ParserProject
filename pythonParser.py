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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\3\3\3\3\3\3\4\3\4\5\4\30\n\4\3\4\3\4")
        buf.write("\5\4\34\n\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\5\5\5&\n\5")
        buf.write("\3\5\6\5)\n\5\r\5\16\5*\3\5\2\2\6\2\4\6\b\2\2\2/\2\20")
        buf.write("\3\2\2\2\4\22\3\2\2\2\6\"\3\2\2\2\b%\3\2\2\2\n\13\5\4")
        buf.write("\3\2\13\f\7\b\2\2\f\21\3\2\2\2\r\16\5\6\4\2\16\17\7\b")
        buf.write("\2\2\17\21\3\2\2\2\20\n\3\2\2\2\20\r\3\2\2\2\21\3\3\2")
        buf.write("\2\2\22\23\7\t\2\2\23\24\7\n\2\2\24\5\3\2\2\2\25\27\7")
        buf.write("\f\2\2\26\30\7\3\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\33\7\4\2\2\32\34\7\3\2\2\33\32\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\35\3\2\2\2\35\36\7\5\2\2\36\37\7\n\2\2")
        buf.write("\37#\7\5\2\2 #\5\b\5\2!#\7\f\2\2\"\25\3\2\2\2\" \3\2\2")
        buf.write("\2\"!\3\2\2\2#\7\3\2\2\2$&\7\6\2\2%$\3\2\2\2%&\3\2\2\2")
        buf.write("&(\3\2\2\2\')\7\7\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*")
        buf.write("+\3\2\2\2+\t\3\2\2\2\b\20\27\33\"%*")
        return buf.getvalue()


class pythonParser ( Parser ):

    grammarFileName = "python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'='", "'\"'", "'-'", "<INVALID>", 
                     "<INVALID>", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DIGIT", "WS", "COMMENT", "STRING", "LETTER", 
                      "VAR" ]

    RULE_expression = 0
    RULE_commentExpression = 1
    RULE_variableExpression = 2
    RULE_number = 3

    ruleNames =  [ "expression", "commentExpression", "variableExpression", 
                   "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    DIGIT=5
    WS=6
    COMMENT=7
    STRING=8
    LETTER=9
    VAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentExpression(self):
            return self.getTypedRuleContext(pythonParser.CommentExpressionContext,0)


        def WS(self):
            return self.getToken(pythonParser.WS, 0)

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
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pythonParser.COMMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.commentExpression()
                self.state = 9
                self.match(pythonParser.WS)
                pass
            elif token in [pythonParser.T__3, pythonParser.DIGIT, pythonParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.variableExpression()
                self.state = 12
                self.match(pythonParser.WS)
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


    class CommentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(pythonParser.COMMENT, 0)

        def STRING(self):
            return self.getToken(pythonParser.STRING, 0)

        def getRuleIndex(self):
            return pythonParser.RULE_commentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentExpression" ):
                listener.enterCommentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentExpression" ):
                listener.exitCommentExpression(self)




    def commentExpression(self):

        localctx = pythonParser.CommentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commentExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(pythonParser.COMMENT)
            self.state = 17
            self.match(pythonParser.STRING)
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

        def VAR(self):
            return self.getToken(pythonParser.VAR, 0)

        def STRING(self):
            return self.getToken(pythonParser.STRING, 0)

        def number(self):
            return self.getTypedRuleContext(pythonParser.NumberContext,0)


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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(pythonParser.VAR)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pythonParser.T__0:
                    self.state = 20
                    self.match(pythonParser.T__0)


                self.state = 23
                self.match(pythonParser.T__1)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pythonParser.T__0:
                    self.state = 24
                    self.match(pythonParser.T__0)


                self.state = 27
                self.match(pythonParser.T__2)
                self.state = 28
                self.match(pythonParser.STRING)
                self.state = 29
                self.match(pythonParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(pythonParser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(pythonParser.DIGIT)
            else:
                return self.getToken(pythonParser.DIGIT, i)

        def getRuleIndex(self):
            return pythonParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = pythonParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.T__3:
                self.state = 34
                self.match(pythonParser.T__3)


            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.match(pythonParser.DIGIT)
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==pythonParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





