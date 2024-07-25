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
        for s in servidores:
            for indice in range(len(r)):
                if(indice != 0):
                    if r[indice] in s:
                        temp.append(r[indice])
                        break
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
