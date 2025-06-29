# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("fornecedores.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

# CREATE - Criar
def create_fornecedor(cnpj, razao_social, nome_fantasia, area_atuacao, endereco, contato, produto):
    id_fornecedor = gerar_proximo_id()  # Gera o próximo ID automaticamente
    with open("fornecedores.txt", "a") as arquivo:
        arquivo.write(f"{id_fornecedor},{cnpj},{razao_social},{nome_fantasia},{area_atuacao},{endereco},{contato},{produto}\n")
    print(f"Fornecedor {id_fornecedor} adicionado com sucesso!")

# UPDATE - Atualizar
def update_fornecedor(id_fornecedor, cnpj, razao_social, nome_fantasia, area_atuacao, endereco, contato, produto):
    try:
        with open("fornecedores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("fornecedores.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_fornecedor:  # Verifica pelo ID
                    arquivo.write(f"{id_fornecedor},{cnpj},{razao_social},{nome_fantasia},{area_atuacao},{endereco},{contato},{produto}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Fornecedor {id_fornecedor} atualizado com sucesso!")
            else:
                print(f"Fornecedor {id_fornecedor} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum fornecedor cadastrado.")

# DELETE - Deletar
def delete_fornecedor(id_fornecedor):
    try:
        with open("fornecedores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("fornecedores.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_fornecedor:  # Verifica pelo ID
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Fornecedor {id_fornecedor} deletado com sucesso!")
            else:
                print(f"Fornecedor {id_fornecedor} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum fornecedor cadastrado.")

# SEARCH - Pesquisar
def search_fornecedor(id_fornecedor):
    try:
        with open("fornecedores.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_fornecedor:  # Verifica pelo ID
                    print("\nFornecedor encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"CNPJ: {dados[1]}")
                    print(f"Razão Social: {dados[2]}")
                    print(f"Nome Fantasia: {dados[3]}")
                    print(f"Área de Atuação: {dados[4]}")
                    print(f"Endereço: {dados[5]}")
                    print(f"Contato: {dados[6]}")
                    print(f"Produto: {dados[7]}")
                    return
            print(f"Fornecedor com ID {id_fornecedor} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum fornecedor cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Fornecedores ===")
        print("1. Adicionar Fornecedor")
        print("2. Atualizar Fornecedor")
        print("3. Deletar Fornecedor")
        print("4. Pesquisar Fornecedor pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cnpj = input("CNPJ: ")
            razao_social = input("Razão Social: ")
            nome_fantasia = input("Nome Fantasia: ")
            area_atuacao = input("Área de Atuação: ")
            endereco = input("Endereço: ")  # Importa enum
            contato = input("Contato: ")  # Importa enum
            produto = input("Produto: ")  # Importa enum
            create_fornecedor(cnpj, razao_social, nome_fantasia, area_atuacao, endereco, contato, produto)
        elif opcao == "2":
            id_fornecedor = input("ID do Fornecedor a ser atualizado: ")
            cnpj = input("Novo CNPJ: ")
            razao_social = input("Nova Razão Social: ")
            nome_fantasia = input("Novo Nome Fantasia: ")
            area_atuacao = input("Nova Área de Atuação: ")
            endereco = input("Novo Endereço: ")  # Importa enum
            contato = input("Novo Contato: ")  # Importa enum
            produto = input("Novo Produto: ")  # Importa enum
            update_fornecedor(id_fornecedor, cnpj, razao_social, nome_fantasia, area_atuacao, endereco, contato, produto)
        elif opcao == "3":
            id_fornecedor = input("ID do Fornecedor a ser deletado: ")
            delete_fornecedor(id_fornecedor)
        elif opcao == "4":
            id_fornecedor = input("ID do Fornecedor a ser pesquisado: ")
            search_fornecedor(id_fornecedor)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()