from config import TABLA, PRODUCCIONES
from Scanner import Scanner
from Stack import Stack

NO_TERMINALES = {'<Asignacion>', '<Expresion>', '<Resto_Expr>', '<Operando>', '<Valor>', '<Operador>'}

def parser(tokens: list) -> str:
    """
    Realiza un análisis léxico y sintáctico simultaneamente para evitar comprobaciones adicionales.
    Devuelve un mensaje de error o 'Correcto' si la línea es sintácticamente correcta.
    """

    pila = Stack()
    pila.push('<Asignacion>')

    token = tokens.pop(0)

    while not pila.empty():
        cima = pila.peek()

        if token[0] == 'Error':
            return token[1]

        if cima in NO_TERMINALES:
            if token[0] is None:
                return 'Error sintáctico: Final de línea inesperada'

            tipo = token[0]
            clave = (cima, tipo)

            if clave not in TABLA:
                return f'Error sintáctico en componente léxico {token[0]}'

            num_prod = TABLA[clave]
            pila.pop()

            for simbolo in PRODUCCIONES[num_prod]:
                pila.push(simbolo)

        else:
            if token[0] is None:
                print(f'Pila: {pila}, Token: {token}')
                return 'Error sintáctico: Final de línea inesperada'

            if cima != token[0]:
                return f'Error sintáctico en componente léxico {token[0]}'

            pila.pop()
            token = tokens.pop(0)

    # Pila vacia: comprobar que no quede contenido en la línea
    if token[0] is not None:
        return 'Error sintáctico: Contenido adicional al final de la línea'

    return 'Correcto'
