n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))

if n1 < n2:
    result = n1/n2
    print(f"A divisão do primeiro numero pelo segundo é {result}")
else:
    result = n2/n1
    print(f"A divisão do segundo numero pelo primeiro é {result}")
    