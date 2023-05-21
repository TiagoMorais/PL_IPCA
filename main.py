# arith.py
from EscreveGrammar import EscreveGrammar

ag = EscreveGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente... 
            r'ESCREVE "ola", "mundo";',
            r'ESCREVE "ola", 1+1 ;',
            r'ESCREVE "ola", 1 ,"mundo";',
            r'VAR h ; ',
            r'VAR h = 1+5; ',
            r'VAR y = 10 * (h - 1) ; ',
            r'VAR z = -1 ; ',
            ]

for frase in exemplos:
    print("\n")
    EscreveGrammar.initSymbols()
    #print(f"----------------------")
    #print(f"--- frase '{frase}'")
    res = ag.parse ( frase ) 
    #print(f"resultado: {res}")
