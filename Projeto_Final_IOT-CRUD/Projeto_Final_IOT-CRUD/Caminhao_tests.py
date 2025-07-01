import TELA_Caminhões

def menu():
    while True:
        print ("1 - Adicionar caminhão")
        print ("2 - Listar caminhões")
        print ("3 - Alterar caminhão")
        print ("4 - Excluir caminhão")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            TELA_Caminhões.adicionar_caminhao()

        elif opcao == "2":
            print("Listando estoque")
            TELA_Caminhões.listar_caminhoes()

        elif opcao == "3":
            print("Alterando item")
            TELA_Caminhões.alterar_caminhao()

        elif opcao == "4":
            print("Excluir item")
            TELA_Caminhões.excluir_caminhao()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()