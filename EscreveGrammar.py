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

    def p_init(self, p):
        """ init : block"""
        p[0] = p[1]
        # print(p[1])

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
                        | print
                        | function
                        | return
                        | func_call"""
        p[0] = TreeNode(op='instruction', args=[p[1]])

    def p_print(self, p):
        """ print : ESCREVE E FIM
                  | ESCREVE STRING FIM"""
        p[0] = TreeNode(op='print', args=[p[2]])

    def p_expr_op(self, p):
        """ E : E '+' E  
                | E '-' E 
                | E '*' E      """
        p[0] = TreeNode(op=p[2], args=[p[1], p[3]])

    def p_expr_sinalmenos(self, p):
        " E : '-' E   %prec simetrico "
        p[0] = TreeNode(op='-', args=[p[2]])

    def p_expr_pare(self, p):
        """ E : '(' E ')' """
        p[0] = p[2]

    def p_expr_num(self, p):
        """ E :  NUM  """
        p[0] = p[1]

    def p_expr_var(self, p):
        """ E :  VARID  """
        p[0] = TreeNode(op="var_lookup", args=[p[1]])

    def p_ciclos(self, p):
        """ instruction : PARA VARID EM RANGE FAZER block FIMPARA FIM """
        p[0] = TreeNode(op="for_loop", args=[p[2], p[4], p[6]])

    def p_create_var(self, p):
        """ declare_var : VAR VARID FIM"""
        EscreveGrammar.symbols[p[2]] = None

    def p_assign_var(self, p):
        """ assign : VAR VARID '=' E FIM"""
        EscreveGrammar.symbols[p[2]] = p[4]
        p[0] = TreeNode(op='assign', args=[p[2], p[4]])

    def p_return(self,p):
        """ return : RETURN E FIM"""
        p[0]= TreeNode(op='return', args=[p[2]])

    def p_func(self,p):
        """ function : FUNC VARID '(' params ')' block FIMFUNC"""
        p[0] = TreeNode(op='func', args=[p[2], p[4] ,p[6]])
    
    def p_params(self,p):
        """ params : params ','  VARID """
        params_list: list = p[1].args
        params_list.append(p[3])
        p[0] = TreeNode(op='param', args=params_list)  

    def p_param_end(self, p):
        """ params : VARID"""
        p[0] = TreeNode(op='param', args=[p[1]])

    def p_func_call(self,p):
        """ func_call : VARID '(' arguments ')' FIM """
        p[0] = TreeNode(op='func_call', args=[p[1],p[3]])

    def p_arguments(self,p):
        """ arguments : arguments ',' E  """
        arguments_list: list = p[1].args
        arguments_list.append(p[3])
        p[0] = TreeNode(op='arguments', args=arguments_list)  

    def p_arguments_end(self, p):
        """ arguments : E"""
        p[0] = TreeNode(op='arguments', args=[p[1]])

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1) 
