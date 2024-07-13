# FUNÇÕES:
def receberEntrada():
    return(list(map(int, input().split())))

def receberEntradasConsecutivas(qntdEntradas):
    listaTemp = []
    for entrada in range(qntdEntradas):
        listaTemp.append(list(map(int, input().split())))
    return listaTemp

def criarGrafo(lista, grafo, chave, valor):
    for par in lista:
        grafo[par[chave]] = []
    for par in lista:
        grafo[par[chave]].append(par[valor])

def guardarCausaUnica(listaParaGuardar, grafo, listaXi):
    for item in listaXi:
        if(grafo.get(item, False)):
            if(len(grafo[item]) == 1):
                if grafo[item][0] not in listaParaGuardar:
                    listaParaGuardar.append(grafo[item][0])
            guardarCausaUnica(listaParaGuardar, grafo, grafo[item])

def conferirBifurcacao(evento, grafo):
    if (grafo.get(evento, False)):
        for causa in grafo[evento]:
            conferirBifurcacao(causa, grafo)
    else: 
        if evento not in listaDePrimeirasCausas:
            listaDePrimeirasCausas.append(evento)

    if len(listaDePrimeirasCausas) > len(set(listaDePrimeirasCausas)):
        bifurcacao = True
    else:
        bifurcacao = False
    
    return bifurcacao

def encontrarConsequências(evento, grafo, lista):
    if (grafo.get(evento, False)):
        for conseq in grafo[evento]:
            if conseq not in lista:
                lista.append(conseq)
                encontrarConsequências(conseq , grafo, lista)

# ENTRADAS:
eiv = receberEntrada()
listaParesEventos = receberEntradasConsecutivas(eiv[1]) 
xi = receberEntrada()

# GRAFOS:
grafoCausaConsequencia = {}
criarGrafo(listaParesEventos, grafoCausaConsequencia, 0, 1)

grafoConsequenciaCausa = {}
criarGrafo(listaParesEventos, grafoConsequenciaCausa, 1, 0)

# ENCONTRANDO AS CAUSAS QUE POSSUEM APENAS UMA CONSEQUÊNCIA (a partir de uma consequência verdadeira):
causasUnicas = []
guardarCausaUnica(causasUnicas, grafoConsequenciaCausa, xi)

# ENCONTRANDO O CAMINHO DE EVENTOS VERDADEIROS:
causaPrimaria = []
consequenciasVerdadeiras = []
for x in xi:
    listaDePrimeirasCausas = []
    if not(conferirBifurcacao(x, grafoConsequenciaCausa)):
        if len(listaDePrimeirasCausas) == 1:
            causaPrimaria.append(listaDePrimeirasCausas[0])
        encontrarConsequências(listaDePrimeirasCausas[0], grafoCausaConsequencia, consequenciasVerdadeiras)

# SAÍDA:
eventosVerdadeiros = list(set(xi + causasUnicas + consequenciasVerdadeiras + causaPrimaria))
print(" ".join(map(str, eventosVerdadeiros)))

# PRINTS:
# print("\nCAUSA PRIMÁRIA:\n", causaPrimaria)
# print("\nLISTA DE PARES DE EVENTOS:\n", listaParesEventos)
# print("\nGRAFO CAUSA -> CONSEQUENCIA:\n", grafoCausaConsequencia)
# print("\nGRAFO CONSEQUENCIA -> CAUSA:\n", grafoConsequenciaCausa)
# print("\nCAUSAS DE CONSEQUÊNCIAS ÚNICAS:\n", causasUnicas)
# print("\nEVENTOS VERDADEIROS:\n", eventosVerdadeiros, "\n")
