validos = int(input("Digite a quantidade de votos validos: "))
brancos = int(input("Digite a quantidade de votos brancos: "))
nulos = int(input("Digite a quantidade de votos nulos: "))

total = validos+brancos+nulos

pcvalidos = ((validos*100)/total)
pcbrancos = ((brancos*100)/total)
pcnulos = ((nulos*100)/total)

print(f"O total de votos é {total} \n o percentual de votos validos foi de {pcvalidos:.2f}% o percentual de votos brancos foi de {pcbrancos:.2f}% o percentual de votos nulos foi de {pcnulos:.2f}%")

