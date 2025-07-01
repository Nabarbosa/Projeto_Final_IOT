"""
Nome do arquivo: Clientes_tests.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

import CRUD_Clientes

def menu():
    while True:
        print ("1 - Adicionar cliente")
        print ("2 - Listar clientes")
        print ("3 - Alterar cliente")
        print ("4 - Excluir cliente")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Clientes.create_cliente()

        elif opcao == "2":
            print("Listando clientes")
            CRUD_Clientes.search_cliente()

        elif opcao == "3":
            print("Alterando cliente")
            CRUD_Clientes.update_cliente()

        elif opcao == "4":
            print("Excluir cliente")
            CRUD_Clientes.delete_cliente()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()
