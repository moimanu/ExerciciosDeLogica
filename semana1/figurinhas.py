# Aqui acontece a entrada de dados (em uma única string) e sua respectiva tranformação em uma lista de inteiros
def criarLista(comando):
    entrada = input(comando)
    listaEntrada = list(map(int, entrada.split()))
    return listaEntrada

# Condições para a primeira entrada
msgIvalido = ("Valores inválidos, tente outra vez: ")
lista1 = criarLista("Escreva o número de espaços no álbum (1-100), figurinhas carimbadas (menor ou igual a metade) e figurinhas compradas (1-300): ")
while lista1[0] < 1 or lista1[0] > 100 or lista1[1] < 1 or lista1[1] > lista1[0]/2 or lista1[2] < 1 or lista1[2] > 300 or len(lista1) != 3:
    lista1 = criarLista(msgIvalido)

# Condições para a segunda entrada (+ correção para não digitarem carimbadas iguais)
lista2 = criarLista(f"Escreva quais são as figurinhas carimbadas ({lista1[1]}, sem repetir): ")
while lista2[0] < 1 or lista2[0] > 100 or len(lista2) > lista1[1]:
    lista2 = criarLista(msgIvalido)
for n in range(len(lista2)):
    for n2 in range(len(lista2)):
            if n != n2:
                while lista2[n] == lista2[n2] or lista2[n] > lista1[0] or lista2[n2] > lista1[0] or lista2[n] < 1 or lista2[n2] < 1:
                    lista2 = criarLista(msgIvalido)

# Condições para a terceira entrada
lista3 = criarLista(f"Escreva as figurinhas já compradas ({lista1[2]}): ")
while len(lista3) > lista1[2]:
    lista3 = criarLista(msgIvalido)

# Contador de figurinhas carimbadas que faltam encontrar
contador = 0
for x in lista2:
    confere = False
    for y in lista3:
        if x == y:
            confere = True
    if confere:
        contador = contador + 1

print("Número de figurinhas carimbadas que faltam: ",len(lista2)-contador)