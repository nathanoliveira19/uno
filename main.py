from cards import *
from initial import *
from actions import *


comprar, jogar, jogador, cpu = criaDeckEmbaralharado()
#print("Jogar:" + str(jogar) + "\n")
#print("Jogador:" + str(jogador) + "\n")
#print(cartasPermitidas(jogador, jogar))
print("Carta na mesa:\n")
desenharCarta(jogar)      
