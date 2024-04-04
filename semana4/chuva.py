qntdColunas = 6
qntdLinhas = 5
matriz = []
for n in range(5):
    matriz.append(list(input()))


def bloco_abaixo():
    for linha in range(1, len(matriz)):
        for coluna in range(qntdColunas):
            if matriz [linha-1] [coluna] == "o" and matriz [linha] [coluna] == ".":
                matriz [linha] [coluna] = "o"
                bloco_acima()

def bloco_acima():
    for linha in range(1, len(matriz)):
        for coluna in range(qntdColunas):
            if matriz [linha-1] [coluna] == "o" and matriz [linha] [coluna] == "#":
                if coluna != 0 or coluna != len(qntdColunas):
                    matriz [linha-1] [coluna-1] = "o"
                    matriz [linha-1] [coluna+1] = "o"
                    bloco_abaixo()

bloco_abaixo()
for linha in matriz:
    print(linha)