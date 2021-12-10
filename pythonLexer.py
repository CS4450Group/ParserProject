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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\6\7#\n\7\r\7\16\7$\3\7\3\7\3")
        buf.write("\b\3\b\3\t\7\t,\n\t\f\t\16\t/\13\t\3\n\5\n\62\n\n\3\13")
        buf.write("\3\13\3\13\5\13\67\n\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\3\2\4\5\2\13\f\17\17\"\"\4\2C\\")
        buf.write("c|\2:\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33")
        buf.write("\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2\2\r\"\3\2\2\2\17(\3")
        buf.write("\2\2\2\21-\3\2\2\2\23\61\3\2\2\2\25\66\3\2\2\2\27\30\7")
        buf.write("\"\2\2\30\4\3\2\2\2\31\32\7?\2\2\32\6\3\2\2\2\33\34\7")
        buf.write("$\2\2\34\b\3\2\2\2\35\36\7/\2\2\36\n\3\2\2\2\37 \4\62")
        buf.write(";\2 \f\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2")
        buf.write("\2$%\3\2\2\2%&\3\2\2\2&\'\b\7\2\2\'\16\3\2\2\2()\7%\2")
        buf.write("\2)\20\3\2\2\2*,\13\2\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2.\22\3\2\2\2/-\3\2\2\2\60\62\t\3\2\2\61\60")
        buf.write("\3\2\2\2\62\24\3\2\2\2\63\67\5\23\n\2\64\65\7a\2\2\65")
        buf.write("\67\5\21\t\2\66\63\3\2\2\2\66\64\3\2\2\2\67\26\3\2\2\2")
        buf.write("\7\2$-\61\66\3\2\3\2")
        return buf.getvalue()


class pythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    DIGIT = 5
    WS = 6
    COMMENT = 7
    STRING = 8
    LETTER = 9
    VAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'='", "'\"'", "'-'", "'#'" ]

    symbolicNames = [ "<INVALID>",
            "DIGIT", "WS", "COMMENT", "STRING", "LETTER", "VAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "DIGIT", "WS", "COMMENT", 
                  "STRING", "LETTER", "VAR" ]

    grammarFileName = "python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


