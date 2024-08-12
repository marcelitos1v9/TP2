valor = float(input("Qual o valor da parcela em atraso: "))
juros = float(input("Qual a porcentagem de juros: "))
tempo = int(input("Quantos meses esta em atraso?: "))

vl_atra = valor+(valor*(juros/100)*tempo)

print(f"O valor a ser pago em atraso é ${vl_atra}")


