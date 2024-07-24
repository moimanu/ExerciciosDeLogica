# FUNÇÕES:
def receberEntradasConsecutivas(qntdConexoes):
    temp = []
    for c in range(qntdConexoes):
        temp.append(list(map(int, input().split())))
    return temp

# ENTRADAS:
testes = int(input())
verticeInicial = int(input())
qntdVerticesEArestas = list(map(int, input().split()))
arestas = receberEntradasConsecutivas(qntdVerticesEArestas[1])

# GRAFO:
grafo = {}
for a in arestas:
    if a[0] < a[1]:
        grafo[a[0]] = []
    else:
        grafo[a[1]] = []
for a in arestas:
    if a[0] < a[1]:
        if a[1] not in grafo[a[0]]:
            grafo[a[0]].append(a[1])
    else:
        if a[0] not in grafo[a[1]]:
            grafo[a[1]].append(a[0])

print("\n")
print("TESTES:",testes,"\n")
print("VÉRTICE INICIAL:",verticeInicial,"\n")
print("QNTD V E A:",qntdVerticesEArestas,"\n")
print("ARESTAS:",arestas,"\n")
print("GRAFO:",grafo,"\n")


def conferirCaminho(verticeA):
    if verticeA in grafo:
        for verticeB in grafo[verticeA]:
            contadorPassos.append(verticeB)
            conferirCaminho(verticeB)

contadorPassos = []
conferirCaminho(verticeInicial)

print(contadorPassos)
print(len(contadorPassos)*2)