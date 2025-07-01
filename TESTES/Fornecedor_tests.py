import CRUD_Fornecedores

def menu():
    while True:
        print ("1 - Adicionar fornecedor")
        print ("2 - Listar fornecedores")
        print ("3 - Alterar fornecedor")
        print ("4 - Excluir fornecedor")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Fornecedores.create_fornecedor()

        elif opcao == "2":
            print("Listando fornecedores")
            CRUD_Fornecedores.search_fornecedor()

        elif opcao == "3":
            print("Alterando fornecedor")
            CRUD_Fornecedores.update_fornecedor()

        elif opcao == "4":
            print("Excluir fornecedor")
            CRUD_Fornecedores.delete_fornecedor()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()