import os 
os.system("cls")
numero = int(input("1,2,3 - Categoria A \n 4,5,6 - Categoria B \n Escolha um numero: "))

match numero:
    case 1|2|3:
        print("Voce escolheu a categoria A")
    case 4|5|6:
        print("Voce escolheu a categoria B")
    case _:
        print("Escolha invalida")
        
        
        
    