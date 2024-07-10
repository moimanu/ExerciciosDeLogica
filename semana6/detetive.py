entrada1 = list(map(int, input().split())) # <= Primeira entrada (E, I, V)

lista=[]
for n in range(entrada1[1]):
    lista.append(list(map(int, input().split()))) # <= lista com os pontos A e B

ultimaEntrada = list(map(int, input().split())) # <= Última entrada (Xi)

print("LISTA: ", lista)

grafo = {}
for n in lista:
    grafo[n[1]] = []
for n in lista:
    grafo[n[1]].append(n[0])
    
print("GRAFO: ", grafo)

listaDeUltimosVertices = []
def printarGrafo(vertice):
    if (grafo.get(vertice, False)):
        for n in grafo[vertice]:
            print(n)
            printarGrafo(n)
    else: 
        print("O último vértice foi: ", vertice)
        listaDeUltimosVertices.append(vertice)
        
printarGrafo(ultimaEntrada[0])

print("FILHOS DO PRIMEIRO VÉRTICE: ", grafo[ultimaEntrada[0]])
print("LISTA DE ÚLTIMOS VÉRTICES: ",listaDeUltimosVertices)