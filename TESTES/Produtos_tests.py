"""
Nome do arquivo: Produtos_tests.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

import CRUD_Produtos

def menu():
    while True:
        print ("1 - Adicionar produto")
        print ("2 - Listar produtos")
        print ("3 - Alterar produto")
        print ("4 - Excluir produto")
        print ("5 - Sair")
        opcao = input ("Digite sua opcao: ")
        if opcao == "1":
            print("Adicionando item")
            CRUD_Produtos.create_produto()

        elif opcao == "2":
            print("Listando produtos")
            CRUD_Produtos.search_produto()

        elif opcao == "3":
            print("Alterando produto")
            CRUD_Produtos.update_produto()

        elif opcao == "4":
            print("Excluir produto")
            CRUD_Produtos.delete_produto()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")

menu()
