grammar gn;

program: (group | statement)+ ;

group: 'GROUP' ID '(' parameters? ')' block ;

parameters: parameter (',' parameter)* ;

parameter: type ID | type ID '=' value ;

type : 'float' | 'coll' | 'str' | 'vec' | 'img' | 'geo' | 'obj' | 'bool' | 'int' | 'tex' | 'virtual' | 'mat' | 'col' ;

value : STRING | INT | FLOAT ;

block : '{' statement* '}' ; 

statement: block | 'return' expr? ';' | expr '=' expr ';' | expr ';' ;

expr: ID '(' exprList? ')' 
    | '-' expr // unary minus
    | '!' expr // boolean not
    | expr '*' expr
    | expr ('+'|'-') expr
    | expr '==' expr // equality comparison (lowest priority op)
    | ID // variable reference
    | INT
    | '(' expr ')'
    ;
    
exprList : expr (',' expr)* ; // arg list