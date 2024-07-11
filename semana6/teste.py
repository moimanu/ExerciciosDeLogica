# ENTRADAS:
entrada1 = list(map(int, input().split())) # <= Primeira entrada (E, I, V)

lista=[]
for n in range(entrada1[1]):
    lista.append(list(map(int, input().split()))) # <= lista com os pontos A e B

ultimaEntrada = list(map(int, input().split())) # <= Última entrada (Xi)

print("LISTA: ", lista)

# GUARDANDO TODOS OS EVENTOS EM UM VETOR
caminho = []
for n in lista:
    for i in n:
        if i not in caminho:
            caminho.append(i)
caminho.sort()

# TRANSFORMANDO A LISTA EM UM GRAFO
grafo = {}
for n in lista:
    grafo[n[1]] = []
for n in lista:
    grafo[n[1]].append(n[0])
    
print("GRAFO: ", grafo)

# CONFERINDO AS PRIMEIRAS CONEXÕES UNICAS
listaConexoesUnicas = []
def conferirConexaoUnica(vertice):
    if (grafo.get(vertice, False)):
        if (len(grafo[vertice]) == 1):
            listaConexoesUnicas.append(vertice)
            conferirConexaoUnica(grafo[vertice][0])
            ultimaEntrada[0] = listaConexoesUnicas[len(listaConexoesUnicas) - 1]

conferirConexaoUnica(ultimaEntrada[0])

print("CONEXÕES ÚNICAS: ", listaConexoesUnicas)
print("ÚLTIMA CONEXÃO ÚNICA: ", ultimaEntrada[0])
print("EVENTO CONFIRMADO: ", ultimaEntrada)

# CONFERINDO A PRIMEIRA CAUSA DE TODOS OS EVENTOS
listaDePrimeirasCausas = []
def encontrarPrimeiraCausa(evento):
    if (grafo.get(evento, False)):
        for n in grafo[evento]:
            encontrarPrimeiraCausa(n)
    else: 
        print("A causa primeira encontrada foi: ", evento)
        listaDePrimeirasCausas.append(evento)
        
encontrarPrimeiraCausa(ultimaEntrada[0])

print("LISTA DE PRIMEIRAS CAUSAS: ",listaDePrimeirasCausas)

# CONFERINDO SE HÁ ALGUMA BIFURCAÇÃO
bifurcacao = False
for n in listaDePrimeirasCausas:
    if n != listaDePrimeirasCausas[0]:
        bifurcacao = True
        break

# CONFIGURANDO A SAÍDA
if bifurcacao:
    if(len(listaConexoesUnicas) < 1):
        print(ultimaEntrada)
    else:
        print(listaConexoesUnicas)
else:
    print(caminho)