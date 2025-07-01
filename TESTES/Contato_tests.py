import CRUD_Contatos

def menu():
    while True:
        print ("1 - Adicionar contato")
        print ("2 - Listar contatos")
        print ("3 - Alterar contato")
        print ("4 - Excluir contato")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Contatos.create_contato()

        elif opcao == "2":
            print("Listando contatos")
            CRUD_Contatos.search_contato()

        elif opcao == "3":
            print("Alterando contato")
            CRUD_Contatos.update_contato()

        elif opcao == "4":
            print("Excluir contato")
            CRUD_Contatos.delete_contato()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()