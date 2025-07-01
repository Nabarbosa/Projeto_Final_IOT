# CRUD em arquivos de texto para gerenciar contatos com informações completas

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("contatos.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])
            return ultimo_id + 1
    except FileNotFoundError:
        return 1

# CREATE - Criar
def create_contato(telefone, email, celular):
    id_contato = gerar_proximo_id()
    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"{id_contato},{telefone},{email},{celular}\n")
    print(f"Contato {id_contato} adicionado com sucesso!")

# UPDATE - Atualizar
def update_contato(id_contato, telefone, email, celular):
    try:
        with open("contatos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("contatos.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_contato:
                    arquivo.write(f"{id_contato},{telefone},{email},{celular}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Contato {id_contato} atualizado com sucesso!")
            else:
                print(f"Contato {id_contato} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum contato cadastrado.")

# DELETE - Deletar
def delete_contato(id_contato):
    try:
        with open("contatos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("contatos.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_contato:
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Contato {id_contato} deletado com sucesso!")
            else:
                print(f"Contato {id_contato} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum contato cadastrado.")

# SEARCH - Pesquisar
def search_contato(id_contato):
    try:
        with open("contatos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_contato:
                    print("\nContato encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Telefone: {dados[1]}")
                    print(f"E-mail: {dados[2]}")
                    print(f"Celular: {dados[3]}")
                    return
            print(f"Contato com ID {id_contato} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum contato cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Contatos ===")
        print("1. Adicionar Contato")
        print("2. Atualizar Contato")
        print("3. Deletar Contato")
        print("4. Pesquisar Contato pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            create_contato(telefone, email, celular)
        elif opcao == "2":
            id_contato = input("ID do Contato a ser atualizado: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo E-mail: ")
            celular = input("Novo Celular: ")
            update_contato(id_contato, telefone, email, celular)
        elif opcao == "3":
            id_contato = input("ID do Contato a ser deletado: ")
            delete_contato(id_contato)
        elif opcao == "4":
            id_contato = input("ID do Contato a ser pesquisado: ")
            search_contato(id_contato)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
