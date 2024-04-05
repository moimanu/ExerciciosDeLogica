entrada1 = list(map(int, input().split())) # <= Definindo a primeira entrada
linhas = entrada1[0]
colunas = entrada1[1]

matriz = [] 
for n in range(linhas): # <= Definindo a segunda entrada
    matriz.append(list(input()))

def bloco_abaixo(): # <= Função para conferir se há bloco abaixo da gota
    for i in range(1, linhas):
        for j in range(colunas):
            if matriz[i-1][j] == "o" and matriz[i][j] == ".":
                matriz[i][j] = "o"
                gota_acima()

def gota_acima(): # <= Função para conferir gota em cima de um bloco
    for i in range(1, linhas):
        for j in range(colunas):
            if matriz[i-1][j] == "o" and matriz[i][j] == "#":
                if j != 0 or j != len(colunas):
                    if matriz[i-1][j-1] != "#":
                        matriz[i-1][j-1] = "o"
                    if matriz[i-1][j+1] != "#":
                        matriz[i-1][j+1] = "o"
                    bloco_abaixo()

gota_acima()
bloco_abaixo()

for linha in matriz: # <= Definindo a saída
    print(''.join(linha))