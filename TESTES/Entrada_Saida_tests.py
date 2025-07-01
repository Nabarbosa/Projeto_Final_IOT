"""
Nome do arquivo: Entrada_Saida_tests.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

import CRUD_Registro

def menu():
    while True:
        print ("1 - Adicionar registro")
        print ("2 - Listar registros")
        print ("3 - Alterar registro")
        print ("4 - Excluir registro")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Registro.create_registro()

        elif opcao == "2":
            print("Listando registros")
            CRUD_Registro.search_registro()

        elif opcao == "3":
            print("Alterando registro")
            CRUD_Registro.update_registro()

        elif opcao == "4":
            print("Excluir registro")
            CRUD_Registro.delete_registro()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()
