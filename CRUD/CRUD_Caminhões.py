"""
Nome do arquivo: CRUD_Caminhões
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

# CRUD em arquivos de texto para gerenciar caminhões com informações completas

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("caminhoes.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

# CREATE - Criar
def create_caminhao(renavan, modelo, marca, cor, placa, chassi, status, tipo, peso):
    id_caminhao = gerar_proximo_id()  # Gera o próximo ID automaticamente
    with open("caminhoes.txt", "a") as arquivo:
        arquivo.write(f"{id_caminhao},{renavan},{modelo},{marca},{cor},{placa},{chassi},{status},{tipo},{peso}\n")
    print(f"Caminhão {id_caminhao} adicionado com sucesso!")

# UPDATE - Atualizar
def update_caminhao(id_caminhao, renavan, modelo, marca, cor, placa, chassi, status, tipo, peso):
    try:
        with open("caminhoes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("caminhoes.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_caminhao:  # Verifica pelo ID
                    arquivo.write(f"{id_caminhao},{renavan},{modelo},{marca},{cor},{placa},{chassi},{status},{tipo},{peso}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Caminhão {id_caminhao} atualizado com sucesso!")
            else:
                print(f"Caminhão {id_caminhao} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum caminhão cadastrado.")

# DELETE - Deletar
def delete_caminhao(id_caminhao):
    try:
        with open("caminhoes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("caminhoes.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_caminhao:  # Verifica pelo ID
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Caminhão {id_caminhao} deletado com sucesso!")
            else:
                print(f"Caminhão {id_caminhao} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum caminhão cadastrado.")

# SEARCH - Pesquisar
def search_caminhao(id_caminhao):
    try:
        with open("caminhoes.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_caminhao:  # Verifica pelo ID
                    print("\nCaminhão encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Renavan: {dados[1]}")
                    print(f"Modelo: {dados[2]}")
                    print(f"Marca: {dados[3]}")
                    print(f"Cor: {dados[4]}")
                    print(f"Placa: {dados[5]}")
                    print(f"Chassi: {dados[6]}")
                    print(f"Status: {dados[7]}")
                    print(f"Tipo: {dados[8]}")
                    print(f"Peso: {dados[9]}")
                    return
            print(f"Caminhão com ID {id_caminhao} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum caminhão cadastrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Caminhões ===")
        print("1. Adicionar Caminhão")
        print("2. Atualizar Caminhão")
        print("3. Deletar Caminhão")
        print("4. Pesquisar Caminhão pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            renavan = input("Renavan: ")
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            cor = input("Cor: ")
            placa = input("Placa: ")
            chassi = input("Chassi: ")
            status = input("Status: ")
            tipo = input("Tipo: ")
            try:
                peso = float(input("Peso: "))
            except ValueError:
                print("Peso deve ser um número real.")
                continue
            create_caminhao(renavan, modelo, marca, cor, placa, chassi, status, tipo, peso)
        elif opcao == "2":
            id_caminhao = input("ID do Caminhão a ser atualizado: ")
            renavan = input("Novo Renavan: ")
            modelo = input("Novo Modelo: ")
            marca = input("Nova Marca: ")
            cor = input("Nova Cor: ")
            placa = input("Nova Placa: ")
            chassi = input("Novo Chassi: ")
            status = input("Novo Status: ")
            tipo = input("Novo Tipo: ")
            try:
                peso = float(input("Novo Peso: "))
            except ValueError:
                print("Peso deve ser um número real.")
                continue
            update_caminhao(id_caminhao, renavan, modelo, marca, cor, placa, chassi, status, tipo, peso)
        elif opcao == "3":
            id_caminhao = input("ID do Caminhão a ser deletado: ")
            delete_caminhao(id_caminhao)
        elif opcao == "4":
            id_caminhao = input("ID do Caminhão a ser pesquisado: ")
            search_caminhao(id_caminhao)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
