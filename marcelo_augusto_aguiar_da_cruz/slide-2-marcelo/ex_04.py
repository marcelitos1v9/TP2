valor = int(input("Digite um valor positivo: "))

classi = valor % 2 
if valor < 0 :
    print("O valor digitado é negativo")
    exit()
else:
    if classi == 0 :
        novo = valor ** 2
        print(f"O valor digitado é par e seu quadrado é {novo}")
    else:          
        novo = valor ** 3
        print(f"O valor digitado é ímpar e seu cubo é {novo}")