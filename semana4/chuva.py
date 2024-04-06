entrada1 = list(map(int, input().split())) # <= Definindo a primeira entrada
linhas = entrada1[0]
colunas = entrada1[1]

matriz = [] 
for n in range(linhas): # <= Definindo a segunda entrada
    matriz.append(list(input()))

def gota_acima(): # <= Função para conferir gota em cima de um bloco
    if matriz[i-1][j] == "o" and matriz[i][j] == "#":
        matriz[i-1][j-1] = "o"
        matriz[i-1][j+1] = "o"

def bloco_abaixo(): # <= Função para conferir se há bloco abaixo da gota
    if matriz[i-1][j] == "o" and matriz[i][j] == ".":
        matriz[i][j] = "o"

for coluna in range(colunas): # <= Conferindo as linhas "n" vezes, em que "n" representa o número de colunas
    for i in range(1, linhas):
        for j in range(colunas):
            gota_acima()
            bloco_abaixo()

for linha in matriz: # <= Definindo a saída
    print(''.join(linha))
