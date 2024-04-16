# Recebendo a entrada:
seq = input()
listaDaSeq = []
for n in range(0, len(seq), 3): # <= Aqui eu criei um loop que itera de 3 em 3
    listaDaSeq.append(seq[slice(n, n+3)]) # <= Aqui eu fiz um append apenas de uma "fatia" de tamanho 3

copas = []
espadas = []
ouros = []
paus = []

for n in listaDaSeq:
    if n[2] == 'C':
        if n in copas:
            copas = 'erro'
        elif copas != 'erro':
            copas.append(n)
    if n[2] == 'E':
        if n in espadas:
            espadas = 'erro'
        elif espadas != 'erro':
            espadas.append(n)
    if n[2] == 'U':
        if n in ouros:
            ouros = 'erro'
        elif ouros != 'erro':
            ouros.append(n)
    if n[2] == 'P':
        if n in paus:
            paus = 'erro'
        elif paus != 'erro':
            paus.append(n)

# Imprimindo a saída:
baralho = [copas, espadas, ouros, paus]
for naipe in baralho:
    if naipe != 'erro':
        naipe = 13 - len(naipe)
    print(naipe)