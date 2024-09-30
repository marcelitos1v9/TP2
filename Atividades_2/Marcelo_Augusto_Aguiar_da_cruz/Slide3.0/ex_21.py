funcionarios = []
contador = 0

while contador < 15:
    nome = input(f"Digite o nome do {contador+1}º funcionário: ")
    sexo = input(f"Digite o sexo do {contador+1}º funcionário (M/F): ").upper()

    if sexo == "M":
        funcionarios.append((nome, "Necessita fazer o exame"))
        contador += 1
    elif sexo == "F":
        funcionarios.append((nome, "Não necessita fazer o exame"))
        contador += 1
    else:
        print("Sexo digitado incorretamente. Tente novamente.")

print("\nResultado:")
for nome, exame in funcionarios:
    print(f"{nome}: {exame}")
