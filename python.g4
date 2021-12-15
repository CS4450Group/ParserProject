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

expression: variableExpression | ifExpression | whileExpression | forExpression | printStatement; // added while and for loops

variableExpression: VAR ASSIGN (STRING | ARITHMETIC | NUMBER | VAR) NL?; //changed '=' to all assignment operators

//evaluatorExpressions now allow consecutive expressions seperated by logic operators 
evaluatorExpression: (VAR | NUMBER | ARITHMETIC)('!' | ('<=' | '<' | '==' | '>' | '>=' | '!='))(VAR | NUMBER | ARITHMETIC) (('and' | 'or' | 'not')(VAR | NUMBER | ARITHMETIC)('!' | ('<=' | '<' | '==' | '>' | '>='))(VAR | NUMBER | ARITHMETIC))*; //ARITHMETIC added

ifExpression: ('if' '('? evaluatorExpression ')'? ':' block) ('elif' '('? evaluatorExpression ')'? ':' block)* ('else' ':' block)?;

whileExpression: ('while' evaluatorExpression ':' block); //while loops added

//for loops, only works for looping through an already assigned variable for the time being. Iterable data types still need to be added / fixed. (strings don't seem to work.)
forExpression: ('for' VAR 'in' (VAR | iterable) ':' block); 

printStatement: ('print(' (STRING | VAR | NUMBER | ARITHMETIC | STRADD) ')') NL?;

iterable: ('range(' ((NUMBER | VAR | ARITHMETIC) | (NUMBER | VAR | ARITHMETIC) ',' (NUMBER | VAR | ARITHMETIC)) ')'); //iterables, not sure if we need to support others besides range

block: INDENT (((expression)+ 'break'?) | 'break') NL? DEDENT?; // added a ? to allow blocks at the end of the file

VAR: (LETTER | '_') (LETTER | '_' | DIGIT)*; //changed from VAR: (LETTER | '_') STRING?; to allow _ seperated words

NUMBER: (('-'? DIGIT+) | INT); //should support the int() function

LETTER: (LOWER | UPPER);

STRING: (('"'~('\n' | '\r')*'"') | STR); //strings should support all characters and the str() function

ARITHMETIC: (NUMBER | VAR) ' '? OP ' '? (NUMBER | VAR) (' '? OP ' '? (NUMBER | VAR))*;  //ARITHMETIC works for all operators +,-,*,/,^,%, for some reason ' '? is required or will match number instead

STR: ('str(' VAR ')');

INT: ('int(' (VAR | ARITHMETIC) ')');

STRADD: (((STRING | VAR) '+' (STRING | VAR)));

DIGIT: [0-9]+;

LOWER: [a-z];

UPPER: [A-Z];

// CHAR: ~('\n' | '\r'); //this is broken for some reason? works alone in string and comment

COMMENT: '#' ~('\n' | '\r')* ->skip;

OP: ('+' | '-' | '*' | '/' | '%' | '^'); //operators for ARITHMETIC
ASSIGN: ('=' | '+=' | '-=' | '*=' | '/=' | '^=' | '%='); //operators for assignment

NL: ('\r'? '\n' ' '*);

WS: [ \t] + -> skip;