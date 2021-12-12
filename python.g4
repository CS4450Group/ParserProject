grammar python;

prog: (expression)*;

expression: variableExpression /* | otherexpressions */;

variableExpression: VAR ' '? '=' ' '? ('"' STRING '"' | NUMBER | VAR);

VAR: (LETTER | '_') STRING?;

NUMBER: '-'? DIGIT+;

LETTER: (LOWER|UPPER);

STRING: (LETTER|DIGIT)+;

DIGIT: [0-9];

LOWER: [a-z];

UPPER: [A-Z];

WS: [ \t\r\n] + -> skip;

COMMENT: '#'.* -> skip;

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