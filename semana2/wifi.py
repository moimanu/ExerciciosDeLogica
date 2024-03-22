nSalas = int((input()))
ldl = []
for n in range(nSalas):
    ldl.append(list(map(int, input().split())))

contador = 0
for x in range(len(ldl)):
    ehOMenor = True
    for y in range(len(ldl)):
        if x!=y:
            if ldl[x][0]<ldl[y][0] and ldl[x][1]>ldl[y][1] and ldl[x][2]>ldl[y][2] and ldl[x][3]<ldl[y][3]:
                ehOMenor = False
                break
    if ehOMenor:
        contador = contador + 1
print(contador)