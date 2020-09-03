import random

def cartasPermitidas(jogador, carta):
    permitidas = []
    for j in jogador:
        if j["tipo"] == "mais4" or j["tipo"] == "coringa":
            permitidas.append(j)
        else:
            if j["cor"] == carta["cor"]:
                permitidas.append(j)
            elif j["tipo"] == "mais2" and carta["tipo"] == "mais2":
                permitidas.append(j)
            elif j["tipo"] == "reverso" and carta["tipo"] == "reverso":
                permitidas.append(j)
            elif j["tipo"] == "pular" and carta["tipo"] == "pular":
                permitidas.append(j)
            elif carta["tipo"] == "comum" and j["tipo"] == "comum" and j["numero"] == carta["numero"]:
                permitidas.append(j)
    return permitidas


def jogar_carta(jogador, jogar, mesa):
    permitidas = cartasPermitidas(jogador, mesa[-1:][0])
    if jogar in permitidas:
        if(jogar["cor"] == "branco"):
            cor = input("Escolha uma cor: ")
            if cor == "amarelo" or cor == "azul" or cor == "verde" or cor == "vermelho":
                jogar["cor"] = cor
            else:
                return jogador, mesa, False
        jogador.remove(jogar)
        mesa.append(jogar)
        return jogador, mesa, True
    else:
        return jogador, mesa, False

def jogar_carta_cpu(jogador, jogar, mesa):
    permitidas = cartasPermitidas(jogador, mesa[-1:][0])
    if jogar in permitidas:
        if(jogar["cor"] == "branco"):
            cores = ["amarelo", "azul", "verde", "vermelho"]
            jogar["cor"] = cores[random.randint(0, len(cores) - 1)]
        jogador.remove(jogar)
        mesa.append(jogar)
        return jogador, mesa, True
    else:
        return jogador, mesa, False

def comprar_cartas(jogador, comprar):
    jogador.append(comprar.pop())
    return jogador, comprar

def acao(carta, jogador, comprar, aplicar):
    reverso = False
    pular = False
    if aplicar is True:
        if carta["tipo"] == "reverso":
            reverso = True
        elif carta["tipo"] == "pular":
            pular = True
        elif carta["tipo"] == "mais2":
            jogador.append(comprar.pop())
            jogador.append(comprar.pop())
        elif carta["tipo"] == "mais4":
            jogador.append(comprar.pop())
            jogador.append(comprar.pop())
            jogador.append(comprar.pop())
            jogador.append(comprar.pop()) 

    return jogador, comprar, reverso, pular