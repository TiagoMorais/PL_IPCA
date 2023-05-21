# arith.py
from EscreveGrammar import EscreveGrammar

ag = EscreveGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente... 
            r'ESCREVE "ola", "mundo";',
            ]
for frase in exemplos:
    EscreveGrammar.initSymbols()
    #print(f"----------------------")
    #print(f"--- frase '{frase}'")
    res = ag.parse ( frase ) 
    #print(f"resultado: {res}")
