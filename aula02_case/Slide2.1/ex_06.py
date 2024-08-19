peso = float(input("Digite seu peso atual"))

planeta = int(input("Digite qual planeta gostaria de saber seu peso :\n1.Mercurio\n2.Venus\n3.Marte\n4.Júpiter\n5.Saturno"))

match planeta:
    case 1:
        peso_novo = peso * 0.37
        print(f"Seu peso no Mercurio é {peso_novo} kg")
    case 2:
        peso_novo = peso * 0.88
        print(f"Seu peso no Venus é {peso_novo} kg")
    case 3:
        peso_novo = peso * 0.38
        print(f"Seu peso no Marte é {peso_novo} kg")      
    case 4:
        peso_novo = peso * 2.64
        print(f"Seu peso no Júpiter é {peso_novo} kg")
    case 5:
        peso_novo = peso * 1.15
        print(f"Seu peso no Saturno é {peso_novo} kg")
          
              