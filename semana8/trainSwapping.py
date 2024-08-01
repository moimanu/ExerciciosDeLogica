qntdTestes = int(input())
listaPassos = []

for teste in range(qntdTestes):
    comprimentoTrem = int(input())
    vagoes = list(map(int, input().split()))

    passos = 0

    for nVagao in range(comprimentoTrem):
        if(vagoes.index(nVagao+1) != nVagao):
            passos += vagoes.index(nVagao+1) - (nVagao)
            vagoes.remove(nVagao+1)
            vagoes.insert(nVagao, nVagao+1)
    
    listaPassos.append(passos)

for passo in listaPassos:
    print("Optimal train swapping takes", passo,"swaps.")
