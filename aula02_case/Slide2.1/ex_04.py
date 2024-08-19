valor = float(input("Digite o valor da compra: "))

pagamento = int(input("Digite a forma de pagamento:\n 1. A vista em especie\n 2. Cartão de débito\n 3. Cartão de Credito(vencimento)\n"))

match pagamento:
    case 1:
        valor_pagamento = valor - (valor*0.15)
        print(f"O valor a ser pago com o desconto de 15% é R${valor_pagamento}")
    case 2:
        valor_pagamento = valor - (valor*0.10)
        print(f"O valor a ser pago com o desconto de 10% é R${valor_pagamento}")
    case 3:
        valor_pagamento = valor - (valor*0.05)
        print(f"O valor a ser pago com o desconto de 5% é R${valor_pagamento}")
    case _:
        print("Opção inválida!")
                