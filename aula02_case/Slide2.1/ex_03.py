print("**************** CÁLCULO DE GRANDEZAS ELÉTRICAS **********")

opcao = int(input("Digite qual grandeza quer calcular:\n1. Tensão (em Volt)\n2. Resistência (em Ohm)\n3. Corrente (em Ampére)\n Selecione a opcão: "))

print("**********************************************************")
match opcao:
    case 1:
        resistencia = float(input("Digite o valor da Resistencia: "))
        corrente = float(input("Digite o valor da corrente: "))
        tensao = resistencia * corrente
        print(f"O valor da tensao é {tensao:2f}")
    case 2:
        tensao = float(input("Digite o valor da Tensão: "))
        corrente = float(input("Digite o valor da corrente: "))
        resistencia = tensao / corrente
        print(f"O valor da resistencia é {resistencia:2f}")
    case 3:
        tensao = float(input("Digite o valor da Tensão: "))
        resistencia = float(input("Digite o valor da resistencia: "))
        corrente = tensao / resistencia
        print(f"O valor da corrente é {corrente:2f}")
