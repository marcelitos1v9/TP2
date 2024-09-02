n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

op = str(input("Digite qual tipo de operação deseja \n+ Soma \n- Subtração\n* Multiplação \n / Divisão"))

match op:
    case '+':
        result = n1 + n2
        print(f"O resultado da soma é {result}")
    case '-':
        result = n1 - n2
        print(f"O resultado da subtração é {result}")
    case '*':
        result = n1 * n2
        print(f"O resultado da multiplicação é {result}")
    case '/':
        if n2 != 0:
            result = n1 / n2
            print(f"O resultado da divisão é {result}")
        else:
            print("Não é possível realizar a divisão por zero")
    case _:
        print("Operação inválida!")