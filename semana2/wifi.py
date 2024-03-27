m = []
for n in range(int((input()))):
    m.append(list(map(int, input().split())))

contador = 0
for x in range(len(m)):
    for y in range(len(m)):
            if m[x][0]<m[y][0] and m[x][1]>m[y][1] and m[x][2]>m[y][2] and m[x][3]<m[y][3]:
                contador = contador + 1
                break
print(len(m)-contador)
