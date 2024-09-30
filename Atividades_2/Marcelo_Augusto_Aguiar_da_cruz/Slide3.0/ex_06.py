preco_item = 1.99

for quantidade in range(1, 51):
    total = quantidade * preco_item
    print(f"{quantidade} itens - R$ {total:.2f}")
