qntdTestes = int(input())
listaPassos = []

for teste in range(qntdTestes):
    comprimentoTrem = int(input())
    vagoes = list(map(int, input().split()))

    passos = 0
    menorVagao = 1
    for vagao in vagoes:
        for n in vagoes:
            if(n == menorVagao and vagoes.index(n) != n-1):
                passos += vagoes.index(n) - (n-1)
                vagoes.remove(n)
                vagoes.insert(n-1, n)
        menorVagao += 1
    listaPassos.append(passos)

for passo in listaPassos:
    print("Optimal train swapping takes", passo,"swaps.")