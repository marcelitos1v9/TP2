nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

# estrutura condicional if

if media >= 6:
    print("Aprovado")
elif media >=2 and media < 6:
    print("Recuperacao")
else:
    print("Reprovado")