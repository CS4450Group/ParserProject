grammar python;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from pythonParser import pythonParser
}
@lexer::members {
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

}

prog: (expression)* EOF;

expression: variableExpression  
            | ifExpression | whileExpression;

variableExpression: VAR '=' ('"' STRING '"' | NUMBER | VAR | arithmetic) NL?;

evaluatorExpression: VAR('!' | ('<=' | '<' | '==' | '>' | '>=')) (VAR | NUMBER | arithmetic)?;

ifExpression: ('if' evaluatorExpression ':' block) ('else if' evaluatorExpression ':' block)* ('else' ':' block)?;

whileExpression: ('while' evaluatorExpression ':' block);

arithmetic: (NUMBER | VAR) OP (NUMBER | VAR);  

block: INDENT (expression)+ DEDENT?;

VAR: (LETTER | '_') STRING?;

NUMBER: '-'? DIGIT+;

LETTER: (LOWER|UPPER);

STRING: (LETTER|DIGIT)+;

DIGIT: [0-9]+;

LOWER: [a-z];

UPPER: [A-Z];

COMMENT: '#' ~('\n' | '\r')* ->skip;

OP: ('+' | '-' | '*' | '/' | '%' | '^');

NL: ('\r'? '\n' ' '*);

WS: [ \t] + -> skip;




// /*
//  * Parser Rules
//  */
// operation : addition | subtraction;
// subtraction : NUMBER '-' NUMBER;
// addition  : NUMBER '+' NUMBER ;
// var: LOWER;
// /*
//  * Lexer Rules
//  */
// NUMBER     : '-'? DIGIT+ ;
// fragment DIGIT: [0-9];
// LOWER: [a-z];
// fragment UPPER: [A-Z];
// WHITESPACE : [ \t\r\n] + -> skip ;
