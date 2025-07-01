import TELA_Fornecedores

def menu():
    while True:
        print ("1 - Adicionar fornecedor")
        print ("2 - Listar fornecedores")
        print ("3 - Alterar fornecedor")
        print ("4 - Excluir fornecedor")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando fornecedor")
            TELA_Fornecedores.adicionar_fornecedor()

        elif opcao == "2":
            print("Listando fornecedores")
            TELA_Fornecedores.listar_fornecedores()

        elif opcao == "3":
            print("Alterando fornecedor")
            TELA_Fornecedores.alterar_fornecedor()

        elif opcao == "4":
            print("Excluindo fornecedor")
            TELA_Fornecedores.excluir_fornecedor()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()