import logging
from EscreveLexer import EscreveLexer
import ply.yacc as pyacc
import re

from tree_node import TreeNode


class EscreveGrammar:
    precedence = (
        ('right', '='),
        ('left', '+', '-'),  # level=1, assoc=left
        ("left", '*'),      # level=2, assoc=left
        ("right", 'simetrico'),
    )
    # guardar as atribuições de variáveis
    symbols = {}

    @staticmethod
    def initSymbols():
        EscreveGrammar.symbols.clear()

    def build(self, **kwargs):
        self.lexer = EscreveLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
    def p_init(self,p):
        """ init : block"""
        print('------')
        print(p[1])

    def p_init(self, p):
        """ init : block"""
        p[0]=p[1]
        #print(p[1])

    def p_block(self, p):
        """ block : block instruction """
        block_list: list = p[1].args
        block_list.append(p[2])
        p[0] = TreeNode(op='block', args=block_list)


    def p_block_end(self, p):
        """ block : instruction"""
        p[0] = TreeNode(op='instruction', args=[p[1]])

    def p_instruction(self, p):
        """ instruction : assign 
                        | declare_var
                        | print"""
        p[0] = TreeNode(op='instruction', args=[p[1]])

    def p_print(self, p):
        """ print : ESCREVE E FIM
                  | ESCREVE STRING FIM"""
        p[0] = TreeNode(op='print', args=[p[2]])

    # def p_initial(self, p):
    #     """ initial : escreve
    #                 | assign
    #                 | declare_var"""
    #     p[0] = p[1]

    # def p_comando_escreve(self, p):
    #     """ escreve : ESCREVE lista_strings FIM"""
    #     for t in p[2]:
    #         pass
    #         # print(t)

    def p_expr_op(self, p):
        """ E : E '+' E  
                | E '-' E 
                | E '*' E      """
        p[0]=TreeNode(op=p[2],args= [ p[1] , p[3]])

    def p_expr_sinalmenos(self, p):
        " E : '-' E   %prec simetrico "
        p[0] = TreeNode(op='-', args=[p[2]])

    def p_expr_pare(self, p):
        """ E : '(' E ')' """
        #    ^    ^  ^  ^
        #    0    1  2  3
        p[0] = p[2]

    def p_expr_num(self, p):
        """ E :  NUM  """
        p[0] = p[1]

    def p_expr_var(self, p):
        """ E :  VARID  """
        p[0]=TreeNode(op="var_lookup",args=[p[1]])
        # symbols { "E": 10 }
        # p[0] = ArithGrammar.symbols[ "E" ]

        # if p[1] in EscreveGrammar.symbols:
        #     p[0] = EscreveGrammar.symbols[p[1]]
        # else:
        #     print(EscreveGrammar.symbols)
        #     raise Exception(
        #         f"error: '{p[1]}' undeclared (first use in this function)")

    # def p_lista_strings_multiple(self, p):
    #     """lista_strings : lista_strings SEPARADOR E
    #                      | lista_strings SEPARADOR NUM
    #                      | lista_strings SEPARADOR STRING"""
    #     p[0] = p[1] + [p[3]]

    # def p_lista_strings_single(self, p):
    #     """lista_strings : STRING
    #                      | NUM
    #                      | E"""
    #    p[0] = [p[1]]

    def p_ciclos(self, p):
        """ instruction : PARA VARID EM RANGE FAZER block FIMPARA FIM """
        p[0]= TreeNode(op="for_loop",args=[p[2],p[4],p[6]])
       
        # pattern = r'\[(\d+)\.\.(\d+)\]'

        # # Aplica a expressão regular na string
        # matches = re.search(pattern, p[4])
        # if matches:
        #     # Obtém os dois inteiros encontrados
        #     inicio = int(matches.group(1))
        #     fim = int(matches.group(2))
        #     print(inicio, fim, p[6])
        # else:
        #     raise Exception(f"error: range invalid syntax")
        # EscreveGrammar.symbols[p[2]] = inicio

    # def p_inst_block(self, p):
    #     """ INST : INST initial """
    #     p[0] = p[1]

    # def p_inst_initial(self, p):
    #     """ INST : initial """
    #     p[0] = p[1]

    # def p_insts(self,p):
    #     """ INSTS : INSTS INST  """

    # def p_inst(self,p):
    #     """ INSTS : INST """

    # def p_inst_single(self,p):
    #     """ INST : initial """

    # ASSIGN

    def p_create_var(self, p):
        """ declare_var : VAR VARID FIM"""
        EscreveGrammar.symbols[p[2]] = None

    def p_assign_var(self, p):
        """ assign : VAR VARID '=' E FIM"""
        EscreveGrammar.symbols[p[2]] = p[4]
        p[0] = TreeNode(op='assign', args=[p[2], p[4]])
    # FIM ASSIGN

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
