import CRUD_Funcionários

def menu():
    while True:
        print ("1 - Adicionar funcionário")
        print ("2 - Listar funcionários")
        print ("3 - Alterar funcionário")
        print ("4 - Excluir funcionário")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Funcionários.create_funcionario()

        elif opcao == "2":
            print("Listando funcionários")
            CRUD_Funcionários.search_funcionario()

        elif opcao == "3":
            print("Alterando funcionário")
            CRUD_Funcionários.update_funcionario()

        elif opcao == "4":
            print("Excluir funcionário")
            CRUD_Funcionários.delete_funcionario()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()