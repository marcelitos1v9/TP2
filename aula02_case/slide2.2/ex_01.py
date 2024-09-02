ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o seu ano de nascimento"))

idade = ano_atual - ano_nasc

if idade < 16:
    print(f"Você nao pode votar ainda pois tem {idade} anos")
else:
    print(f"Você ja pode votar pois possui {idade} anos")