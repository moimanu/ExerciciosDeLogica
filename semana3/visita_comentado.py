#PASSO 1)
#Primeira entrada para definir N, A e B =>
entrada1 = list(map(int, input().split())) # <= Criação de uma lista com a primeira entrada
if entrada1[1] > entrada1[2]:
    entrada1 = [entrada1[0],entrada1[2],entrada1[1]] # <= Ordenando o caminho no sentido da "menor" cidade para a "maior" cidade
qntdN = entrada1[0] - 1
cityA = entrada1[1]
cityB = entrada1[2]

#PASSO 2)
#Criação de uma matriz em que cada item representa uma aresta "D" que vai do "P" ao "Q" =>
maior_vertice = 0
matriz=[]
for n in range(qntdN):
    temp = list(map(int, input().split())) # <= Lista temporária do input para adicionar à matriz

    temp = [temp[0], temp[1], temp[2]] #| <= Criando simetria entre todos os vértices
    matriz.append(temp)                #| 
    temp = [temp[1], temp[0], temp[2]] #| 
    matriz.append(temp)                #|

    if temp[0]>maior_vertice: # <= Definindo o maior vértice para declarar o fim do grafo
        maior_vertice = temp[0]  

#PASSO 3)
#Criação de uma "tabela hash" (dicionário python), para o grafo, a partir da matriz =>
grafo = {}
for n in matriz: # <= Abri chaves para todos os vértices de partida
    grafo [n[0]] = {}
for n in matriz: # <= Adicionei os vértices de destino respectivos aos vértices de partida
    grafo [n[0]] [n[1]] = n[2]
grafo [maior_vertice] = {} # <= Declarando o fim do grafo

#PASSO 4)
#Função para encontrar o caminho de "A" até "B"
v_validos = []
seq_city = []
def procurar_caminho (cityA):
    v_validos.append(cityA) # <= Adiciona o vertice aos v. válidos

    for n in grafo[cityA].keys():  #| <= Pra cada vértice destino do vértice de partida:
        if n == cityB:             #| <= Se encontrar a cidade destino
            v_validos.append(n)    #| <= Armazenar cidade destino aos v. válidos
            for n in v_validos:    #| <= Armazenar as cidades processadas na "sequencia final de cidades"
                seq_city.append(n) #|
            break                  #| <= Termina

        grafo[n].pop(cityA, None) # <= Serve para tirar os vértices cíclicos...

        procurar_caminho(n) # <= Se não encontrou o fim, volta à função (recursão)

        if n != cityB:      #| <= Se o caminho não levar à nada:
            v_validos.pop() #| <= Tira o vértice dos válidos e passa para o próximo

procurar_caminho(cityA) # <= Chama a função

#PASSO 5)
#Somátorio das arestas para encontrar o valor do caminho
tamanho_caminho = 0
for n in range(1, len(seq_city)):
    tamanho_caminho = tamanho_caminho + grafo[seq_city[n-1]] [seq_city[n]]
print(tamanho_caminho)

#RESUMO
#Passo 1) Receber a primeira entrada e definir N, A e B
#Passo 2) Receber todas as outras entradas e definir P, Q e D (bem como Q, P e D) em uma matriz
#Passo 3) Criar um grafo, com um dicionário, a partir da matriz anterior
#Passo 4) Encontrar o caminho de A até B e armazená-lo (eliminando os caminhos cíclicos)
#Passo 5) Realizar o somatório das arestas do caminho armazenado
