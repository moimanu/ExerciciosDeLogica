# Restrições para as entradas =>
ent1 = int(input())
while ent1<0 or ent1>160:
    ent1 = int(input("Valor inválido, tente outro: "))
ent2 = int(input())
while ent2<0 or ent2>160:
    ent1 = int(input("Valor inválido, tente outro: "))

# Resolução do problema =>
g = max(ent1,ent2)
p = min(ent1,ent2)
h = 70
b = 160
aTotal = h*b
aEsquerda = p*h+(((g-p)**2)/2)
if aEsquerda == aTotal/2:
    print(0)
elif aEsquerda < aTotal/2:
    print(1)
else:
    print(2)