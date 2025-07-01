import TELA_Endereco

def menu():
    while True:
        print ("1 - Adicionar endereco")
        print ("2 - Listar enderecos")
        print ("3 - Alterar endereco")
        print ("4 - Excluir endereco")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando endereco")
            TELA_Endereco.adicionar_endereco()

        elif opcao == "2":
            print("Listando enderecos")
            TELA_Endereco.listar_enderecos()

        elif opcao == "3":
            print("Alterando endereco")
            TELA_Endereco.alterar_endereco()

        elif opcao == "4":
            print("Excluindo endereco")
            TELA_Endereco.excluir_endereco()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()