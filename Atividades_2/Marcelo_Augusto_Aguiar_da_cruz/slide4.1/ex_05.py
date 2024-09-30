matriz = []
contagem_maiores_que_10 = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        if valor > 10:
            contagem_maiores_que_10 += 1
    matriz.append(linha)

print(f"\nA matriz possui {contagem_maiores_que_10} valores maiores que 10.")
