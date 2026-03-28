
TOKENS_SIMPLES = {'-', ')', '+', '(', ';', '/', '*', '='}

class Scanner:
    def __init__(self, line: str):
        self.line = line
        self.pos = 0

    def _skip_whitespace(self):
        while self.pos < len(self.line) and self.line[self.pos] == ' ':
            self.pos += 1

    def next_token(self) -> tuple:
        self._skip_whitespace()
        if self.pos >= len(self.line):
            return (None, None)

        c = self.line[self.pos]

        if c in TOKENS_SIMPLES:
            token = c
            self.pos += 1
            return (c, c)

        if c.islower():
            start = self.pos
            while self.pos < len(self.line) and self.line[self.pos].islower():
                self.pos += 1
            return ('identificador', self.line[start:self.pos])

        if c.isdigit():
            start = self.pos
            while self.pos < len(self.line) and self.line[self.pos].isdigit():
                self.pos += 1
            return ('cte_ent', self.line[start:self.pos])

        return ("Error", "Error léxico en posición " + str(self.pos))