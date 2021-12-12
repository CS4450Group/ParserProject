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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\5\3\31\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\4\5\4%\n\4")
        buf.write("\3\5\3\5\3\5\5\5*\n\5\3\5\5\5-\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\3\6\3\6\3")
        buf.write("\6\5\6A\n\6\3\7\3\7\6\7E\n\7\r\7\16\7F\3\7\3\7\3\7\2\2")
        buf.write("\b\2\4\6\b\n\f\2\4\3\2\6\n\3\2\17\20\2N\2\21\3\2\2\2\4")
        buf.write("\30\3\2\2\2\6\32\3\2\2\2\b&\3\2\2\2\n.\3\2\2\2\fB\3\2")
        buf.write("\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3")
        buf.write("\2\2\2\21\22\3\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\25")
        buf.write("\7\2\2\3\25\3\3\2\2\2\26\31\5\6\4\2\27\31\5\n\6\2\30\26")
        buf.write("\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\7\17\2\2\33")
        buf.write("!\7\3\2\2\34\35\7\4\2\2\35\36\7\22\2\2\36\"\7\4\2\2\37")
        buf.write("\"\7\20\2\2 \"\7\17\2\2!\34\3\2\2\2!\37\3\2\2\2! \3\2")
        buf.write("\2\2\"$\3\2\2\2#%\7\27\2\2$#\3\2\2\2$%\3\2\2\2%\7\3\2")
        buf.write("\2\2&)\7\17\2\2\'*\7\5\2\2(*\t\2\2\2)\'\3\2\2\2)(\3\2")
        buf.write("\2\2*,\3\2\2\2+-\t\3\2\2,+\3\2\2\2,-\3\2\2\2-\t\3\2\2")
        buf.write("\2./\7\13\2\2/\60\5\b\5\2\60\61\7\f\2\2\61\62\5\f\7\2")
        buf.write("\62:\3\2\2\2\63\64\7\r\2\2\64\65\5\b\5\2\65\66\7\f\2\2")
        buf.write("\66\67\5\f\7\2\679\3\2\2\28\63\3\2\2\29<\3\2\2\2:8\3\2")
        buf.write("\2\2:;\3\2\2\2;@\3\2\2\2<:\3\2\2\2=>\7\16\2\2>?\7\f\2")
        buf.write("\2?A\5\f\7\2@=\3\2\2\2@A\3\2\2\2A\13\3\2\2\2BD\7\31\2")
        buf.write("\2CE\5\4\3\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G")
        buf.write("H\3\2\2\2HI\7\32\2\2I\r\3\2\2\2\13\21\30!$),:@F")
        return buf.getvalue()


class pythonParser ( Parser ):

    grammarFileName = "python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'\"'", "'!'", "'<='", "'<'", "'=='", 
                     "'>'", "'>='", "'if'", "':'", "'else if'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUMBER", "LETTER", "STRING", 
                      "DIGIT", "LOWER", "UPPER", "COMMENT", "NL", "WS", 
                      "INDENT", "DEDENT" ]

    RULE_prog = 0
    RULE_expression = 1
    RULE_variableExpression = 2
    RULE_evaluatorExpression = 3
    RULE_ifExpression = 4
    RULE_block = 5

    ruleNames =  [ "prog", "expression", "variableExpression", "evaluatorExpression", 
                   "ifExpression", "block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    VAR=13
    NUMBER=14
    LETTER=15
    STRING=16
    DIGIT=17
    LOWER=18
    UPPER=19
    COMMENT=20
    NL=21
    WS=22
    INDENT=23
    DEDENT=24

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

        def EOF(self):
            return self.getToken(pythonParser.EOF, 0)

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pythonParser.T__8 or _la==pythonParser.VAR:
                self.state = 12
                self.expression()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(pythonParser.EOF)
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


        def ifExpression(self):
            return self.getTypedRuleContext(pythonParser.IfExpressionContext,0)


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
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pythonParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.variableExpression()
                pass
            elif token in [pythonParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.ifExpression()
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

        def NL(self):
            return self.getToken(pythonParser.NL, 0)

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
            self.state = 24
            self.match(pythonParser.VAR)
            self.state = 25
            self.match(pythonParser.T__0)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pythonParser.T__1]:
                self.state = 26
                self.match(pythonParser.T__1)
                self.state = 27
                self.match(pythonParser.STRING)
                self.state = 28
                self.match(pythonParser.T__1)
                pass
            elif token in [pythonParser.NUMBER]:
                self.state = 29
                self.match(pythonParser.NUMBER)
                pass
            elif token in [pythonParser.VAR]:
                self.state = 30
                self.match(pythonParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.NL:
                self.state = 33
                self.match(pythonParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluatorExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonParser.VAR)
            else:
                return self.getToken(pythonParser.VAR, i)

        def NUMBER(self):
            return self.getToken(pythonParser.NUMBER, 0)

        def getRuleIndex(self):
            return pythonParser.RULE_evaluatorExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluatorExpression" ):
                listener.enterEvaluatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluatorExpression" ):
                listener.exitEvaluatorExpression(self)




    def evaluatorExpression(self):

        localctx = pythonParser.EvaluatorExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_evaluatorExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(pythonParser.VAR)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pythonParser.T__2]:
                self.state = 37
                self.match(pythonParser.T__2)
                pass
            elif token in [pythonParser.T__3, pythonParser.T__4, pythonParser.T__5, pythonParser.T__6, pythonParser.T__7]:
                self.state = 38
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pythonParser.T__3) | (1 << pythonParser.T__4) | (1 << pythonParser.T__5) | (1 << pythonParser.T__6) | (1 << pythonParser.T__7))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.VAR or _la==pythonParser.NUMBER:
                self.state = 41
                _la = self._input.LA(1)
                if not(_la==pythonParser.VAR or _la==pythonParser.NUMBER):
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


    class IfExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evaluatorExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonParser.EvaluatorExpressionContext)
            else:
                return self.getTypedRuleContext(pythonParser.EvaluatorExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonParser.BlockContext)
            else:
                return self.getTypedRuleContext(pythonParser.BlockContext,i)


        def getRuleIndex(self):
            return pythonParser.RULE_ifExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpression" ):
                listener.enterIfExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpression" ):
                listener.exitIfExpression(self)




    def ifExpression(self):

        localctx = pythonParser.IfExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(pythonParser.T__8)
            self.state = 45
            self.evaluatorExpression()
            self.state = 46
            self.match(pythonParser.T__9)
            self.state = 47
            self.block()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pythonParser.T__10:
                self.state = 49
                self.match(pythonParser.T__10)
                self.state = 50
                self.evaluatorExpression()
                self.state = 51
                self.match(pythonParser.T__9)
                self.state = 52
                self.block()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pythonParser.T__11:
                self.state = 59
                self.match(pythonParser.T__11)
                self.state = 60
                self.match(pythonParser.T__9)
                self.state = 61
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(pythonParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(pythonParser.DEDENT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pythonParser.ExpressionContext,i)


        def getRuleIndex(self):
            return pythonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = pythonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(pythonParser.INDENT)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.expression()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==pythonParser.T__8 or _la==pythonParser.VAR):
                    break

            self.state = 70
            self.match(pythonParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





