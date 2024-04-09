venceu = 0
for p in range(6):
    if input() == 'V':
        venceu += 1

if venceu >= 5:
    print(1)
elif venceu >= 3:
    print(2)
elif venceu >= 1:
    print(3)
else:
    print(-1)