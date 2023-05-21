from EscreveLexer import EscreveLexer
import ply.yacc as pyacc


class EscreveGrammar:
    precedence = (
        ( 'right', '=' ),
        ( 'left' , '+', '-'), # level=1, assoc=left
         ("left", '*'),      # level=2, assoc=left 
         )
    # guardar as atribuições de variáveis
    symbols = {}

    @staticmethod
    def initSymbols():
        pass
        EscreveGrammar.symbols.clear()


    def build(self, **kwargs):
        self.lexer = EscreveLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_initial(self, p):
        """ initial : comando
                    | assign
                    | declare_var"""

    def p_comando_escreve(self, p):
        """ comando : ESCREVE lista_strings FIM"""
        for t in p[2]:
            print(t)

    

    def p_lista_strings_multiple(self,p):
        """lista_strings : lista_strings SEPARADOR E
                         | lista_strings SEPARADOR NUM
                         | lista_strings SEPARADOR STRING"""

        p[0] = p[1] + [p[3]]

    def p_expr_op(self, p):
        """ E : E '+' E  
                | E '-' E 
                | E '*' E """       
        if p[2] == '+':
            p[0] = int(p[1]) + int(p[3])
        elif p[2] == '-': 
            p[0] = p[1] - p[3] 
        elif p[2] == '*': 
            p[0] = p[1] * p[3]
        else: 
            print(f"operador '{p[2]}' desconhecido ") # análise léxica garante que não acontecerá
        print(p[0])

    def p_lista_strings_single(self,p):
        """lista_strings : STRING
                         | NUM
                         | E"""
        p[0] = [p[1]]

    def p_expr_num(self, p):      
            """ E :  NUM  """
            p[0] = p[1] 

    #ASSIGN 
    def p_create_var(self, p):
        """ declare_var : VAR VARID FIM"""
        EscreveGrammar.symbols[ p[2] ]=None    
        print(f"info: variável '{p[2]}' declarada")

    def p_assign_var(self, p):
        """ assign : VAR VARID '=' E FIM"""
        EscreveGrammar.symbols[ p[2] ]= p[4]    
        print(f"info: variável '{p[2]}' fica com o valor {p[4]}")
        p[0]=dict(op='assign',args= [ p[2] , p[4]] )
    #FIM ASSIGN

    def p_error(self,p):
        if p:
            print(f"Erro de sintaxe no token: {p.value}")
        else:
            print("Erro de sintaxe no final da entrada")