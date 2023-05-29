# # arith.py
# from EscreveGrammar import EscreveGrammar

# ag = EscreveGrammar()
# ag.build()

# exemplos = [ # exemplos a avaliar de forma independente... 
#             # r'ESCREVE "ola", "mundo";',
#             # r'ESCREVE "ola", 1+1 ;',
#             # r'ESCREVE "ola", 1 ,"mundo";',
#             # r'VAR h ; ',
#             # r'VAR h = 1+5; ',
#             # r'VAR y = 10 * (h - 1) ; ',
#              r'VAR z = -1 ; ',
#             #r'PARA i EM [10..20] FAZER VAR x=3; VAR y=2; VAR z=4; VAR a=5; FIMPARA ;'
#             ]

# for frase in exemplos:
#     #EscreveGrammar.initSymbols()
#     print("\n")
    
#     #print(f"----------------------")
#     #print(f"--- frase '{frase}'")
#     res = ag.parse ( frase ) 
#     #print(f"resultado: {res}")


# arith.py
from EscreveGrammar import EscreveGrammar
from eval import Eval
import sys
from pprint import PrettyPrinter
pp = PrettyPrinter(sort_dicts=False)

lg = EscreveGrammar()
lg.build()


if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            ast_tree = lg.parse(contents)
            print("---")
            pp.pprint(ast_tree)
            print("---")
            Eval.evaluate(ast_tree)   
            print("--------------------") 
        except Exception as e:
            print(e, file=sys.stderr)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ast = lg.parse(expr)
            pp.pprint(ast)
            res = Eval.evaluate(ast)
            #if res is not None:
            print(f"<< {res}")
            
        except Exception as e:
            print(e)

