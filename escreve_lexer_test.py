# arith_lexer_test.py
from EscreveLexer import EscreveLexer

al = EscreveLexer()
al.build()
#al.input('PARA i EM [10..20] FAZER 1+1; FIMPARA ;') #"(3+5)*7")
al.input("""
    FUNC power(r,t)
    ESCREVE r;
    ESCREVE t;
FIMFUNC

power(2,2);
""") #"(3+5)*7")


while True:
    tk = al.token() 
    if not tk: 
        break
    print(tk,end=" ")

    