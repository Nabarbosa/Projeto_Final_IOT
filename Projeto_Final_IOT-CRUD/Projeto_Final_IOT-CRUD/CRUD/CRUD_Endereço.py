# CRUD em arquivos de texto para gerenciar endereços com informações completas

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("enderecos.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])
            return ultimo_id + 1
    except FileNotFoundError:
        return 1

# CREATE - Criar
def create_endereco(logradouro, numero, bairro, cep, cidade, uf, complemento):
    id_endereco = gerar_proximo_id()
    with open("enderecos.txt", "a") as arquivo:
        arquivo.write(f"{id_endereco},{logradouro},{numero},{bairro},{cep},{cidade},{uf},{complemento}\n")
    print(f"Endereço {id_endereco} adicionado com sucesso!")

# UPDATE - Atualizar
def update_endereco(id_endereco, logradouro, numero, bairro, cep, cidade, uf, complemento):
    try:
        with open("enderecos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("enderecos.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_endereco:
                    arquivo.write(f"{id_endereco},{logradouro},{numero},{bairro},{cep},{cidade},{uf},{complemento}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Endereço {id_endereco} atualizado com sucesso!")
            else:
                print(f"Endereço {id_endereco} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum endereço cadastrado.")

# DELETE - Deletar
def delete_endereco(id_endereco):
    try:
        with open("enderecos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("enderecos.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_endereco:
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Endereço {id_endereco} deletado com sucesso!")
            else:
                print(f"Endereço {id_endereco} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum endereço cadastrado.")

# SEARCH - Pesquisar
def search_endereco(id_endereco):
    try:
        with open("enderecos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_endereco:
                    print("\nEndereço encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Logradouro: {dados[1]}")
                    print(f"Número: {dados[2]}")
                    print(f"Bairro: {dados[3]}")
                    print(f"CEP: {dados[4]}")
                    print(f"Cidade: {dados[5]}")
                    print(f"UF: {dados[6]}")
                    print(f"Complemento: {dados[7]}")
                    return
            print(f"Endereço com ID {id_endereco} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum endereço cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Endereços ===")
        print("1. Adicionar Endereço")
        print("2. Atualizar Endereço")
        print("3. Deletar Endereço")
        print("4. Pesquisar Endereço pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            logradouro = input("Logradouro: ")
            numero = input("Número: ")
            bairro = input("Bairro: ")
            cep = input("CEP: ")
            cidade = input("Cidade: ")
            uf = input("UF: ")
            complemento = input("Complemento: ")
            create_endereco(logradouro, numero, bairro, cep, cidade, uf, complemento)
        elif opcao == "2":
            id_endereco = input("ID do Endereço a ser atualizado: ")
            logradouro = input("Novo Logradouro: ")
            numero = input("Novo Número: ")
            bairro = input("Novo Bairro: ")
            cep = input("Novo CEP: ")
            cidade = input("Nova Cidade: ")
            uf = input("Nova UF: ")
            complemento = input("Novo Complemento: ")
            update_endereco(id_endereco, logradouro, numero, bairro, cep, cidade, uf, complemento)
        elif opcao == "3":
            id_endereco = input("ID do Endereço a ser deletado: ")
            delete_endereco(id_endereco)
        elif opcao == "4":
            id_endereco = input("ID do Endereço a ser pesquisado: ")
            search_endereco(id_endereco)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
