# arith_lexer_test.py
from EscreveLexer import EscreveLexer

al = EscreveLexer()
al.build()
#al.input('PARA i EM [10..20] FAZER 1+1; FIMPARA ;') #"(3+5)*7")
al.input('VAR x = "1" ;') #"(3+5)*7")


while True:
    tk = al.token() 
    if not tk: 
        break
    print(tk,end=" ")

    