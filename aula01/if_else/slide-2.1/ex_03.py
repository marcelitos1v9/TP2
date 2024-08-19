altura = float(input("Digite sua altura"))
sexo = int(input("homem-1 \n  mulher - 2 \n1.75"))

if sexo == 1:
    pesoIdeal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {pesoIdeal}")
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {pesoIdeal}")
    
    