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

    # especificação da gramática :
    # def p_expr(self, p):
    #      E : E '+' E 
    #        | E '*' E    
    #        | '(' E ')' 
    #        |  num   """
      
    def p_expr_listvar(self, p):
        """ LstV :  LstV ';' V 
                 | V """
        print("--------------\n-- symbols: ")
        print(ArithGrammar.symbols )
        print("-------------- ")
            
    def p_expr_atrib(self,p):
        """ V : varid assign E """
        #""" V : varid assign E
        #      | varid assign num """   # conflito reduce/reduce
        # print(f"{p[3]}")
        #  E:=20 
        #            symbols["E"]=20         # { E: 20}
        #            symbols[ p[1] ]= p[3]
        ArithGrammar.symbols[ p[1] ]= p[3]    
        print(f"info: variável '{p[1]}' fica com o valor {p[3]}")
        p[0]=dict(op='assign',args= [ p[1] , p[3]] )
              
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
        #p[0]=dict(op='+',args= [ p[1] , p[3]] )
        # p[0]=dict(op=p[2],args= [ p[1] , p[3]] )
    
    #def p_expr_sub(self, p):
    #    """ E : E '-' E """   
    #    p[0] = p[1] - p[3]
           
    #def p_expr_mult(self, p):      
    #    """ E : E '*' E """
    #    #p[0] = p[1] + p[3]
    #    p[0] = p[1] * p[3]  
        
    def p_expr_sinalmenos(self, p): 
        " E : '-' E   %prec simetrico "
        p[0] = -p[2]
        
    def p_expr_pare(self, p):      
        """ E : '(' E ')' """
        #    ^    ^  ^  ^
        #    0    1  2  3 
        p[0]= p[2]
    
    def p_expr_num(self, p):      
        """ E :  num  """
        p[0]= p[1] 
    
    def p_expr_var(self, p):      
        """ E :  varid  """
        # symbols { "E": 10 }
        # p[0] = ArithGrammar.symbols[ "E" ]
        if p[1] in ArithGrammar.symbols:
            p[0]= ArithGrammar.symbols[ p[1] ] 
        else:
            raise Exception(f"error: '{p[1]}' undeclared (first use in this function)")
            
    
    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
