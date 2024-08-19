num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    exit()
elif num1 >num2 and num1 >num3:
    print(f"O primeiro numero é o maior")
elif num2 >num3 and num2 >num3:
    print(f"O segundo numero é o maior")
elif num3 >num1 and num3 >num2:
    print(f"O terceiro numero é o maior")