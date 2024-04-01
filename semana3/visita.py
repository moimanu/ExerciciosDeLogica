entrada1 = list(map(int, input().split()))
if entrada1[1] > entrada1[2]:
    entrada1 = [entrada1[0],entrada1[2],entrada1[1]]
qntd_de_entradas = entrada1[0] - 1
vert_ini = entrada1[1]
vert__fin = entrada1[2]

maior_vertice = 0

#Criação de uma matriz com todas as entradas =>
matriz=[]
for n in range(qntd_de_entradas):
    temp = list(map(int, input().split())) # <= Lista temporária do input para adicionar à matriz
    temp = [temp[0], temp[1], temp[2]]  
    matriz.append(temp)
    temp = [temp[1], temp[0], temp[2]]  
    matriz.append(temp)     

    if temp[0]>maior_vertice:
        maior_vertice = temp[0]  

#Criação de uma tabela hash (para o grafo) a partir da matriz =>
grafo = {}
for n in matriz:
    grafo [n[0]] = {}
for n in matriz:
    grafo [n[0]] [n[1]] = n[2]
grafo [maior_vertice] = {}

#Função para encontrar o caminho de "A" até "B"
processado = []
lista_final = []
def procurar_caminho (vert_ini):
    processado.append(vert_ini)

    for n in grafo[vert_ini].keys(): 
        if n == vert__fin:
            processado.append(n)
            for n in processado:
                lista_final.append(n)
            break
        grafo[n].pop(vert_ini, None) # <= Serve para tirar os vértices cíclicos...
        procurar_caminho(n)
        if n != vert__fin:
            processado.pop()

procurar_caminho(vert_ini)

#Somátorio das arestas para encontrar o valor do caminho
tamanho_caminho = 0
for n in range(1, len(lista_final)):
    tamanho_caminho = tamanho_caminho + grafo[lista_final[n-1]] [lista_final[n]]

print(tamanho_caminho)