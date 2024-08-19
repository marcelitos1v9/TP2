situacao = int(input("Digite a situação de poluição atual entre 0 a 10"))

match situacao.lower():
    case 0|1|2:
        print("Aceitavel")
    case 3|4|5:
        print("Suspender Atividades do grupo 1")
    case 6|7:
        print("Suspender Atividades do grupo 1 e 2")
    case _:
        print("Suspender Atividades do grupo 1, 2 e 3")
        
            

