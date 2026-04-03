
TOKENS_SIMPLES = {'-', ')', '+', '(', ';', '/', '*', '='}

def skip_whitespace(line: str, pos: int) -> int:
    while pos < len(line) and line[pos] == ' ':
        pos += 1
    return pos

def scanner(line: str) -> list[tuple[str, str]]:
    """ Devuelve todos los tokens como una lista de tuplas (tipo, valor) """
    pos = 0
    tokens = []

    while pos < len(line):

        pos = skip_whitespace(line, pos)

        if pos >= len(line):
            tokens.append((None, None))
            return tokens

        c = line[pos]

        if c in TOKENS_SIMPLES:
            token = c
            pos += 1
            tokens.append((c, c))

        elif c.islower():
            start = pos
            while pos < len(line) and line[pos].islower():
                pos += 1
            tokens.append(('identificador', line[start:pos]))

        elif c.isdigit():
            start = pos
            while pos < len(line) and line[pos].isdigit():
                pos += 1
            tokens.append(('cte_ent', line[start:pos]))

        else:
            return ("Error", "Error léxico en posición " + str(pos))

    return tokens