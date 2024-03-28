# my bnf
```text
/*bnf grammar*/

expr				: KEYWORD:VAR IDENTIFIER EQ expr
						: comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*

comp-expr		: NOT comp-expr
						: arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

arith-expr	:	term ((PLUS|MINUS) term)*

term				: factor ((MUL|DIV) factor)*

factor			: (PLUS|MINUS) factor




atom 				: INT|FLOAT|IDENTIFIER
						: LPAREN expr RPAREN
						: if-expr
						: while-expr
/*q6*/
if-expr			: KEYWORD:IF expr KEYWORD:THEN expr



/*q7*/
while-expr	: KEYWORD:WHILE expr KEYWORD:THEN expr
