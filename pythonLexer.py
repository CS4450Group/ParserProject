# Generated from python.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from pythonParser import pythonParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\"")
        buf.write("\u00de\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\5\26\u008b\n\26\3\26\3\26\3")
        buf.write("\26\7\26\u0090\n\26\f\26\16\26\u0093\13\26\3\27\5\27\u0096")
        buf.write("\n\27\3\27\6\27\u0099\n\27\r\27\16\27\u009a\3\30\3\30")
        buf.write("\5\30\u009f\n\30\3\31\3\31\3\31\5\31\u00a4\n\31\3\31\6")
        buf.write("\31\u00a7\n\31\r\31\16\31\u00a8\3\32\6\32\u00ac\n\32\r")
        buf.write("\32\16\32\u00ad\3\33\3\33\3\34\3\34\3\35\3\35\7\35\u00b6")
        buf.write("\n\35\f\35\16\35\u00b9\13\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u00cc\n\37\3 \5 \u00cf\n \3 \3 \7 \u00d3\n")
        buf.write(" \f \16 \u00d6\13 \3!\6!\u00d9\n!\r!\16!\u00da\3!\3!\2")
        buf.write("\2\"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"\3\2\b\3\2")
        buf.write("\62;\3\2c|\3\2C\\\4\2\f\f\17\17\7\2\'\',-//\61\61``\4")
        buf.write("\2\13\13\"\"\2\u00f1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\3C\3\2\2\2\5E\3\2\2\2\7H")
        buf.write("\3\2\2\2\tJ\3\2\2\2\13M\3\2\2\2\rO\3\2\2\2\17R\3\2\2\2")
        buf.write("\21V\3\2\2\2\23Y\3\2\2\2\25]\3\2\2\2\27`\3\2\2\2\31b\3")
        buf.write("\2\2\2\33j\3\2\2\2\35o\3\2\2\2\37u\3\2\2\2!{\3\2\2\2#")
        buf.write("}\3\2\2\2%\177\3\2\2\2\'\u0081\3\2\2\2)\u0085\3\2\2\2")
        buf.write("+\u008a\3\2\2\2-\u0095\3\2\2\2/\u009e\3\2\2\2\61\u00a0")
        buf.write("\3\2\2\2\63\u00ab\3\2\2\2\65\u00af\3\2\2\2\67\u00b1\3")
        buf.write("\2\2\29\u00b3\3\2\2\2;\u00bc\3\2\2\2=\u00cb\3\2\2\2?\u00ce")
        buf.write("\3\2\2\2A\u00d8\3\2\2\2CD\7#\2\2D\4\3\2\2\2EF\7>\2\2F")
        buf.write("G\7?\2\2G\6\3\2\2\2HI\7>\2\2I\b\3\2\2\2JK\7?\2\2KL\7?")
        buf.write("\2\2L\n\3\2\2\2MN\7@\2\2N\f\3\2\2\2OP\7@\2\2PQ\7?\2\2")
        buf.write("Q\16\3\2\2\2RS\7c\2\2ST\7p\2\2TU\7f\2\2U\20\3\2\2\2VW")
        buf.write("\7q\2\2WX\7t\2\2X\22\3\2\2\2YZ\7p\2\2Z[\7q\2\2[\\\7v\2")
        buf.write("\2\\\24\3\2\2\2]^\7k\2\2^_\7h\2\2_\26\3\2\2\2`a\7<\2\2")
        buf.write("a\30\3\2\2\2bc\7g\2\2cd\7n\2\2de\7u\2\2ef\7g\2\2fg\7\"")
        buf.write("\2\2gh\7k\2\2hi\7h\2\2i\32\3\2\2\2jk\7g\2\2kl\7n\2\2l")
        buf.write("m\7u\2\2mn\7g\2\2n\34\3\2\2\2op\7y\2\2pq\7j\2\2qr\7k\2")
        buf.write("\2rs\7n\2\2st\7g\2\2t\36\3\2\2\2uv\7t\2\2vw\7c\2\2wx\7")
        buf.write("p\2\2xy\7i\2\2yz\7g\2\2z \3\2\2\2{|\7*\2\2|\"\3\2\2\2")
        buf.write("}~\7.\2\2~$\3\2\2\2\177\u0080\7+\2\2\u0080&\3\2\2\2\u0081")
        buf.write("\u0082\7h\2\2\u0082\u0083\7q\2\2\u0083\u0084\7t\2\2\u0084")
        buf.write("(\3\2\2\2\u0085\u0086\7k\2\2\u0086\u0087\7p\2\2\u0087")
        buf.write("*\3\2\2\2\u0088\u008b\5/\30\2\u0089\u008b\7a\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u0091\3\2\2\2")
        buf.write("\u008c\u0090\5/\30\2\u008d\u0090\7a\2\2\u008e\u0090\5")
        buf.write("\63\32\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092,\3\2\2\2\u0093\u0091\3\2\2")
        buf.write("\2\u0094\u0096\7/\2\2\u0095\u0094\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0099\5\63\32\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b.\3\2\2\2\u009c\u009f\5\65\33")
        buf.write("\2\u009d\u009f\5\67\34\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\60\3\2\2\2\u00a0\u00a3\7$\2\2\u00a1\u00a4")
        buf.write("\5/\30\2\u00a2\u00a4\5\63\32\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a7\7$\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\62\3\2\2\2\u00aa\u00ac")
        buf.write("\t\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\64\3\2\2\2\u00af")
        buf.write("\u00b0\t\3\2\2\u00b0\66\3\2\2\2\u00b1\u00b2\t\4\2\2\u00b2")
        buf.write("8\3\2\2\2\u00b3\u00b7\7%\2\2\u00b4\u00b6\n\5\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00ba\u00bb\b\35\2\2\u00bb:\3\2\2\2\u00bc\u00bd")
        buf.write("\t\6\2\2\u00bd<\3\2\2\2\u00be\u00cc\7?\2\2\u00bf\u00c0")
        buf.write("\7-\2\2\u00c0\u00cc\7?\2\2\u00c1\u00c2\7/\2\2\u00c2\u00cc")
        buf.write("\7?\2\2\u00c3\u00c4\7,\2\2\u00c4\u00cc\7?\2\2\u00c5\u00c6")
        buf.write("\7\61\2\2\u00c6\u00cc\7?\2\2\u00c7\u00c8\7`\2\2\u00c8")
        buf.write("\u00cc\7?\2\2\u00c9\u00ca\7\'\2\2\u00ca\u00cc\7?\2\2\u00cb")
        buf.write("\u00be\3\2\2\2\u00cb\u00bf\3\2\2\2\u00cb\u00c1\3\2\2\2")
        buf.write("\u00cb\u00c3\3\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c7\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cc>\3\2\2\2\u00cd\u00cf")
        buf.write("\7\17\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d4\7\f\2\2\u00d1\u00d3\7\"\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5@\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d7\u00d9\t\7\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\b!\2\2\u00ddB\3\2\2\2")
        buf.write("\21\2\u008a\u008f\u0091\u0095\u009a\u009e\u00a3\u00a8")
        buf.write("\u00ad\u00b7\u00cb\u00ce\u00d4\u00da\3\b\2\2")
        return buf.getvalue()


class pythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    VAR = 21
    NUMBER = 22
    LETTER = 23
    STRING = 24
    DIGIT = 25
    LOWER = 26
    UPPER = 27
    COMMENT = 28
    OP = 29
    ASSIGN = 30
    NL = 31
    WS = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'!'", "'<='", "'<'", "'=='", "'>'", "'>='", "'and'", "'or'", 
            "'not'", "'if'", "':'", "'else if'", "'else'", "'while'", "'range'", 
            "'('", "','", "')'", "'for'", "'in'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUMBER", "LETTER", "STRING", "DIGIT", "LOWER", "UPPER", 
            "COMMENT", "OP", "ASSIGN", "NL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "VAR", "NUMBER", "LETTER", "STRING", "DIGIT", "LOWER", 
                  "UPPER", "COMMENT", "OP", "ASSIGN", "NL", "WS" ]

    grammarFileName = "python.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: pythonLexer = lexer

        def pull_token(self):
            return super(pythonLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NL, pythonParser.INDENT, pythonParser.DEDENT, 1) 
        return self.denter.next_token()



