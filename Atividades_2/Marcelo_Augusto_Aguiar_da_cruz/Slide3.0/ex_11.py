nomes = ["Luiz", "Ana", "Cristina", "Fernanda", "Maria Alice", "Joaquina"]

while True:
    opcao = int(input("Digite 1 para buscar um nome ou 0 para sair: "))
    
    if opcao == 0:
        print("Saindo da aplicação.")
        break
    elif opcao == 1:
        nome_busca = input("Digite o nome que deseja localizar: ")
        encontrado = False
        
        for nome in nomes:
            if nome_busca == nome:
                print(f"Nome {nome} encontrado.")
                encontrado = True
                break
        
        if not encontrado:
            print("Nome não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")
