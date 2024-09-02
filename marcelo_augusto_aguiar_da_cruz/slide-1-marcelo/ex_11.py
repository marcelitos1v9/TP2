# ler a  descricao do produto(nome) a quantidade comprada e o preço unitario .calcular e escrever o total e a descrição do produto

produto = str(input("Digite o nome do produto: "))

qtd = int(input("DIgite a quantidade comprada deste produto: "))

valor = float(input("Digite o valor do produto: "))

vlr_total = qtd*valor

print(f"O valor total pago em {qtd} {produto} é de R${vlr_total:.2f}")

