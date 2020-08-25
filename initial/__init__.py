from cards import *
import random

def criaDeckEmbaralharado():
    deck = []
    for a in amarelo:
        deck.append(a)
        if a["numero"] != 0:
            deck.append(a)
    for a in azul:
        deck.append(a)
        if a["numero"] != 0:
            deck.append(a)
    for v in verde:
        deck.append(v)
        if v["numero"] != 0:
            deck.append(v)
    for v in vermelho:
        deck.append(v)
        if v["numero"] != 0:
            deck.append(v)

    deck.append(reversoAmarelo)
    deck.append(reversoAmarelo)
    deck.append(pularAmarelo)
    deck.append(pularAmarelo)
    deck.append(mais2Amarelo)
    deck.append(mais2Amarelo)

    deck.append(reversoAzul)
    deck.append(reversoAzul)
    deck.append(pularAzul)
    deck.append(pularAzul)
    deck.append(mais2Azul)
    deck.append(mais2Azul)

    deck.append(reversoVerde)
    deck.append(reversoVerde)
    deck.append(pularVerde)
    deck.append(pularVerde)
    deck.append(mais2Verde)
    deck.append(mais2Verde)

    deck.append(reversoVermelho)
    deck.append(reversoVermelho)
    deck.append(pularVermelho)
    deck.append(pularVermelho)
    deck.append(mais2Vermelho)
    deck.append(mais2Vermelho)

    deck.append(mais4)
    deck.append(mais4)
    deck.append(mais4)
    deck.append(mais4)

    deck.append(coringa)
    deck.append(coringa)
    deck.append(coringa)
    deck.append(coringa)

    random.shuffle(deck)

    jogar = deck[0]
    while jogar["tipo"] != "comum":
        random.shuffle(deck)
        jogar = deck[0]
        
    jogador = deck[1:8]
    cpu = deck[8:15]
    comprar = deck[15:]

    return comprar, jogar, jogador, cpu