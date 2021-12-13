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
            | ifExpression | whileExpression | forExpression; // added while and for loops

variableExpression: VAR ASSIGN ('"' STRING '"' | NUMBER | VAR | arithmetic) NL?; //changed '=' to all assignment operators

//evaluatorExpressions now allow consecutive expressions seperated by logic operators 
evaluatorExpression: VAR('!' | ('<=' | '<' | '==' | '>' | '>='))(VAR | NUMBER | arithmetic) (('and' | 'or' | 'not')VAR('!' | ('<=' | '<' | '==' | '>' | '>='))(VAR | NUMBER | arithmetic))*; //arithmetic added

ifExpression: ('if' evaluatorExpression ':' block) ('else if' evaluatorExpression ':' block)* ('else' ':' block)?;

whileExpression: ('while' evaluatorExpression ':' block); //while loops added

//for loops, only works for looping through an already assigned variable for the time being. Iterable data types still need to be added / fixed. (strings don't seem to work.)
forExpression: ('for' VAR 'in' (VAR) ':' block); 

arithmetic: (NUMBER | VAR) OP (NUMBER | VAR) (OP (NUMBER | VAR))*;  //arithmetic works for all operators +,-,*,/,^,%

block: INDENT (expression)+ DEDENT?; // added a ? to allow blocks at the end of the file

VAR: (LETTER | '_') (LETTER | '_' | DIGIT)*; //changed from VAR: (LETTER | '_') STRING?; to allow _ seperated words

NUMBER: '-'? DIGIT+;

LETTER: (LOWER|UPPER);

STRING: (LETTER|DIGIT)+;

DIGIT: [0-9]+;

LOWER: [a-z];

UPPER: [A-Z];

COMMENT: '#' ~('\n' | '\r')* ->skip;

OP: ('+' | '-' | '*' | '/' | '%' | '^'); //operators for arithmetic
ASSIGN: ('=' | '+=' | '-=' | '*=' | '/=' | '^=' | '%='); //operators for assignment

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
