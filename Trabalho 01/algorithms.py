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