#solicitar um numero ao usuario 

numero = int(input("Digite um numero: "))
i = 0
while i <= numero:
    if i % 2 == 0:
        print(i)
        i += 1