print("Responda 1 para sim 0 para não \n Empréstimo")
negativo = int(input("Possui o nome negativo? "))

if negativo == 1:
    print("Empréstimo Negado")
else:
    carteirAss = int(input("Possui carteira assinada? "))
    if carteirAss == 0:
        print("Empréstimo Negado")
    else:
        casaProprias = int(input("Possui casa própria? "))
        if casaProprias == 0:
            print("Empréstimo Negado")
        else:
            print("Empréstimo Aprovado")