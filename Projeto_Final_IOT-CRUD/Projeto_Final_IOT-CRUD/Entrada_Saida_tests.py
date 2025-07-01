import TELA_Entrada_Saida

def menu():
    while True:
        print ("1 - Adicionar registro de entrada/saida")
        print ("2 - Listar registros de entrada/saida")
        print ("3 - Alterar registro de entrada/saida")
        print ("4 - Excluir registro de entrada/saida")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando registro de entrada/saida")
            TELA_Entrada_Saida.adicionar_entrada_saida()

        elif opcao == "2":
            print("Listando registros de entrada/saida")
            TELA_Entrada_Saida.listar_entrada_saida()

        elif opcao == "3":
            print("Alterando registro de entrada/saida")
            TELA_Entrada_Saida.alterar_entrada_saida()

        elif opcao == "4":
            print("Excluindo registro de entrada/saida")
            TELA_Entrada_Saida.excluir_entrada_saida()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()