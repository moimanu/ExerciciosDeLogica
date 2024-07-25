# FUNÇÕES:
def receberEntradasConsecutivas(qntdConexoes):
    temp = []
    for c in range(qntdConexoes):
        temp.append(list(map(int, input().split())))
    return temp

def preencherGrafo(grafo, arestas):
    for a in arestas:
        grafo[a[0]] = []
        grafo[a[1]] = []
    for a in arestas:
        if a[1] not in grafo[a[0]]:
            grafo[a[0]].append(a[1])
        if a[0] not in grafo[a[1]]:
            grafo[a[1]].append(a[0])

def conferirCaminho(verticeA, grafo, contador):
    if verticeA in grafo:
        for verticeB in grafo[verticeA]:
            grafo[verticeB].remove(verticeA)
            contador.append(verticeB)
            conferirCaminho(verticeB, grafo, contador)
            
def encontrarQntdPassos(listaParaGuardar):
    # ENTRADAS:
    verticeInicial = int(input())
    qntdVerticesEArestas = list(map(int, input().split()))
    arestasLabirinto = receberEntradasConsecutivas(qntdVerticesEArestas[1])

    # PROCESSO:
    grafoLabirinto = {}
    preencherGrafo(grafoLabirinto, arestasLabirinto)

    contadorPassos = []
    conferirCaminho(verticeInicial, grafoLabirinto, contadorPassos)

    listaParaGuardar.append(len(contadorPassos)*2)

# SAÍDA:
testes = int(input())
qntdPassos = []

for n in range(testes):
    encontrarQntdPassos(qntdPassos)

for n in qntdPassos:
    print(n)
