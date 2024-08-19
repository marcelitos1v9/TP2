salario = float(input("Digite o salario atual: "))
cat = str(input("Digite a categoria pertencente A,B ou C: \n"))

match cat.lower() :
    case 'a':
        novo_salario = salario + (salario*0.10)
        print(f"Seu salario atual é de {salario} e passara a ser {novo_salario}")
    case 'b':
        novo_salario = salario + (salario*0.15)
        print(f"Seu salario atual é de {salario} e passara a ser {novo_salario}")
    case 'c':
        novo_salario = salario + (salario*0.25)
        print(f"Seu salario atual é de {salario} e passara a ser {novo_salario}")
    case _:
        print("Categoria invalida")

          