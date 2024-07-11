# ENTRADAS:
entrada1 = list(map(int, input().split())) # <= Primeira entrada (E, I, V)

listaParesEventos = []
for n in range(entrada1[1]):
    listaParesEventos.append(list(map(int, input().split()))) # <= lista com os pontos A e B

ultimaEntrada = list(map(int, input().split())) # <= Última entrada (Xi)

print("\nLISTA DE PARES DE EVENTOS:\n", listaParesEventos,"\n")

# GUARDANDO TODOS OS EVENTOS EM UMA LISTA E OS ORDENANDO
eventos = []
for n in listaParesEventos:
    for i in n:
        if i not in eventos:
            eventos.append(i)
eventos.sort()

# TRANSFORMANDO A LISTA DE PARES EM UM GRAFO (dicionário)
grafo = {}
for n in listaParesEventos:
    grafo[n[1]] = []
for n in listaParesEventos:
    grafo[n[1]].append(n[0])
    
print("GRAFO:\n", grafo,"\n")

# CONFERINDO AS PRIMEIRAS CONEXÕES ÚNICAS A PARTIR DO EVENTO CONFIRMADO
listaConexoesUnicas = []
def conferirConexaoUnica(evento):
    if (grafo.get(evento, False)):
        if (len(grafo[evento]) == 1):
            if evento not in listaConexoesUnicas:
                listaConexoesUnicas.append(evento)
            listaConexoesUnicas.append(grafo[evento][0])
            conferirConexaoUnica(grafo[evento][0])
            ultimaEntrada[n] = grafo[evento][0]

for n in range(len(ultimaEntrada)):
    conferirConexaoUnica(ultimaEntrada[n]) # <= Atualizando o evento verdadeiro para a próxima conexão única

print("EVENTOS COM CONEXÕES ÚNICAS (a partir do primeiro verdadeiro):\n", listaConexoesUnicas,"\n")
print("ÚLTIMOS EVENTOS INICIAIS CONFIRMADOS:\n", ultimaEntrada,"\n")

# CONFERINDO A PRIMEIRA CAUSA A PARTIR DE UM EVENTO VERDADEIRO
listaDePrimeirasCausas = []
def encontrarPrimeiraCausa(evento):
    if (grafo.get(evento, False)):
        for n in grafo[evento]:
            encontrarPrimeiraCausa(n)
    else: 
        listaDePrimeirasCausas.append(evento)

saida = []

for n in range(len(ultimaEntrada)):
    encontrarPrimeiraCausa(ultimaEntrada[n])
    print("LISTA DE PRIMEIRAS CAUSAS:\n",listaDePrimeirasCausas,"\n")

    # CONFERINDO SE HÁ ALGUMA BIFURCAÇÃO
    bifurcacao = False
    for i in listaDePrimeirasCausas:
        if i != listaDePrimeirasCausas[0]:
            bifurcacao = True
            break
    
    # CONFIGURANDO A SAÍDA
    if bifurcacao:
        if(len(listaConexoesUnicas) < 1):
            saida.append(ultimaEntrada[n])
        else:
            for c in listaConexoesUnicas:
                if c not in saida:
                    saida.append(c)
    else:
        for e in eventos:
            saida.append(e)
        break

saida.sort()

print("SAÍDA:\n", " ".join(map(str, saida)),"\n")