pessoa1 = str(input("Digite a altura da primeira pessoa"))
pessoa2  = str(input("Digite a altura da segunda pessoa"))
pessoa3 = str(input("Digite a altura da terceira pessoa"))

if pessoa1 > pessoa2 and pessoa1 > pessoa3:
    print(f"primeira pessoa é a maior com {pessoa1}")
elif pessoa2 > pessoa3 and pessoa2 > pessoa1 :
    print(f"Segunda pessoa é a maior com {pessoa2}")
else:
    print(f"Terceira pessoa é a maior com {pessoa3}")