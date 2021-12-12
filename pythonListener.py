# Generated from python.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pythonParser import pythonParser
else:
    from pythonParser import pythonParser

# This class defines a complete listener for a parse tree produced by pythonParser.
class pythonListener(ParseTreeListener):

    # Enter a parse tree produced by pythonParser#prog.
    def enterProg(self, ctx:pythonParser.ProgContext):
        pass

    # Exit a parse tree produced by pythonParser#prog.
    def exitProg(self, ctx:pythonParser.ProgContext):
        pass


    # Enter a parse tree produced by pythonParser#expression.
    def enterExpression(self, ctx:pythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#expression.
    def exitExpression(self, ctx:pythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#variableExpression.
    def enterVariableExpression(self, ctx:pythonParser.VariableExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#variableExpression.
    def exitVariableExpression(self, ctx:pythonParser.VariableExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#evaluatorExpression.
    def enterEvaluatorExpression(self, ctx:pythonParser.EvaluatorExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#evaluatorExpression.
    def exitEvaluatorExpression(self, ctx:pythonParser.EvaluatorExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#ifExpression.
    def enterIfExpression(self, ctx:pythonParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#ifExpression.
    def exitIfExpression(self, ctx:pythonParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#block.
    def enterBlock(self, ctx:pythonParser.BlockContext):
        pass

    # Exit a parse tree produced by pythonParser#block.
    def exitBlock(self, ctx:pythonParser.BlockContext):
        pass



del pythonParser