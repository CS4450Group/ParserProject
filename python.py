import sys
from antlr4 import *
from pythonLexer import pythonLexer
from pythonParser import pythonParser


def main(argv):
    if len(sys.argv) > 1:
        line = FileStream(sys.argv[1])
    else:
        line = InputStream(sys.stdin.readline())

    lexer = pythonLexer(line)
    tokens = CommonTokenStream(lexer)
    parser = pythonParser(tokens)
    tree = parser.expression()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
