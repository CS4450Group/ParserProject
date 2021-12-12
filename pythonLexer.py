# Generated from python.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5$\n\5\3\5\5\5\'\n\5\3")
        buf.write("\6\5\6*\n\6\3\6\6\6-\n\6\r\6\16\6.\3\7\3\7\5\7\63\n\7")
        buf.write("\3\b\3\b\6\b\67\n\b\r\b\16\b8\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\6\fB\n\f\r\f\16\fC\3\f\3\f\3\r\3\r\7\rJ\n\r\f\r\16")
        buf.write("\rM\13\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\3\2\6\3\2\62;\3\2c|\3\2C\\")
        buf.write("\5\2\13\f\17\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t#")
        buf.write("\3\2\2\2\13)\3\2\2\2\r\62\3\2\2\2\17\66\3\2\2\2\21:\3")
        buf.write("\2\2\2\23<\3\2\2\2\25>\3\2\2\2\27A\3\2\2\2\31G\3\2\2\2")
        buf.write("\33\34\7\"\2\2\34\4\3\2\2\2\35\36\7?\2\2\36\6\3\2\2\2")
        buf.write("\37 \7$\2\2 \b\3\2\2\2!$\5\r\7\2\"$\7a\2\2#!\3\2\2\2#")
        buf.write("\"\3\2\2\2$&\3\2\2\2%\'\5\17\b\2&%\3\2\2\2&\'\3\2\2\2")
        buf.write("\'\n\3\2\2\2(*\7/\2\2)(\3\2\2\2)*\3\2\2\2*,\3\2\2\2+-")
        buf.write("\5\21\t\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\f\3")
        buf.write("\2\2\2\60\63\5\23\n\2\61\63\5\25\13\2\62\60\3\2\2\2\62")
        buf.write("\61\3\2\2\2\63\16\3\2\2\2\64\67\5\r\7\2\65\67\5\21\t\2")
        buf.write("\66\64\3\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\28")
        buf.write("9\3\2\2\29\20\3\2\2\2:;\t\2\2\2;\22\3\2\2\2<=\t\3\2\2")
        buf.write("=\24\3\2\2\2>?\t\4\2\2?\26\3\2\2\2@B\t\5\2\2A@\3\2\2\2")
        buf.write("BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\f\2\2F\30")
        buf.write("\3\2\2\2GK\7%\2\2HJ\13\2\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2")
        buf.write("\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NO\b\r\2\2O\32\3\2\2")
        buf.write("\2\f\2#&).\62\668CK\3\b\2\2")
        return buf.getvalue()


class pythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    VAR = 4
    NUMBER = 5
    LETTER = 6
    STRING = 7
    DIGIT = 8
    LOWER = 9
    UPPER = 10
    WS = 11
    COMMENT = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'='", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUMBER", "LETTER", "STRING", "DIGIT", "LOWER", "UPPER", 
            "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "VAR", "NUMBER", "LETTER", "STRING", 
                  "DIGIT", "LOWER", "UPPER", "WS", "COMMENT" ]

    grammarFileName = "python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


