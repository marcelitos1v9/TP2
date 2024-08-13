cf = float(input("digite o valor de fabricação do veiculo: "))

vi = (cf*28)/100

pd = (cf*45)/100

vf = cf+vi+pd

print(f"o valor do veiculo final é R${vf:.2f}")