
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

def comprar(jogador, comprar):
    jogador.append(comprar.pop())
