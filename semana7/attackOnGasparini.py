entrada1 = list(map(int, input().split()))
entrada2 = list(input())
entrada3 = list(map(int, input().split()))

muros = [entrada1[1]]

for titan in entrada2:
    if titan =='P':
        titan = entrada3[0]
    elif titan =='M':
        titan = entrada3[1]
    elif titan =='G':
        titan = entrada3[2]
    for n in range(len(muros)):
        if titan <= muros[n]:
            muros[n] -= titan
        elif n == len(muros)-1:
            muros.append(entrada1[1]-titan)

print(len(muros))