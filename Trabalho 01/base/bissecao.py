import os
import numpy

    
def bissecao(func, a, b, precision):
    if (func(a) * func(b) >= 0):
        return "Não há raizes nesse intervalo"

    meio = a
    while (abs(b - a) >= precision or abs(func(meio)) >= precision):
        
        meio = (a + b) / 2
        #printData(func, a, b, meio)
        
        if(func(meio) == 0):
            return func(meio)
    
        if(func(meio) * func(a) >= 0):
            a = meio
        else:
            b = meio
        
        #printData(func, a, b, meio)
    
    return meio

def main():
    print("Exemplo de função --> (x*x*x) - 9*x + 3")
    i = input("Entre com a função no formato do terminal: ") 
    i = compile(i, 'input', 'eval')
    a = int(input("Entre o primeiro intervalo : "))
    b = int(input("Entre o segundo intervalo : "))
    prec = float(input("Entre com a precisão : "))
    func = lambda x : eval(i, {'x': x, 'np': numpy})

    res = bissecao(func, a, b, prec)
    print("Raiz encontrada : ", res)

if __name__ == "__main__":
    main()    