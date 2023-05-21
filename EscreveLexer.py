import ply.lex as plex


class EscreveLexer:
    tokens= ("ESCREVE","STRING","FIM","SEPARADOR")
    t_ignore = ' \t\n'  # Ignora espaços em branco e quebras de linha
    
    def __init__(self):
        self.lexer = None

    def t_ESCREVE(self,t):
        r'ESCREVE'
        return t

    def t_STRING(self, t):
        r'"[^"]+"'
        t.value = t.value[1:-1]  # Remove as aspas duplas do valor
        return t
    
    def t_FIM(self,t):
        r';'
        return t
    
    def t_SEPARADOR(self,t):
        r','
        return t
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)
    
    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type # num, None

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)