def receberEntrada():
    return(list(map(int, input().split())))

def receberEntradasConsecutivas(qntdEntradas):
    listaTemp = []
    for entrada in range(qntdEntradas):
        listaTemp.append(list(input().split()))
    return listaTemp

def algoritmo():
    servidores = receberEntradasConsecutivas(servidoresEClientes[0]) 
    requisicoes = receberEntradasConsecutivas(servidoresEClientes[1]) 
    conexoes = 0

    for r in requisicoes:
        temp = []
        for app in range(len(r)):
            for s in servidores:
                if r[app] in s:
                    if r[app] not in temp:
                        temp.append(r[app])
        conexoes += len(temp)
    
    saida.append(conexoes)

saida = []
while True:
    servidoresEClientes = receberEntrada()
    if servidoresEClientes != [0, 0]:
        algoritmo()
    else:
        for s in saida:
            print(s)
        break