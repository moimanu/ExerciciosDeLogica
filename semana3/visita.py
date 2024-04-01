entrada1 = list(map(int, input().split()))
if entrada1[1] > entrada1[2]:
    entrada1 = [entrada1[0],entrada1[2],entrada1[1]]
qntdN = entrada1[0] - 1
cityA = entrada1[1]
cityB = entrada1[2]

maior_vertice = 0
matriz=[]
for n in range(qntdN):
    temp = list(map(int, input().split())) 

    temp = [temp[0], temp[1], temp[2]]
    matriz.append(temp)                
    temp = [temp[1], temp[0], temp[2]] 
    matriz.append(temp)                

    if temp[0]>maior_vertice:
        maior_vertice = temp[0]  

grafo = {}
for n in matriz: 
    grafo [n[0]] = {}
for n in matriz: 
    grafo [n[0]] [n[1]] = n[2]
grafo [maior_vertice] = {}

v_validos = []
seq_city = []
def procurar_caminho (cityA):
    v_validos.append(cityA) 
    for n in grafo[cityA].keys():  
        if n == cityB:           
            v_validos.append(n)
            for n in v_validos:
                seq_city.append(n) 
            break

        grafo[n].pop(cityA, None)

        procurar_caminho(n) 

        if n != cityB:     
            v_validos.pop()

procurar_caminho(cityA)

tamanho_caminho = 0
for n in range(1, len(seq_city)):
    tamanho_caminho = tamanho_caminho + grafo[seq_city[n-1]] [seq_city[n]]
print(tamanho_caminho)