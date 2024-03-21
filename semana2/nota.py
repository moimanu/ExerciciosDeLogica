ent1 = int(input())
ent2 = int(input())

g = max(ent1,ent2)
p = min(ent1,ent2)
h = 70
b = 160
aTotal = h*b
aEsquerda = (p*h)+((((g-p)*h)/2))
if aEsquerda == aTotal/2:
    print(0)
elif aEsquerda > aTotal/2:
    print(1)
else:
    print(2)