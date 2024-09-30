nomes = []

for i in range(7):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("\nNomes armazenados e suas posições:")
for i, nome in enumerate(nomes):
    print(f"Posição {i}: {nome}")
