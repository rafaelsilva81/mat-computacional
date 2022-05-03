import os
import numpy
    
def posicaoFalsa(func, a, b, precision):
    x1 = a
    f1 = func(x1)
    x2 = b
    f2 = func(x2)
    x3 = 0
    f3 = 0

    max_itr = 300

    #Inicialização
    itr = 0
    success = 0
    root = x1

    if (f1 * f2 >= 0):
        return "Não é possivel garantir que há raízes nesse intervalo"
    
    while True:
        x3 = x1 - (x2 - x1) * f1 / (f2 - f1)
        f3 = func(x3)
        if (f1 * f3 < 0): #Caso isso seja verdadeiro, a raiz está entre [x2, x3]
            x2 = x3
        else: #Se não, a raiz está entre [x1, x3]
            x1 = x3
        if (abs(f1) < abs(f2)):
            root = x1
        else: 
            root = x2
        itr = itr+1
        success = (abs(x2-x1) <= precision)
        if (success or itr >= max_itr):
            break
    
    return root


def main():
    print("Exemplo de função --> (x*x*x) - 9*x + 3")
    i = input("Entre com a função no formato do terminal: ")
    i = compile(i, 'input', 'eval')
    a = int(input("Entre o primeiro intervalo : "))
    b = int(input("Entre o segundo intervalo : "))
    prec = float(input("Entre com a precisão : "))
    #print(prec)
    func = lambda x : eval(i, {'x': x, 'np': numpy})

    res = posicaoFalsa(func, a, b, prec)
    print("Raiz encontrada : ", res)

if __name__ == "__main__":
    main()    