qntdN = int(input())
lista = []
for n in range(qntdN):
    lista.append(int(input()))
    if lista[len(lista)-1] == 0:
        lista.pop()
        lista.pop()
soma = 0
for n in lista:
    soma += n
print(soma)