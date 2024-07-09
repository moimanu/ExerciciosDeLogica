entrada1 = list(map(int, input().split())) # <= Primeira entrada (E, I, V)

lista=[]
for n in range(entrada1[0]):
    lista.append(list(map(int, input().split()))) # <= lista com os pontos A e B

ultimaEntrada = list(map(int, input().split())) # <= Última entrada (Xi)

grafo = {}
for n in lista: 
    grafo [n[1]] = n[0] # <= Relação entre os pontos A e B

contadorPontas = 0
def procurarCaminho(verticeInicial):
    if (grafo[verticeInicial].keys()):
        for n in grafo[verticeInicial].keys():
            procurarCaminho(n)
    else:
        contadorPontas += 1

for n in ultimaEntrada:
    print(grafo[n])
    print(grafo[n].keys())

print(contadorPontas)
