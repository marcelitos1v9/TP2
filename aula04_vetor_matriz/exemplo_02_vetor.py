# vetor = [10,40,70,64,23,75,12,75]

tamanho = int(input("Digite o tamanho do vetor: "))
vetor=[]

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento do vetor {i+1}ºdo vetor "))
    vetor.append(elemento)
print(f"Vetor {vetor}")