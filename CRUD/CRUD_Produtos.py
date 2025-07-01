"""
Nome do arquivo: CRUD_Produtos.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("produtos.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

from datetime import datetime

# CREATE - Criar
def create_produto(descricao, tipo, quantidade, validade, observacoes):
    id_produto = gerar_proximo_id()  # Gera o próximo ID automaticamente
    with open("produtos.txt", "a") as arquivo:
        arquivo.write(f"{id_produto},{descricao},{tipo},{quantidade},{validade},{observacoes}\n")
    print(f"Produto {id_produto} adicionado com sucesso!")

# UPDATE - Atualizar
def update_produto(id_produto, descricao, tipo, quantidade, validade, observacoes):
    try:
        with open("produtos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("produtos.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_produto:  # Verifica pelo ID
                    arquivo.write(f"{id_produto},{descricao},{tipo},{quantidade},{validade},{observacoes}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Produto {id_produto} atualizado com sucesso!")
            else:
                print(f"Produto {id_produto} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

# DELETE - Deletar
def delete_produto(id_produto):
    try:
        with open("produtos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("produtos.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_produto:  # Verifica pelo ID
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Produto {id_produto} deletado com sucesso!")
            else:
                print(f"Produto {id_produto} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

# SEARCH - Pesquisar
def search_produto(id_produto):
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_produto:  # Verifica pelo ID
                    print("\nProduto encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Descrição: {dados[1]}")
                    print(f"Tipo: {dados[2]}")
                    print(f"Quantidade: {dados[3]}")
                    print(f"Validade: {dados[4]}")
                    print(f"Observações: {dados[5]}")
                    return
            print(f"Produto com ID {id_produto} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum produto cadastrado.")

# Função para ler data de validade
def input_date(msg):
    while True:
        valor = input(msg)
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Produtos ===")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Deletar Produto")
        print("4. Pesquisar Produto pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            tipo = input("Tipo: ")
            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade deve ser um número inteiro.")
                continue
            validade = input_date("Validade (DD/MM/AAAA): ")
            observacoes = input("Observações: ")
            create_produto(descricao, tipo, quantidade, validade, observacoes)
        elif opcao == "2":
            id_produto = input("ID do Produto a ser atualizado: ")
            descricao = input("Nova Descrição: ")
            tipo = input("Novo Tipo: ")
            try:
                quantidade = int(input("Nova Quantidade: "))
            except ValueError:
                print("Quantidade deve ser um número inteiro.")
                continue
            validade = input_date("Nova Validade (DD/MM/AAAA): ")
            observacoes = input("Novas Observações: ")
            update_produto(id_produto, descricao, tipo, quantidade, validade, observacoes)
        elif opcao == "3":
            id_produto = input("ID do Produto a ser deletado: ")
            delete_produto(id_produto)
        elif opcao == "4":
            id_produto = input("ID do Produto a ser pesquisado: ")
            search_produto(id_produto)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
