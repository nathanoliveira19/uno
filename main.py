from cards import *
from initial import *
from actions import *
import os
import time
import random

comprar, aux, jogador, cpu = criaDeckEmbaralharado()

mesa = []
mesa.append(aux)

comando = ""
aplicar = False
reverso = False
pular = False

while comando != "s":
    os.system('cls' if os.name == 'nt' else 'clear')
    if aplicar is True:
        jogador, comprar, reverso, pular = acao(mesa[-1:][0], jogador, comprar, aplicar)
        aplicar = False
    print("Digite s para sair do jogo.")
    print("Carta na mesa:\n")
    desenharCarta(mesa[-1:][0])
    print("Sua vez!!!\n")
    print("Quantidades de cartas da CPU: {}".format(len(cpu)))
    print("\nSuas cartas:")
    desenharDeckSeparado(jogador, 3)
    comando = input("Digite um comando: ")
    resultadoOperacao = False
    if reverso is False and pular is False:
        try:
            if comando != "comprar" and comando != "s":
                jogador, mesa, resultadoOperacao = jogar_carta(jogador, jogador[int(comando)], mesa)
                aplicar = True
                if resultadoOperacao is False:
                    print("Não foi possível jogar esta carta", end="\r")
                    time.sleep(1)
                else:
                    print("Jogando carta...", end="\r")
                    time.sleep(1)
            elif comando == "comprar":
                if cartasPermitidas(jogador, mesa[-1:][0]) == []:
                    jogador, comprar = comprar_cartas(jogador, comprar)
                    print("Comprando carta...", end="\r")
                    time.sleep(1)
                else:
                    print("Você só pode comprar se não tiver cartas para jogar!", end="\r")
                    time.sleep(1)
        except:
            print("Comando inválido", end="\r")
            resultadoOperacao = False
            time.sleep(1)

    #Vez da cpu
    if aplicar is True:
        cpu, comprar, reverso, pular = acao(mesa[-1:][0], cpu, comprar, aplicar)
        aplicar = False
    if resultadoOperacao is True and (reverso is False and pular is False):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Carta na mesa:\n")
        desenharCarta(mesa[-1:][0])

        print("Vez da CPU...\n")
        cartas_uno = []
        for i in range(0, len(cpu)):
            cartas_uno.append(uno)
        desenharDeckSeparado(cartas_uno, 3)
        permitidas_cpu = cartasPermitidas(cpu, mesa[-1:][0])
        if permitidas_cpu != []:
            jogar_cpu = permitidas_cpu[random.randint(0, len(permitidas_cpu) - 1)]
            cpu, mesa, resultadoOperacao = jogar_carta_cpu(cpu, jogar_cpu, mesa)
            aplicar = True
            print("Jogando carta...", end="\r")
            time.sleep(3.5)
        else:
            cpu, comprar = comprar_cartas(cpu, comprar)
            print("Comprando carta...", end="\r")
            time.sleep(3.5)

