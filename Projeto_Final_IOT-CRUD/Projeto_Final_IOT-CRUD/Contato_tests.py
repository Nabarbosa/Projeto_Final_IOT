import TELA_Contatos

def menu():
    while True:
        print ("1 - Adicionar contato ")
        print ("2 - Listar contatos")
        print ("3 - Alterar contato")
        print ("4 - Excluir contato")
        print ("0 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando contato")
            TELA_Contatos.adicionar_contato()

        elif opcao == "2":
            print("Listando contatos")
            TELA_Contatos.listar_contatos()

        elif opcao == "3":
            print("Alterando contato")
            TELA_Contatos.alterar_contato()

        elif opcao == "4":
            print("Excluindo contato")
            TELA_Contatos.excluir_contato()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")



menu()