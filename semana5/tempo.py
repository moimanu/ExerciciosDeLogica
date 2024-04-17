lista = []
for x in range(int(input())): # Entrada
    entrada = list(input().split())
    lista.append([entrada[0],int(entrada[1])])

saida = []
amigosCalculados = []
contagemPermitida = True

for item in lista: # Criei um laço para cada evento

    amigo = item[1]
    tempoDeConversa = 0

    if amigo not in amigosCalculados: # Se o amigo desse evento já foi calculado, eu não preciso conferí-lo novamente

        amigosCalculados.append(amigo) # Se ele não foi calculado, eu o adiciono à lista de amigos calculados

        for indice in range(lista.index(item), len(lista)): # Aqui eu delimitei a conferência para apenas os eventos que sucedem o evento atual

            if lista[indice][0] == 'R' and lista[indice][1] == amigo:
                contagemPermitida = True

            if contagemPermitida:
                
                tempoDeConversa = tempoDeConversa + 1

                if lista[indice][0] == 'E' and lista[indice][1] == amigo:
                    contagemPermitida = False
                    tempoDeConversa = tempoDeConversa - 1
                
                if lista[indice][0] == 'T':
                    tempoDeConversa = tempoDeConversa + lista[indice][1] - 2

        if contagemPermitida == True: # Se o evento não teve resposta, a saída deve ser "-1"
            tempoDeConversa = -1

        if item[0] != 'T':
            saida.append([amigo, tempoDeConversa])

saida.sort(key=lambda elemento:elemento[0]) # Ordenando a lista de saída para imprimí-la
for s in saida:
    print(s[0],s[1])