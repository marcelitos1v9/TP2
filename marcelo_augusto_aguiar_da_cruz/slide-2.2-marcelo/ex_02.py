metros = float(input("Digite a medida em metros a ser convertida"))

conversao = int(input("Digite a opção que sera convertida\n1.decimetros\n2.centimetos\n3.milimetros"))

match conversao:
    case 1:
        decimetros = metros * 10
        print(f"{metros} metros equivalem a {decimetros} decimetros")
    case 2:
        centimetros = metros * 100
        print(f"{metros} metros equivalem a {centimetros} centimetros")
    case 3:
        milimetros = metros * 1000
        print(f"{metros} metros equivalem a {milimetros} milimetros")
    case _:
        print("Opção invalida")