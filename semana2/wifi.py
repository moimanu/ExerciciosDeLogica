# Função para transformar a entrada em uma lista com inteiros =>
def criarLista():
    entrada = input()
    listaEntrada = list(map(int, entrada.split()))
    return listaEntrada

# Entrada de dados =>
nSalas = int((input()))
ldl = []
for n in range(nSalas):
    ldl.append(criarLista())

contador = 0

print(contador)
print(ldl)