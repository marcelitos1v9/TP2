# Crie um vetor que leia 
# valores inteiros , e mostre os 
# valores armazenados , e 
# mostre quais são pares

tamanho = int(input("Digite o tamanho do vetor"))
vetor = []
vetor_pares=[]

for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número do vetor: "))
    vetor.append(numero)
    if numero % 2 == 0:
        vetor_pares.append(numero)
    
print(f"Vetor: {vetor}")
print(f"Vetor pares: {vetor_pares}")
