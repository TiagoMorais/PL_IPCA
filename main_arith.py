# arith.py
from ArithGrammar2 import ArithGrammar

ag = ArithGrammar()
ag.build()

exemplos = [ # exemplos a avaliar de forma independente... 
            r'1+1+5-9*2',
            r'1-1',
            r'2*2',
            ]

for frase in exemplos:
    print("\n")
    ArithGrammar.initSymbols()
    #print(f"----------------------")
    #print(f"--- frase '{frase}'")
    res = ag.parse ( frase ) 
    #print(f"resultado: {res}")
