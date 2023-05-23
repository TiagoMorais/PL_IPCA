# arith.py
from EscreveGrammar import EscreveGrammar

ag = EscreveGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente... 
            # r'ESCREVE "ola", "mundo";',
            # r'ESCREVE "ola", 1+1 ;',
            # r'ESCREVE "ola", 1 ,"mundo";',
            # r'VAR h ; ',
            # r'VAR h = 1+5; ',
            # r'VAR y = 10 * (h - 1) ; ',
            # r'VAR z = -1 ; ',
            r'PARA i EM [10..20] FAZER VAR x=1; FIMPARA ;'
            ]

for frase in exemplos:
    #EscreveGrammar.initSymbols()
    print("\n")
    
    #print(f"----------------------")
    #print(f"--- frase '{frase}'")
    res = ag.parse ( frase ) 
    #print(f"resultado: {res}")
