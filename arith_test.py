# arith_lexer_test.py
from ArithLexer import ArithLexer

al = ArithLexer()
al.build()
al.input('1+1*1') #"(3+5)*7")

while True:
    tk = al.token() 
    if not tk: 
        break
    print(tk,end=" ")

    