from ArithLexer import ArithLexer
import ply.yacc as pyacc


class ArithGrammar:
    precedence = (
       # ( 'nonassoc', '>' ),
        ( 'left' , '+', '-'), # level=1, assoc=left
         ("left", '*'),      # level=2, assoc=left 
         )
    # guardar as atribuições de variáveis
    symbols = {}

    # métodos para lidar com 
    @staticmethod
    def initSymbols():
        ArithGrammar.symbols.clear()
    
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = ArithLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_expr_op(self, p):
        """ E : E '+' E  
              | E '-' E 
              | E '*' E """       
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-': 
            p[0] = p[1] - p[3] 
        elif p[2] == '*': 
            p[0] = p[1] * p[3]
        else: 
            print(f"operador '{p[2]}' desconhecido ") # análise léxica garante que não acontecerá
        print(p[0])

    def p_expr_num(self, p):      
            """ E :  num  """
            p[0] = p[1] 
    
    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
