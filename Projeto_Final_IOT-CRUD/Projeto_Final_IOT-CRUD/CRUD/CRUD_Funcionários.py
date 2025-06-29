# Importações necessárias
from CRUD_Endereço import create_endereco
from CRUD_Contatos import create_contato

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("funcionarios.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

# CREATE - Criar
def create_funcionario(nome, cpf, cargo, dta_nascimento, endereco, contato):
    id_funcionario = gerar_proximo_id()  # Gera o próximo ID automaticamente
    with open("funcionarios.txt", "a") as arquivo:
        arquivo.write(f"{id_funcionario},{nome},{cpf},{cargo},{dta_nascimento},{endereco},{contato}\n")
    print(f"Funcionário {id_funcionario} adicionado com sucesso!")

# UPDATE - Atualizar
def update_funcionario(id_funcionario, nome, cpf, cargo, dta_nascimento, endereco, contato):
    try:
        with open("funcionarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("funcionarios.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_funcionario:  # Verifica pelo ID
                    arquivo.write(f"{id_funcionario},{nome},{cpf},{cargo},{dta_nascimento},{endereco},{contato}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Funcionário {id_funcionario} atualizado com sucesso!")
            else:
                print(f"Funcionário {id_funcionario} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum funcionário cadastrado.")

# DELETE - Deletar
def delete_funcionario(id_funcionario):
    try:
        with open("funcionarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("funcionarios.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_funcionario:  # Verifica pelo ID
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Funcionário {id_funcionario} deletado com sucesso!")
            else:
                print(f"Funcionário {id_funcionario} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum funcionário cadastrado.")

# SEARCH - Pesquisar
def search_funcionario(id_funcionario):
    try:
        with open("funcionarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_funcionario:  # Verifica pelo ID
                    print("\nFuncionário encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Nome: {dados[1]}")
                    print(f"CPF: {dados[2]}")
                    print(f"Cargo: {dados[3]}")
                    print(f"Data de Nascimento: {dados[4]}")
                    print(f"Endereço: {dados[5]}")
                    print(f"Contato: {dados[6]}")
                    return
            print(f"Funcionário com ID {id_funcionario} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum funcionário cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Funcionários ===")
        print("1. Adicionar Funcionário")
        print("2. Atualizar Funcionário")
        print("3. Deletar Funcionário")
        print("4. Pesquisar Funcionário pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cargo = input("Cargo: ")
            dta_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")

            print("\n--- Cadastro de Endereço ---")
            logradouro = input("Logradouro: ")
            numero = input("Número: ")
            bairro = input("Bairro: ")
            cep = input("CEP: ")
            cidade = input("Cidade: ")
            uf = input("UF: ")
            complemento = input("Complemento: ")
            create_endereco(logradouro, numero, bairro, cep, cidade, uf, complemento)
            endereco = f"{logradouro}, {numero}, {bairro}, {cep}, {cidade}, {uf}, {complemento}"

            print("\n--- Cadastro de Contato ---")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            create_contato(telefone, email, celular)
            contato = f"{telefone}, {email}, {celular}"

            create_funcionario(nome, cpf, cargo, dta_nascimento, endereco, contato)
        elif opcao == "2":
            id_funcionario = input("ID do Funcionário a ser atualizado: ")
            nome = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            cargo = input("Novo Cargo: ")
            dta_nascimento = input("Nova Data de Nascimento (DD/MM/AAAA): ")

            print("\n--- Atualização de Endereço ---")
            logradouro = input("Novo Logradouro: ")
            numero = input("Novo Número: ")
            bairro = input("Novo Bairro: ")
            cep = input("Novo CEP: ")
            cidade = input("Nova Cidade: ")
            uf = input("Nova UF: ")
            complemento = input("Novo Complemento: ")
            create_endereco(logradouro, numero, bairro, cep, cidade, uf, complemento)
            endereco = f"{logradouro}, {numero}, {bairro}, {cep}, {cidade}, {uf}, {complemento}"

            print("\n--- Atualização de Contato ---")
            telefone = input("Novo Telefone: ")
            email = input("Novo E-mail: ")
            celular = input("Novo Celular: ")
            create_contato(telefone, email, celular)
            contato = f"{telefone}, {email}, {celular}"

            update_funcionario(id_funcionario, nome, cpf, cargo, dta_nascimento, endereco, contato)
        elif opcao == "3":
            id_funcionario = input("ID do Funcionário a ser deletado: ")
            delete_funcionario(id_funcionario)
        elif opcao == "4":
            id_funcionario = input("ID do Funcionário a ser pesquisado: ")
            search_funcionario(id_funcionario)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
