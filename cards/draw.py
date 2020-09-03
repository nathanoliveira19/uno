# -*- coding: UTF-8 -*-
from termcolor import colored
import math

def printLinhas(linhas, carta):
    for linha in linhas:
        if carta["cor"] == "amarelo":
            print(colored(linha, 'yellow'))
        elif carta["cor"] == "azul":
            print(colored(linha, 'blue'))
        elif carta["cor"] == "verde":
            print(colored(linha, 'green'))
        elif carta["cor"] == "vermelho":
            print(colored(linha, 'red'))
        elif carta["cor"] == "branco":
            print(colored(linha, 'white'))
        else:
            print("Essa carta precisa ter uma cor definida!")    


def stringCartaUNO(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│    UNO    │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("└───────────┘")
    return linhas

def stringCartaComum(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│{}          │".format(carta["numero"]))
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│     {}     │".format(carta["numero"]))
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│          {}│".format(carta["numero"]))
    linhas.append("└───────────┘")
    return linhas

def stringCartaReverso(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│ ↗↙        │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│     ↗↙    │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│         ↗↙│")
    linhas.append("└───────────┘")
    return linhas

def stringCartaPular(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│ ⦸         │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│     ⦸     │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│          ⦸│")
    linhas.append("└───────────┘")
    return linhas

def stringCartaMaisDois(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│ ⁺²        │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│    +2     │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│         ⁺²│")
    linhas.append("└───────────┘")
    return linhas

def stringCartaMaisQuatro(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│ +4        │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│    +4     │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│         ⁺4│")
    linhas.append("└───────────┘")
    return linhas

def stringCartaCoringa(carta):
    linhas = []
    linhas.append("┌───────────┐")
    linhas.append("│ ⨁         │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│    ⨁      │")
    linhas.append("│           │")
    linhas.append("│           │")
    linhas.append("│         ⨁ │")
    linhas.append("└───────────┘")
    return linhas

def desenharCartaComum(carta):
    printLinhas(stringCartaComum(carta), carta)

def desenharCartaReverso(carta):
    printLinhas(stringCartaReverso(carta), carta)

def desenharCartaPular(carta):    
    printLinhas(stringCartaPular(carta), carta)

def desenharCartaMaisDois(carta):
    printLinhas(stringCartaMaisDois(carta), carta)

def desenharCartaMaisQuatro(carta):
    printLinhas(stringCartaMaisQuatro(carta), carta)

def desenharCartaCoringa(carta):
    printLinhas(stringCartaCoringa(carta), carta)

def desenharDeck(cartas):
    tamanhos = []
    print_arg = []
    primeiro = 0
    for carta in cartas:
        if carta["tipo"] == "comum":
            desenho = stringCartaComum(carta)
        elif carta["tipo"] == "reverso":
            desenho = stringCartaReverso(carta)
        elif carta["tipo"] == "pular":
            desenho = stringCartaPular(carta)
        elif carta["tipo"] == "mais2":
            desenho = stringCartaMaisDois(carta)
        elif carta["tipo"] == "mais4":
            desenho = stringCartaMaisQuatro(carta)
        elif carta["tipo"] == "coringa":
            desenho = stringCartaCoringa(carta)
        elif carta["tipo"] == "uno":
            desenho = stringCartaUNO(carta)
        if carta["cor"] == "amarelo":
            color = "yellow"
        elif carta["cor"] == "azul":
            color = "blue"
        elif carta["cor"] == "vermelho":
            color = "red"
        elif carta["cor"] == "verde":
            color = "green"
        else:
            color = "white"
            
        i = 0
        for linha in desenho:
            if primeiro == 0:
                print_arg.append(colored(linha, color))
            else:
                print_arg[i] = print_arg[i] + "  " +  colored(linha, color)
            i = i + 1
        primeiro = 1
    for arg in print_arg:
        print(arg)

def desenharCarta(carta):
    if carta["tipo"] == "comum":
        desenharCartaComum(carta)
    elif carta["tipo"] == "reverso":
        desenharCartaReverso(carta)
    elif carta["tipo"] == "pular":
        desenharCartaPular(carta)
    elif carta["tipo"] == "mais2":
        desenharCartaMaisDois(carta)
    elif carta["tipo"] == "mais4":
        desenharCartaMaisQuatro(carta)
    elif carta["tipo"] == "coringa":
        desenharCartaCoringa(carta)
    else:
        print("Não foi possível desenhar a carta")

def desenharDeckSeparado(cartas, limiteLinha):
    indiceEsq = 0
    indiceDir = indiceEsq + limiteLinha
    acabou = False
    while not acabou:
        desenharDeck(cartas[indiceEsq:indiceDir])
        aux = indiceEsq
        indiceEsq = indiceDir
        if aux + limiteLinha < len(cartas):
            indiceDir = aux + limiteLinha
        elif indiceDir != len(cartas):
            indiceDir = len(cartas)
        else:
            acabou = True