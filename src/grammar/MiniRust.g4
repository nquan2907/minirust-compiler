grammar MiniRust;

@lexer::header {
from utils.lexerror import *
}

@lexer::members {
def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_TOKEN:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

// ====================
// Parser Rules
// ====================

program: struct_expr* funcDecl* EOF;

typeExpr
    : I32
    | F32
    | BOOL
    | STRING
    | VOID
    | ID                            // struct type
    | arrayType                     // array type: [type, size]
    ;

arrayLiteral: LBRACK RBRACK | LBRACK array_list RBRACK;

array_list : expr COMMA array_list | expr;

arrayType : LBRACK typeExpr SEMI INT_LIT RBRACK;


funcDecl
    : FN ID LPAREN paramList RPAREN (ARROW typeExpr)? block
    ;

paramList
    : paramListPrime
    |
    ;

paramListPrime
    : param COMMA paramListPrime
    | param
    ;

param
    : ID COLON typeExpr
    ;

// BLOCK  VD : { x += 1 }
block: LBRACE statementList RBRACE;
statementList: statement statementList | ;

statement
    : callExpr SEMI
    | expr SEMI
    | vardecl
    | ifStmt
    | switchStmt
    | whileStmt
    | forStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | block 
    ;

callExpr: ID LPAREN argList RPAREN;

expr : assign_expr;

assign_expr
    : ID ASSIGN assign_expr
    | or_expr DOT ID ASSIGN assign_expr
    | or_expr LBRACK expr RBRACK ASSIGN assign_expr
    | or_expr
    ;

or_expr : or_expr OR and_expr | and_expr;

and_expr: and_expr AND eq_expr | eq_expr;

eq_expr: rel_expr | rel_expr EQ rel_expr | rel_expr NEQ rel_expr;

rel_expr: add_expr | add_expr LTE add_expr | add_expr GTE add_expr | add_expr GT add_expr | add_expr LT add_expr;

add_expr: add_expr ADD mul_expr | add_expr SUB mul_expr | mul_expr;

mul_expr: mul_expr MUL una_expr | mul_expr DIV una_expr | mul_expr MOD una_expr | una_expr;

una_expr: SUB una_expr | NOT una_expr | primary_expr;

primary_expr
            : primary_expr LBRACK expr RBRACK      // array indexing
            | primary_expr DOT ID                  // member access
            | ID LPAREN argList RPAREN             // function call trong expr: f(a,b)
            | LPAREN expr RPAREN
            | INT_LIT
            | FLOAT_LIT
            | STRING_LITERAL
            | TRUE
            | FALSE
            | ID
            | arrayLiteral
            | structLiteral
            ;

argList: argListprime | ;
argListprime: expr COMMA argListprime | expr;

// TẠO CẤU TRÚC STRUCT
struct_expr: STRUCT ID LBRACE fieldDeclList RBRACE;
fieldDeclList: fieldDec COMMA fieldDeclList | fieldDec;
fieldDec: ID COLON typeExpr;                                // tên file : kiểu dữ liệu

// GỌI CẤU TRÚC STRUCT
structLiteral: ID LBRACE initializerList RBRACE;
initializerList: initializerDec COMMA initializerList | initializerDec;
initializerDec: ID COLON expr;                               // tên file : dữ liệu

// VARIABLE DECLARATION
vardecl : LET ID COLON typeExpr ASSIGN expr SEMI           // let x: i32 = 100;
        | LET MUT ID COLON typeExpr ASSIGN expr SEMI       // let mut x: i32 = 100;
        | LET MUT ID ASSIGN expr SEMI                      // let mut count = 0;
        | LET MUT ID COLON typeExpr SEMI                   // let mut ratio: f32;
        | LET ID ASSIGN expr SEMI;                         // let msg = "Processing";

// STATEMENTS
    // IF - ELSE - ELSE IF
ifStmt: IF expr block elsePart | IF expr block;
elsePart: ELSE block | ELSE ifStmt;

    // SWITCH
switchStmt: SWITCH expr LBRACE switchBody  RBRACE;
switchBody
    : defaultClause caseClause+
    | caseClause+ defaultClause caseClause*
    | caseClause+
    ;

switchClause: caseClause;
caseClause: CASE literal COLON statementList;
defaultClause: DEFAULT COLON statementList;

literal: INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LITERAL;

    // WHILE
whileStmt: WHILE expr block;

    // FOR
forStmt: FOR ID IN expr DOTDOT expr block;

    // BREAK, CONTINUE
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;

    // RETURN
returnStmt: RETURN SEMI | RETURN expr SEMI;



// ====================
// Lexer Rules
// ====================

// KEYWORDS
FN       : 'fn';
LET      : 'let';
MUT      : 'mut';
STRUCT   : 'struct';
IF       : 'if';
ELSE     : 'else';
WHILE    : 'while';
FOR      : 'for';
IN       : 'in';
BREAK    : 'break';
CONTINUE : 'continue';
SWITCH   : 'switch';
CASE     : 'case';
DEFAULT  : 'default';
RETURN   : 'return';
I32      : 'i32';
F32      : 'f32';
BOOL     : 'bool';
VOID     : 'void';
STRING   : 'string';
TRUE     : 'true';
FALSE    : 'false';

LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
SEMI        : ';';
COMMA       : ',';
COLON       : ':';

DOTDOT   : '..';    // range operator
DOT      : '.';     // member access
MOD      : '%';     // modulo
ARROW    : '->';   

// OPERATORS
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

// COMPARISON
EQ          : '==';
NEQ         : '!=';
LTE         : '<=';
GTE         : '>=';
LT          : '<';
GT          : '>';

// Operators - logical
AND         : '&&';
OR          : '||';
NOT         : '!';

ASSIGN: '=';

// Literal
FLOAT_LIT
    : [0-9]+ '.' [0-9]+ ([Ee][+-]?[0-9]+)?   // 3.14, 3.14e5, 1.0E+3
    | [0-9]+             [Ee][+-]?[0-9]+      // 1e10, 2E+45, 134e8
    ;

INT_LIT : [0-9]+;

ID      : [a-zA-Z_][a-zA-Z0-9_]* | 'print_i32';
WS      : [ \t\r\n\f]+ -> skip;

// COMMENT, WHITE SPACE
COMMENT : '##' ~[\n]* -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' (~[*] | '*' ~[/])* '*/' -> skip;

// ERROR
fragment ESC_SEQ: '\\' [tn"\\];
fragment STR_CHAR   : ~["\\\r\n] | ESC_SEQ;
fragment ILLEGAL_ESC: '\\' ~[tn"\\];

UNCLOSE_STRING: '"' STR_CHAR* ('\\' ('\r' '\n'? | '\n' | EOF) | '\r' '\n'? | '\n' | EOF) {
    s = self.text[1:]
    s = s.rstrip('\r\n')
    raise UncloseString(s)
};

ILLEGAL_ESCAPE  : '"' STR_CHAR* ILLEGAL_ESC;
STRING_LITERAL : '"' STR_CHAR* '"' {
    s = self.text[1:-1]
    s = s.replace('\\\\', '\x00')
    s = s.replace('\\n', '\n')
    s = s.replace('\\t', '\t')
    s = s.replace('\\"', '"')
    s = s.replace('\x00', '\\')
    self.text = s
};

ERROR_TOKEN : . { raise ErrorToken(self.text) }; 