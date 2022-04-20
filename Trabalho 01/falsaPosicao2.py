import os
import numpy

def isNegative( num ):
    if num<0:
        return True
    else:
        return False

    
def posicaoFalsa(func, a, b, precision):
    if (func(a) * func(b) >= 0):
        return "Não é garantido encontrar uma raiz nesse intervalo"

    prox_iteracao = a
    while (abs(b-a) >= precision or abs(func(prox_iteracao)) >= precision):
        
        prox_iteracao = (b*func(a) - a*func(b)) / (func(a) - func(b))
        
        if(func(prox_iteracao) == 0):
            break

        #print("Xk ", prox_iteracao)
        #print("F(xk) ", func(prox_iteracao))
        #x = input()

        if(func(a) * func(prox_iteracao) >= 0):
            a = prox_iteracao
        else:
            b = prox_iteracao

        #print("a ", a)
        #print("b ", b)
        #print("|b-a|", abs(b-a))
        
        #if(abs(b-a) < precision and abs(func(prox_iteracao)) < precision):
           #break

        #x = input()
        
    
    return prox_iteracao

def main():
    print("Exemplo de função --> 2*(x*x*x) - 5*(x*x) + x + 10")
    i = input("Entre com a função no formato do terminal: ")  # enter function once
    i = compile(i, 'input', 'eval')
    a = int(input("Entre o primeiro intervalo : "))
    b = int(input("Entre o segundo intervalo : "))
    prec = float(input("Entre com a precisão : "))
    print(prec)
    func = lambda x : eval(i, {'x': x, 'np': numpy})

    res = posicaoFalsa(func, a, b, prec)
    print("Raiz encontrada : ", res)

if __name__ == "__main__":
    main()    