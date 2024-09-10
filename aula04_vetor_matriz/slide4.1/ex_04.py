matriz_numeros = []

for i in range(5):
    linha=[]
    matriz_numeros.append(linha)
    for j in range(2):
        numero = int(input(f"Digite o número da posição({i},{j}) "))
        linha.append(numero)
        
for i in matriz_numeros:
    print(i)