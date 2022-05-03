import tests
import numpy

def main():
    print("Exemplo de função --> (x*x*x) - 9*x + 3")
    i = input("Entre com a função no formato do terminal: ") 
    user_input = i
    i = compile(i, 'input', 'eval')
    a = int(input("Entre o primeiro intervalo : "))
    b = int(input("Entre o segundo intervalo : "))
    prec = float(input("Entre com a precisão : "))
    func = lambda x : eval(i, {'x': x, 'np': numpy})

    tests.runTests(func, a, b, prec, user_input)

if __name__ == "__main__":
    main()    