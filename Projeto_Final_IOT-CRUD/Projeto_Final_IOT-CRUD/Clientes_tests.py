import TELA_Clientes

def menu():
    while True:
        print ("1 - Adicionar cliente")
        print ("2 - Listar clientes")
        print ("3 - Alterar cliente")
        print ("4 - Excluir cliente")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando cliente")
            TELA_Clientes.adicionar_cliente()

        elif opcao == "2":
            print("Listando clientes")
            TELA_Clientes.listar_clientes()

        elif opcao == "3":
            print("Alterando cliente")
            TELA_Clientes.alterar_cliente()

        elif opcao == "4":
            print("Excluindo cliente")
            TELA_Clientes.excluir_cliente()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")

menu()