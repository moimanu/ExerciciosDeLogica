# AINDA ESTOU TRABALHANDO NESSE EXERCÍCIO...

# FUNÇÕES:
def receberEntradasConsecutivas(qntdConexoes):
    temp = []
    for c in range(qntdConexoes):
        temp.append(list(map(int, input().split())))
    return temp

def conferirCaminho(verticeA):
    if verticeA in grafo:
        for verticeB in grafo[verticeA]:
            grafo[verticeB].remove(verticeA)
            contadorPassos.append(verticeB)
            conferirCaminho(verticeB)

# ENTRADAS:
testes = int(input())
verticeInicial = int(input())
qntdVerticesEArestas = list(map(int, input().split()))
arestas = receberEntradasConsecutivas(qntdVerticesEArestas[1])

# GRAFO:
grafo = {}
for a in arestas:
    grafo[a[0]] = []
    grafo[a[1]] = []
for a in arestas:
    if a[1] not in grafo[a[0]]:
        grafo[a[0]].append(a[1])
    if a[0] not in grafo[a[1]]:
        grafo[a[1]].append(a[0])

# print("\n")
# print("TESTES:",testes,"\n")
# print("VÉRTICE INICIAL:",verticeInicial,"\n")
# print("QNTD V E A:",qntdVerticesEArestas,"\n")
# print("ARESTAS:",arestas,"\n")
# print("GRAFO:",grafo,"\n")

contadorPassos = []
conferirCaminho(verticeInicial)

# print("CONTADOR DE PASSOS:",contadorPassos,"\n")
print(len(contadorPassos)*2)
