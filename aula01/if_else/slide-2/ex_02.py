nome1 = str(input("Digite o nome da primeira pessoa"))
peso1 = float(input(f"Digite o peso de ${nome1}"))

nome2 = str(input("Digite o nome da segunda pessoa"))
peso2 = float(input("Digite o peso de ${nome}"))

if peso1 == peso2:
    print(f"${nome1} e ${nome2} tem o mesmo peso")
elif peso1 < peso2:
    print(f"${nome1} é mais pesado que ${nome2}")
else:
    print(f"${nome2} é mais pesado que ${nome1}")
    
    
