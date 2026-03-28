TABLA = {
    # <Asignacion> ::= identificador = <Expresión> ;
    ('<Asignacion>', 'identificador'): 1,

    # <Expresion> ::= <Operando> <Resto_Expr>
    ('<Expresion>', 'identificador'): 2,
    ('<Expresion>', 'cte_ent'): 2,
    ('<Expresion>', '('): 2,
    ('<Expresion>', '-'): 2,

    # <Resto_Expr> ::= <Operador> <Operando> <Resto_Expr>
    ('<Resto_Expr>', '+'): 3,
    ('<Resto_Expr>', '-'): 3,
    ('<Resto_Expr>', '*'): 3,
    ('<Resto_Expr>', '/'): 3,
    # <Resto_Expr> ::= ε
    ('<Resto_Expr>', ';'): 4,
    ('<Resto_Expr>', ')'): 4,

    # <Operando> ::= - <Valor>
    ('<Operando>', '-'): 5,
    # <Operando> ::= <Valor>
    ('<Operando>', 'identificador'): 6,
    ('<Operando>', 'cte_ent') : 6,
    ('<Operando>', '('): 6,

    # <Valor> ::= identificador
    ('<Valor>', 'identificador'): 7,
    # <Valor> ::= cte_ent
    ('<Valor>', 'cte_ent'): 8,
    # <Valor> ::= ( <Expresion> )
    ('<Valor>', '('): 9,

    # <Operador> ::= + | - | * | /
    ('<Operador>', '+'): 10,
    ('<Operador>', '-'): 11,
    ('<Operador>', '*'): 12,
    ('<Operador>', '/'): 13,
}

PRODUCCIONES = {
    1:  [';', '<Expresion>', '=', 'identificador'],
    2:  ['<Resto_Expr>', '<Operando>'],
    3:  ['<Resto_Expr>', '<Operando>', '<Operador>'],
    4:  [],
    5:  ['<Valor>', '-'],
    6:  ['<Valor>'],
    7:  ['identificador'],
    8:  ['cte_ent'],
    9:  [')', '<Expresion>', '('],
    10: ['+'],
    11: ['-'],
    12: ['*'],
    13: ['/'],
}