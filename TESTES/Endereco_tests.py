"""
Nome do arquivo: Endereco_tests.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

import CRUD_Endereço

def menu():
    while True:
        print ("1 - Adicionar endereço")
        print ("2 - Listar endereços")
        print ("3 - Alterar endereço")
        print ("4 - Excluir endereço")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Endereço.create_endereco()

        elif opcao == "2":
            print("Listando endereços")
            CRUD_Endereço.search_endereco()

        elif opcao == "3":
            print("Alterando endereço")
            CRUD_Endereço.update_endereco()

        elif opcao == "4":
            print("Excluir endereço")
            CRUD_Endereço.delete_endereco()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()
