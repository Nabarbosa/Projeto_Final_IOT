import CRUD_Caminhões

def menu():
    while True:
        print ("1 - Adicionar caminhão")
        print ("2 - Listar caminhões")
        print ("3 - Alterar caminhão")
        print ("4 - Excluir caminhão")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Caminhões.create_caminhao()

        elif opcao == "2":
            print("Listando caminhão")
            CRUD_Caminhões.search_caminhao()

        elif opcao == "3":
            print("Alterando caminhão")
            CRUD_Caminhões.update_caminhao()

        elif opcao == "4":
            print("Excluir caminhão")
            CRUD_Caminhões.delete_caminhao()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()