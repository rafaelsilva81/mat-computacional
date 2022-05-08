import inspect
import numpy
import math
from asyncore import write
import csv
import time
from algorithms import bissecao, posicaoFalsa, pegasus

header = ['Metodo utilizado', 'Raiz encontrada', 'Tempo de execução(ms)', 'Quantidade de Iterações']

def ms(tempo, casas_decimais): 
    return round((tempo * 1000), casas_decimais)

def runTests(func, a, b, prec, filename):
    data_bissecao = []
    data_falsaPosicao = []
    data_pegasus = []

    #Teste bissecao
    start = time.time()
    bis = bissecao(func, a, b, prec)
    end = time.time()
    t = ms(end - start, 5)

    #Teste falsaPosicao
    start2 = time.time()
    pos = posicaoFalsa(func, a, b, prec)
    end2 = time.time()
    t2 = ms(end2 - start2, 5)

    #Teste pegasus
    start3 = time.time()
    peg = pegasus(func, a, b, prec)
    end3 = time.time()
    t3 = ms(end3 - start3, 5)

    data_bissecao.append(["Bisseção", bis[1], float(t), bis[0]])
    data_falsaPosicao.append(["Falsa Posição", pos[1], float(t2), pos[0]])
    data_pegasus.append(["Pegasus", peg[1], float(t3), peg[0]])
    
    writeTests(data_bissecao, data_falsaPosicao, data_pegasus, prec, filename)

def writeTests(dataBissecao, dataFalsaPosicao, dataPegasus, prec, n):
    metadata = ['Precisão:', float(prec)]
    file_name = 'tests/' + n + "-" + time.strftime("%d-%m-%Y-%H_%M_%S")  + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(dataBissecao) 
        writer.writerows(dataFalsaPosicao)
        writer.writerows(dataPegasus)
        writer.writerow('')
        writer.writerow(metadata)