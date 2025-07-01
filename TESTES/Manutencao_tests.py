import CRUD_Manutenção

def menu():
    while True:
        print ("1 - Adicionar manutenção")
        print ("2 - Listar manutenções")
        print ("3 - Alterar manutenção")
        print ("4 - Excluir manutenção")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Manutenção.create_manutencao()

        elif opcao == "2":
            print("Listando manutenções")
            CRUD_Manutenção.search_manutencao()

        elif opcao == "3":
            print("Alterando manutenção")
            CRUD_Manutenção.update_manutencao()

        elif opcao == "4":
            print("Excluir manutenção")
            CRUD_Manutenção.delete_manutencao()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()