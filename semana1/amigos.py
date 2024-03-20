# Primeira entrada de dados
nPredios = int(input("Digite a quantidade de predios na rua: "))
while nPredios < 2 or nPredios > 2 * (10**5):
    nPredios = int(input("Quantidade não aceita. Digite outro número: "))

# Segunda entrada de dados
print("Digite a quantidade de andares =>")
andaresPorPredio = []
for i in range(nPredios):
    andaresPorPredio.append(int(input(f"Predio { i + 1 }: ")))
    while andaresPorPredio[i] < 1 or andaresPorPredio[i] > 10**9 or andaresPorPredio[i] == "":
        andaresPorPredio[i] = (int(input(f"Digite outra quantidade de andares para o predio { i + 1 }: ")))

#laço para encontrar o maior percurso
maiorPercurso = 0
for primeiro in range(len(andaresPorPredio)):
    for segundo in range(len(andaresPorPredio)):
        
        #aqui eu fiz uma correção para que um predio não seja comparado com ele mesmo
        if segundo != primeiro:
            #aqui eu fiz uma correção para que não hajam distâncias negativas
            distancia = abs(primeiro - segundo)
                
            #aqui eu calculei o percurso completo de cada comparação e "guardei" o maior
            percurso = andaresPorPredio[primeiro] + andaresPorPredio[segundo] + distancia
            if percurso > maiorPercurso:
                maiorPercurso = percurso

print(f"A maior distância entre dois apartamentos é: {maiorPercurso}.")