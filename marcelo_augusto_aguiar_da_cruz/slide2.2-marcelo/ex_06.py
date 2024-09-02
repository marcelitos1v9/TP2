valor_produto = float(input("Digite o valor do produto"))

if valor_produto < 20:
    valor_final = valor_produto + (valor_produto*0.45)
    print(f"O valor da venda do produto vai ser de R${valor_final}") 
else :
    valor_final = valor_produto + (valor_produto*0.30)
    print(f"O valor da venda do produto vai ser de R${valor_final}")