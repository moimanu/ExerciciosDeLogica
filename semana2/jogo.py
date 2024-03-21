# Restrições para as entradas =>
numero = int(input())
while numero>10000 or numero <0:
    numero = int(input("Valor inválido, digite outro número: "))

# Resolução do problema =>
def soma (n):
    if n==1:
        return 1
    else: 
        return n + soma(n-1)
total = soma(numero+1)
print(total)