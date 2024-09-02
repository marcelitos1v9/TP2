# Solicitando as alturas e convertendo para float
pessoa1 = float(input("Digite a altura da primeira pessoa: "))
pessoa2 = float(input("Digite a altura da segunda pessoa: "))
pessoa3 = float(input("Digite a altura da terceira pessoa: "))

# Comparando as alturas para determinar a ordem
if pessoa1 >= pessoa2 and pessoa1 >= pessoa3:
    if pessoa2 >= pessoa3:
        print(f"1º: Primeira pessoa com {pessoa1} metros")
        print(f"2º: Segunda pessoa com {pessoa2} metros")
        print(f"3º: Terceira pessoa com {pessoa3} metros")
    else:
        print(f"1º: Primeira pessoa com {pessoa1} metros")
        print(f"2º: Terceira pessoa com {pessoa3} metros")
        print(f"3º: Segunda pessoa com {pessoa2} metros")
elif pessoa2 >= pessoa1 and pessoa2 >= pessoa3:
    if pessoa1 >= pessoa3:
        print(f"1º: Segunda pessoa com {pessoa2} metros")
        print(f"2º: Primeira pessoa com {pessoa1} metros")
        print(f"3º: Terceira pessoa com {pessoa3} metros")
    else:
        print(f"1º: Segunda pessoa com {pessoa2} metros")
        print(f"2º: Terceira pessoa com {pessoa3} metros")
        print(f"3º: Primeira pessoa com {pessoa1} metros")
else:
    if pessoa1 >= pessoa2:
        print(f"1º: Terceira pessoa com {pessoa3} metros")
        print(f"2º: Primeira pessoa com {pessoa1} metros")
        print(f"3º: Segunda pessoa com {pessoa2} metros")
    else:
        print(f"1º: Terceira pessoa com {pessoa3} metros")
        print(f"2º: Segunda pessoa com {pessoa2} metros")
        print(f"3º: Primeira pessoa com {pessoa1} metros")
