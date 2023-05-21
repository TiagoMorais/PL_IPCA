from EscreveLexer import EscreveLexer
import ply.yacc as pyacc


class EscreveGrammar:
    

    @staticmethod
    def initSymbols():
        pass
        #EscreveGrammar.symbols.clear()


    def build(self, **kwargs):
        self.lexer = EscreveLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_comando_escreve(self, p):
        """ comando : ESCREVE lista_strings FIM"""
        for t in p[2]:
            print(t)

    def p_lista_strings_single(self,p):
        'lista_strings : STRING'
        p[0] = [p[1]]

    def p_lista_strings_multiple(self,p):
        'lista_strings : lista_strings SEPARADOR STRING'
        p[0] = p[1] + [p[3]]

    def p_error(p):
        if p:
            print(f"Erro de sintaxe no token: {p.value}")
        else:
            print("Erro de sintaxe no final da entrada")