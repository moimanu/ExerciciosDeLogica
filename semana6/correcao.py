# ESTOU REFAZENDO O CÓDIGO DO DETETIVE

# FUNÇÕES:
def receberEntradasConsecutivas(qntdEntradas, lista):
    for entrada in range(qntdEntradas):
        lista.append(list(map(int, input().split())))

def agruparEventosEmVetor(matriz, vetor):
    for i in matriz:
        for j in i:
            if j not in vetor:
                vetor.append(j)

def criarGrafo(lista, grafo, chave, valor):
    for par in lista:
        grafo[par[chave]] = []
    for par in lista:
        grafo[par[chave]].append(par[valor])

# VARIAVEIS E VETORES:
eiv = list(map(int, input().split()))

listaParesEventos = []
receberEntradasConsecutivas(eiv[1], listaParesEventos) 

xi = list(map(int, input().split()))

eventos = []
agruparEventosEmVetor(listaParesEventos, eventos)

print("\nLISTA DE PARES DE EVENTOS:\n", listaParesEventos,"\n")
print("\nLISTA DE EVENTOS:\n", eventos,"\n")


# GRAFOS:
grafoCausaConsequencia = {}
criarGrafo(listaParesEventos, grafoCausaConsequencia, 0, 1)

grafoConsequenciaCausa = {}
criarGrafo(listaParesEventos, grafoConsequenciaCausa, 1, 0)

print("\nGRAFO CAUSA -> CONSEQUENCIA:\n", grafoCausaConsequencia,"\n")
print("\nGRAFO CONSEQUENCIA -> CAUSA:\n", grafoConsequenciaCausa,"\n")
