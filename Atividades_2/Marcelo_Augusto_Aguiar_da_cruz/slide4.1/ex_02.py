tamanho = int(input("Digite a quantidade de times a ser adicionado: "))
vetor = []

for i in range(tamanho):
    time = str(input(f"Digite o {i+1}º time armazenado: "))
    vetor.append(time)

print(f"Times {vetor}")

