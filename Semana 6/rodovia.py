entrada1 = int(input()) # <= Primeira entrada (quantidade de cidades)

matriz=[]
for n in range(entrada1):
    matriz.append(list(map(int, input().split()))) # <= Matriz com os pontos A e B

grafo = {}
for n in matriz: 
    grafo [n[0]] = n[1] # <= Relação entre os pontos A e B

cidadeAtual = matriz[0][0]
conferenciaAtiva = True

while conferenciaAtiva: # <= Laço para conferir se existe um caminho que liga todos os pontos
    if cidadeAtual in grafo:
        novaCidade = grafo[cidadeAtual]
        del grafo[cidadeAtual]
        cidadeAtual = novaCidade
    elif len(grafo) == 0:
        conferenciaAtiva = False
        print("S")
    else:
        conferenciaAtiva = False
        print("N")

# RESUMO
# Passo 1) Receber as entradas e armazenar os pares de cidades em uma lista;
# Passo 2) Converter a lista em um dicionário;
# Passo 3) Começar a conferir, a partir da primeira cidade, se ela está presente no dicionário;
# Passo 4) Se ela estiver, eu atualizo a cidade a ser conferida pela cidade vizinha e apago a chave em questão;
# Passo 5) Se chegar o momento de não encontrar mais chaves no dicionário, retorna "S";
# Passo 6) Se chegar o momento de não encontrar a cidade e ainda ter chaves, retorna "N".