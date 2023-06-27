grammar gn;

program: (group | statement)+ ;

group: 'group' ID '(' parameters? ')' block ;

parameters: parameter (',' parameter)* ;

parameter: type ID | type ID '=' value ;

type : 'float' | 'coll' | 'str' | 'vec' | 'img' | 'geo' | 'obj' | 'bool' | 'int' | 'tex' | 'virtual' | 'mat' | 'col' ;

value : BOOLEAN | STRING | NUMBER;

block : '{' statement* 'return' exprList? ';' '}' ; 

statement: expr '=' expr ';' | expr ';' ;

expr: ID '(' exprList? ')'  // func call
    | op='-' a=expr // unary minus
    | op='!' a=expr // boolean not
    | a=expr op=('*' | '/') b=expr
    | a=expr op=('+' | '-') b=expr
    | a=expr op='==' b=expr // equality comparison (lowest priority op)
    | ID // variable reference
    | value
    | '(' expr ')'
    ;

exprList : (ID '=')? expr (',' (ID '=')? expr)*; // arg list

BOOLEAN : 'true' | 'false' ;

STRING : '"' (ESC | ~["\\])* '"' ;

fragment ESC : '\\' (["\\/bfnrt] | UNICODE) ;

fragment UNICODE : 'u' HEX HEX HEX HEX ;

fragment HEX : [0-9a-fA-F] ;

ID : ID_LETTER (ID_LETTER | DIGIT)* ; // From C language

fragment ID_LETTER : 'a'..'z'|'A'..'Z'|'_' ;

fragment DIGIT : '0'..'9' ;

NUMBER
    : '-'? INT '.' INT EXP? // 1.35, 1.35E-9, 0.3, -4.5
    | '-'? INT EXP // 1e10 -3e4
    | '-'? INT // -3, 45
    ;
fragment INT : '0' | [1-9] [0-9]* ; // no leading zeros

fragment EXP : [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

LINE_COMMENT : '#' .*? '\r'? '\n' -> skip ; // Match "#" stuff '\n'

WS : [ \t\n\r]+ -> skip ;
