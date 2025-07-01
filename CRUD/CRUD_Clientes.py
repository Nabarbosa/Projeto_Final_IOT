"""
Nome do arquivo: CRUD_Clientes.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

# Importações necessárias
from CRUD_Endereço import create_endereco
from CRUD_Contatos import create_contato

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("clientes.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

# CREATE - Criar
def create_cliente(tipo, nome, cpf, cnpj, observacoes, endereco, contato):
    id_cliente = gerar_proximo_id()  # Gera o próximo ID automaticamente
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{id_cliente},{tipo},{nome},{cpf},{cnpj},{observacoes},{endereco},{contato}\n")
    print(f"Cliente {id_cliente} adicionado com sucesso!")

# UPDATE - Atualizar
def update_cliente(id_cliente, tipo, nome, cpf, cnpj, observacoes, endereco, contato):
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("clientes.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_cliente:  # Verifica pelo ID
                    arquivo.write(f"{id_cliente},{tipo},{nome},{cpf},{cnpj},{observacoes},{endereco},{contato}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Cliente {id_cliente} atualizado com sucesso!")
            else:
                print(f"Cliente {id_cliente} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum cliente cadastrado.")

# DELETE - Deletar
def delete_cliente(id_cliente):
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("clientes.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_cliente:  # Verifica pelo ID
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Cliente {id_cliente} deletado com sucesso!")
            else:
                print(f"Cliente {id_cliente} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum cliente cadastrado.")

# SEARCH - Pesquisar
def search_cliente(id_cliente):
    try:
        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_cliente:  # Verifica pelo ID
                    print("\nCliente encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Tipo: {dados[1]}")
                    print(f"Nome: {dados[2]}")
                    print(f"CPF: {dados[3]}")
                    print(f"CNPJ: {dados[4]}")
                    print(f"Observações: {dados[5]}")
                    print(f"Endereço: {dados[6]}")
                    print(f"Contato: {dados[7]}")
                    return
            print(f"Cliente com ID {id_cliente} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum cliente cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Clientes ===")
        print("1. Adicionar Cliente")
        print("2. Atualizar Cliente")
        print("3. Deletar Cliente")
        print("4. Pesquisar Cliente pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Tipo: ")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cnpj = input("CNPJ: ")
            observacoes = input("Observações: ")

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

            create_cliente(tipo, nome, cpf, cnpj, observacoes, endereco, contato)

        elif opcao == "2":
            id_cliente = input("ID do Cliente a ser atualizado: ")
            tipo = input("Novo Tipo: ")
            nome = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            cnpj = input("Novo CNPJ: ")
            observacoes = input("Novas Observações: ")

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

            update_cliente(id_cliente, tipo, nome, cpf, cnpj, observacoes, endereco, contato)

        elif opcao == "3":
            id_cliente = input("ID do Cliente a ser deletado: ")
            delete_cliente(id_cliente)
        elif opcao == "4":
            id_cliente = input("ID do Cliente a ser pesquisado: ")
            search_cliente(id_cliente)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
