salario = float(input("Digite o valor do salario:"))
pa = float(input("Digite a porcentagem de aumento que o usuario ira receber: "))

aumento = salario +((salario*pa)/100)

print(f"O novo valor que o funcionário ira receber é R${aumento}")