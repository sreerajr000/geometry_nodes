grammar Expression;

// parser rules
program: statement* EOF;
statement: assignment | binaryExp;
assignment: ID ASSIGN binaryExp;

binaryExp
    : additiveExp
    ;

additiveExp
    : multiplicativeExp ((PLUS | MINUS) multiplicativeExp)*
    ;

multiplicativeExp
    : unaryExp ((TIMES | DIV) unaryExp)*
    ;

unaryExp
    : unaryOp LPAREN binaryExp RPAREN
    | binaryOp LPAREN binaryExp COMMA binaryExp RPAREN
    | factor
    ;

factor
    : NUMBER
    | ID
    | LPAREN binaryExp RPAREN
    ;

unaryOp : SIN | COS | TAN | ASIN | ACOS | ATAN | ABS | FLOOR | CEIL | FRACT | INVERSE | SIGN | EXP | RAD | DEG;

binaryOp : POW | LOG | MIN | MAX | ROUND | LT | GT | MOD | SQRT ;

// lexer rules
ID: [a-zA-Z]+ ;              // match identifiers
NUMBER: [0-9]+ ('.' [0-9]+)? ;   // match integers or decimals

ASSIGN: '=' ;                // match '=' symbol
PLUS  : '+' ;                // match '+' symbol
MINUS : '-' ;                // match '-' symbol
TIMES : '*' ;                // match '*' symbol
DIV   : '/' ;                // match '/' symbol

LPAREN: '(' ;                // match '(' symbol
RPAREN: ')' ;                // match ')' symbol
COMMA: ',' ;                 // match ',' symbol

SIN : 'sin' ;
COS : 'cos' ;
TAN : 'tan' ;
ASIN : 'asin' ;
ACOS : 'acos' ;
ATAN : 'atan' ;
ABS : 'abs' ;
FLOOR : 'floor' ;
CEIL : 'ceil' ;
FRACT : 'fract' ;
INVERSE : 'inverse' ;
SIGN : 'sign' ;
EXP : 'exp' ;
RAD : 'rad' ;
DEG : 'deg' ;

POW : 'pow' ;
LOG : 'log' ;
MIN : 'min' ;
MAX : 'max' ;
ROUND : 'round' ;
LT : 'lt' ;
GT : 'gt' ;
MOD : 'mod' ;
SQRT : 'sqrt' ;

WS    : [ \t\n\r]+ -> skip ; // skip spaces, tabs, newlines
