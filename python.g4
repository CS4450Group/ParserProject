grammar python;

expression
   : commentExpression | variableExpression
   ;

commentExpression
   : COMMENT STRING
   ;

variableExpression
   :  VAR ' '? '=' ' '? '"' STRING '"' | number | VAR
   ;

number
   : '-'? DIGIT + 
   ;

DIGIT
   : ('0' .. '9')
   ;

WS
   : [ \r\n\t] + -> channel (HIDDEN)
   ;

COMMENT
   : '#'
   ;

STRING
   : .*
   ;

LETTER
   : ('A' .. 'Z') | ('a' .. 'z')
   ;

VAR
   : LETTER|'_'(STRING)
   ;