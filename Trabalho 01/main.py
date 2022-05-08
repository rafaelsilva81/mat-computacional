import tests
import numpy
import math

def main():
    """  print("Exemplo de função --> (x*x*x) - 9*x + 3")
    i = input("Entre com a função no formato do terminal: ") 
    user_input = i
    i = compile(i, 'input', 'eval') """

    a = -100
    b = 100

    a2 = 10
    b2 = 40
    
    prec1 = math.pow(2,-5)
    func1 = lambda x : (math.pow(x,5) - 3*(math.pow(x,4)) - 3*(math.pow(x,2)) + 2)

    prec2 = math.pow(10, -3)
    func2 = lambda x : (math.sqrt(x) - math.pow(5,(-1*x)))

    prec3 = 0.01
    func3 = lambda x : (math.pow(x,5) - math.pow(x,4) - 4*x + 1)

    prec4 = 0.005
    func4 = lambda x : (0.05*(math.pow(x,3)) - 0.4*math.pow(x,2) + 3*x*math.sin(x))
    
    tests.runTests(func1, a, b, prec1, 'LETRA-A')
    tests.runTests(func2, a2, b2, prec2, 'LETRA-B')
    tests.runTests(func3, a, b, prec3, 'LETRA-C')
    tests.runTests(func4, a, b, prec4, 'LETRA-D')

if __name__ == "__main__":
    main()