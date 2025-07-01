import CRUD_Sensores

def menu():
    while True:
        print ("1 - Adicionar sensor")
        print ("2 - Listar sensores")
        print ("3 - Alterar sensor")
        print ("4 - Excluir sensor")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Sensores.create_sensores()

        elif opcao == "2":
            print("Listando sensores")
            CRUD_Sensores.search_sensores()

        elif opcao == "3":
            print("Alterando sensor")
            CRUD_Sensores.update_sensores()

        elif opcao == "4":
            print("Excluir sensor")
            CRUD_Sensores.delete_sensores()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()