"""
Nome do arquivo: CRUD_Sensores.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

# CRUD em arquivos de texto para gerenciar sensores com informações completas

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("sensores.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])
            return ultimo_id + 1
    except FileNotFoundError:
        return 1

# CREATE - Criar
def create_sensores(temperatura, luminosidade, gas, presenca):
    id_sensores = gerar_proximo_id()
    with open("sensores.txt", "a") as arquivo:
        arquivo.write(f"{id_sensores},{temperatura},{luminosidade},{gas},{presenca}\n")
    print(f"Sensores {id_sensores} adicionados com sucesso!")

# SEARCH - Pesquisar
def search_sensores(id_sensores):
    try:
        with open("sensores.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_sensores:
                    print("\nSensores encontrados:")
                    print(f"ID: {dados[0]}")
                    print(f"Temperatura: {dados[1]}")
                    print(f"Luminosidade: {dados[2]}")
                    print(f"Gás: {dados[3]}")
                    print(f"Presença: {dados[4]}")
                    return
            print(f"Sensores com ID {id_sensores} não encontrados.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum sensor cadastrado.")

# Função para converter entrada booleana
def input_bool(msg):
    while True:
        valor = input(msg + " (s/n): ").strip().lower()
        if valor in ["s", "sim"]:
            return True
        elif valor in ["n", "nao", "não"]:
            return False
        else:
            print("Digite 's' para Sim ou 'n' para Não.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Sensores ===")
        print("1. Adicionar Sensores")
        print("2. Pesquisar Sensores pelo ID")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                temperatura = float(input("Temperatura: "))
                luminosidade = float(input("Luminosidade: "))
            except ValueError:
                print("Temperatura e luminosidade devem ser números reais.")
                continue
            gas = input_bool("Gás detectado?")
            presenca = input_bool("Presença detectada?")
            create_sensores(temperatura, luminosidade, gas, presenca)
        elif opcao == "2":
            id_sensores = input("ID dos Sensores a ser pesquisado: ")
            search_sensores(id_sensores)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
