cat = input("Digite 'A' para calcular 10% \n digite 'B' para calcular 15%\n Digite a opção ")
valor = float(input("Digite o valor: "))

match cat.lower():
    case 'a':
        result = valor*0.1
        print(f"O valor com 10% de desconto é {result:.2f}")
    case 'b':
        result = valor*0.15
        print(f"O valor com 15% de desconto é {result:.2f}")
    case _:
        print("Opção inválida!")
        exit(0)
