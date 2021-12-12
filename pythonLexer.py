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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u0090\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16W\n\16")
        buf.write("\3\16\5\16Z\n\16\3\17\5\17]\n\17\3\17\6\17`\n\17\r\17")
        buf.write("\16\17a\3\20\3\20\5\20f\n\20\3\21\3\21\6\21j\n\21\r\21")
        buf.write("\16\21k\3\22\6\22o\n\22\r\22\16\22p\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\7\25y\n\25\f\25\16\25|\13\25\3\25\3\25\3\26")
        buf.write("\5\26\u0081\n\26\3\26\3\26\7\26\u0085\n\26\f\26\16\26")
        buf.write("\u0088\13\26\3\27\6\27\u008b\n\27\r\27\16\27\u008c\3\27")
        buf.write("\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30\3\2\7\3\2\62;\3\2c|\3\2C\\\4\2\f\f\17\17\4\2")
        buf.write("\13\13\"\"\2\u009b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\3/\3\2\2\2\5\61\3\2\2\2\7\63\3\2\2\2\t")
        buf.write("\65\3\2\2\2\138\3\2\2\2\r:\3\2\2\2\17=\3\2\2\2\21?\3\2")
        buf.write("\2\2\23B\3\2\2\2\25E\3\2\2\2\27G\3\2\2\2\31O\3\2\2\2\33")
        buf.write("V\3\2\2\2\35\\\3\2\2\2\37e\3\2\2\2!i\3\2\2\2#n\3\2\2\2")
        buf.write("%r\3\2\2\2\'t\3\2\2\2)v\3\2\2\2+\u0080\3\2\2\2-\u008a")
        buf.write("\3\2\2\2/\60\7?\2\2\60\4\3\2\2\2\61\62\7$\2\2\62\6\3\2")
        buf.write("\2\2\63\64\7#\2\2\64\b\3\2\2\2\65\66\7>\2\2\66\67\7?\2")
        buf.write("\2\67\n\3\2\2\289\7>\2\29\f\3\2\2\2:;\7?\2\2;<\7?\2\2")
        buf.write("<\16\3\2\2\2=>\7@\2\2>\20\3\2\2\2?@\7@\2\2@A\7?\2\2A\22")
        buf.write("\3\2\2\2BC\7k\2\2CD\7h\2\2D\24\3\2\2\2EF\7<\2\2F\26\3")
        buf.write("\2\2\2GH\7g\2\2HI\7n\2\2IJ\7u\2\2JK\7g\2\2KL\7\"\2\2L")
        buf.write("M\7k\2\2MN\7h\2\2N\30\3\2\2\2OP\7g\2\2PQ\7n\2\2QR\7u\2")
        buf.write("\2RS\7g\2\2S\32\3\2\2\2TW\5\37\20\2UW\7a\2\2VT\3\2\2\2")
        buf.write("VU\3\2\2\2WY\3\2\2\2XZ\5!\21\2YX\3\2\2\2YZ\3\2\2\2Z\34")
        buf.write("\3\2\2\2[]\7/\2\2\\[\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^`\5")
        buf.write("#\22\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\36\3\2")
        buf.write("\2\2cf\5%\23\2df\5\'\24\2ec\3\2\2\2ed\3\2\2\2f \3\2\2")
        buf.write("\2gj\5\37\20\2hj\5#\22\2ig\3\2\2\2ih\3\2\2\2jk\3\2\2\2")
        buf.write("ki\3\2\2\2kl\3\2\2\2l\"\3\2\2\2mo\t\2\2\2nm\3\2\2\2op")
        buf.write("\3\2\2\2pn\3\2\2\2pq\3\2\2\2q$\3\2\2\2rs\t\3\2\2s&\3\2")
        buf.write("\2\2tu\t\4\2\2u(\3\2\2\2vz\7%\2\2wy\n\5\2\2xw\3\2\2\2")
        buf.write("y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}~\b")
        buf.write("\25\2\2~*\3\2\2\2\177\u0081\7\17\2\2\u0080\177\3\2\2\2")
        buf.write("\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0086\7")
        buf.write("\f\2\2\u0083\u0085\7\"\2\2\u0084\u0083\3\2\2\2\u0085\u0088")
        buf.write("\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write(",\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008b\t\6\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\b")
        buf.write("\27\2\2\u008f.\3\2\2\2\17\2VY\\aeikpz\u0080\u0086\u008c")
        buf.write("\3\b\2\2")
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
    VAR = 13
    NUMBER = 14
    LETTER = 15
    STRING = 16
    DIGIT = 17
    LOWER = 18
    UPPER = 19
    COMMENT = 20
    NL = 21
    WS = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'\"'", "'!'", "'<='", "'<'", "'=='", "'>'", "'>='", 
            "'if'", "':'", "'else if'", "'else'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUMBER", "LETTER", "STRING", "DIGIT", "LOWER", "UPPER", 
            "COMMENT", "NL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "VAR", "NUMBER", 
                  "LETTER", "STRING", "DIGIT", "LOWER", "UPPER", "COMMENT", 
                  "NL", "WS" ]

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



