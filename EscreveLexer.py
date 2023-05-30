import ply.lex as plex


class EscreveLexer:
    tokens = ("ESCREVE", "STRING", "FIM",
              "NUM", "VAR", "VARID", 
              "PARA", "EM", "FAZER", "FIMPARA", "RANGE",
              "FUNC", "RETURN" , "FIMFUNC")
    literals = ['*', '+', '(', ')', '-', ',', ';', '=']
    t_ignore = ' \t\n'  # Ignora espaços em branco e quebras de linha

    def t_RETURN(self,t):
        r'RETURN'
        return t

    def t_FUNC(self,t):
        r'FUNC'
        return t

    def t_FIMFUNC(self,t):
        r'FIMFUNC'
        return t

    def t_PARA(self,t):
        r'PARA'
        return t
    
    def t_EM(self,t):
        r'EM'
        return t
    
    def t_RANGE(self,t):
        r'\[[0-9]+\.\.[0-9]+\]'
        return t
    
    def t_FAZER(self,t):
        r'FAZER'
        return t
    
    def t_FIMPARA(self,t):
        r'FIMPARA'
        return t
    
    def __init__(self):
        self.lexer = None

    def t_ESCREVE(self, t):
        r'ESCREVE'
        return t

    def t_VAR(self, t):
        r'VAR'
        return t

    def t_VARID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_STRING(self, t):
        r'"[^"]+"'
        t.value = t.value[1:-1]  # Remove as aspas duplas do valor
        return t

    def t_NUM(self, t):
        r'[0-9]+'
        t.value = int (t.value)
        return t

    def t_FIM(self, t):
        r';'
        return t
        
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type  # num, None

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
