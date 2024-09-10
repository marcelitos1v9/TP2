linhas = int(input("Digite a quantidade de linhas que tera na matriz: "))
colunas = int(input("Digite a quantidade de colunas na matriz: "))

matriz_numeros = []

for i in range(linhas):
    linha=[]
    matriz_numeros.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o número da posição({i},{j}) "))
        linha.append(numero)
        
for i in matriz_numeros:
    print(i)