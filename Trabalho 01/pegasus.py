import os
import numpy

    
def pegasus(func, a, b, precision):
    x1 = a
    f1 = func(x1)
    x2 = b
    f2 = func(x2)
    x3 = 0
    f3 = 0
    
    #Inicialização
    success = 0
    root = x1

    if (f1 * f2 >= 0):
        return "Não é possivel garantir que há raízes nesse intervalo"
    
    while True:
        x3 = x2 - f2/( (f2-f1)/(x2-x1) )
        f3 = func(x3)
        if (f3 * f2 <= 0): #Caso isso seja verdadeiro, a raiz está entre [x2, x3]
            #Replace (x1,f1) with (x2,f2)
            x1 = x2
            f1 = f2
            #Replace (x2,f2) with (x3,f3)
            x2 = x3
            f2 = f3
        else: #Se não, a raiz está entre [x1, x3]
            #Replace (x1,f1) by (x1,f1')
            f1 = f1 * f2 / (f2 +  f3)
            #Replace (x2, f2) with (x3,f3)
            x2 = x3
            f2 = f3
        if (abs(f1) < abs(f2)):
            root = x1
        else: 
            root = x2
        success = (abs(x2-x1) <= precision)
        if (success):
            break
    
    return root

def main():
    print("Exemplo de função --> (x*x*x) - 9*x + 3")
    i = input("Entre com a função no formato do terminal: ")  # enter function once
    i = compile(i, 'input', 'eval')
    a = int(input("Entre o primeiro intervalo : "))
    b = int(input("Entre o segundo intervalo : "))
    prec = float(input("Entre com a precisão : "))
    #print(prec)
    func = lambda x : eval(i, {'x': x, 'np': numpy})

    res = pegasus(func, a, b, prec)
    print("Raiz encontrada : ", res)

if __name__ == "__main__":
    main()    