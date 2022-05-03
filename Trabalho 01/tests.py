import inspect
import numpy
from asyncore import write
import csv
import time
from algorithms import bissecao, posicaoFalsa, pegasus

header = ['Metodo utilizado', 'Raiz encontrada', 'Tempo de execução(ms)']

def ms(tempo, casas_decimais): 
    return round((tempo * 1000), casas_decimais)

def runTests(func, a, b, prec, user_input):
    data_bissecao = []
    data_falsaPosicao = []
    data_pegasus = []

    #Teste bissecao
    start = time.time()
    bis = bissecao(func, a, b, prec)
    end = time.time()
    t = ms(end - start, 3)

    #Teste falsaPosicao
    start2 = time.time()
    pos = posicaoFalsa(func, a, b, prec)
    end2 = time.time()
    t2 = ms(end2 - start2, 3)

    #Teste pegasus
    start3 = time.time()
    peg = pegasus(func, a, b, prec)
    end3 = time.time()
    t3 = ms(end - start, 3)

    data_bissecao.append(["Bisseção", bis, t])
    data_falsaPosicao.append(["Falsa Posição", pos, t2])
    data_pegasus.append(["Pegasus", peg, t3])
    
    writeTests(data_bissecao, data_falsaPosicao, data_pegasus, user_input, prec)

def writeTests(dataBissecao, dataFalsaPosicao, dataPegasus, user_input, prec):
    metadata = ['Função : ', user_input, 'Precisão : ', prec]
    file_name = 'tests/' + "teste" + time.strftime("%d-%m-%Y-%H_%M_%S")  + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(dataBissecao) 
        writer.writerows(dataFalsaPosicao)
        writer.writerows(dataPegasus)
        writer.writerow(metadata)