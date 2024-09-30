preco_pao = 0.54

print("Tabela de Preços de Pães (Somente pares)")
for quantidade in range(2, 51, 2):  
    total = quantidade * preco_pao
    print(f"{quantidade} pães: R$ {total:.2f}")
