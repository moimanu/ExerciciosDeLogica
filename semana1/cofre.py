def criarLista(comando):
    entrada = input(comando)
    listaEntrada = list(map(int, entrada.split()))
    return listaEntrada

msgIvalido = ("Valores inválidos, tente outra vez: \n")

entrada1 = criarLista("Escreva a quantidade de números no cofre e a quantidade de posicoes da sequencia: \n")
for i in range(2):
    while len(entrada1) != 2 or entrada1[i] < 2 or entrada1[i] > 10**5:
        entrada1 = criarLista(msgIvalido)

entrada2 = criarLista("Escreva cada número do cofre: \n")
for i in range(entrada1[0]):
    while len(entrada2) != entrada1[0] or entrada2[i] < 0 or entrada2[i] > 9:
        entrada2 = criarLista(msgIvalido)

entrada3 = criarLista("Escreva cada número da sequência de posições: \n")
for i in range(entrada1[1]):
    while len(entrada3) != entrada1[1] or entrada3[i] < 1 or entrada3[i] > entrada1[0] or entrada3[0] != 1:
        entrada3 = criarLista(msgIvalido)
    # Aqui, comecei um laço a partir do indice 1 para poder comparar se há posições consecutivas iguais 
    for i in range(1, entrada1[1]):
        while entrada3[i] == entrada3[i-1]:
            entrada3 = criarLista(msgIvalido)

saida = []
for r in range(10):
    # Aqui tá certinho uma lista temporária que vai de um índice ao outro.
    listaTemp = []
    for i in range(1, len(entrada3)):

        if i == 1:
            if entrada3[i-1]<entrada3[i]:
                for y in range(entrada3[i-1], entrada3[i]+1):
                    listaTemp.append(entrada2[y-1])

            if entrada3[i-1]>entrada3[i]:
                for y in range(entrada3[i], entrada3[i-1]+1):
                    listaTemp.append(entrada2[y-1])
        
        if i != 1:
            if entrada3[i-1]<entrada3[i]:
                for y in range(entrada3[i-1]+1, entrada3[i]+1):
                    listaTemp.append(entrada2[y-1])

            if entrada3[i-1]>entrada3[i]:
                for y in range(entrada3[i], entrada3[i-1]):
                    listaTemp.append(entrada2[y-1])     
    # Fim da criação da lista temp
    
    contador = 0
    for t in listaTemp:
        if r==t:
            contador=contador+1
    saida.append(contador)

print("Quantidade de vezes que os numéros do 0 ao 9 aparecem: ")
for n in saida:
    print(n,end=" ")