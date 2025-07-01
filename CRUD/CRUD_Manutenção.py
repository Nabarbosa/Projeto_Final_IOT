"""
Nome do arquivo: CRUD_Manutenção.py
Equipe: Clara, Rayanne e Tainá
Turma: G91164
Semestre: 2025.1
"""

# Importações necessárias
from CRUD_Caminhões import search_caminhao
from CRUD_Funcionários import search_funcionario
from CRUD_Produtos import search_produto
from datetime import datetime

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("manutencoes.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])
            return ultimo_id + 1
    except FileNotFoundError:
        return 1

# CREATE - Criar
def create_manutencao(data_ingresso, data_saida, caminhao, mecanico, pecas):
    id_manutencao = gerar_proximo_id()
    with open("manutencoes.txt", "a") as arquivo:
        arquivo.write(f"{id_manutencao},{data_ingresso},{data_saida},{caminhao},{mecanico},{pecas}\n")
    print(f"Manutenção {id_manutencao} adicionada com sucesso!")

# UPDATE - Atualizar
def update_manutencao(id_manutencao, data_ingresso, data_saida, caminhao, mecanico, pecas):
    try:
        with open("manutencoes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("manutencoes.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_manutencao:
                    arquivo.write(f"{id_manutencao},{data_ingresso},{data_saida},{caminhao},{mecanico},{pecas}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Manutenção {id_manutencao} atualizada com sucesso!")
            else:
                print(f"Manutenção {id_manutencao} não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhuma manutenção cadastrada.")

# DELETE - Deletar
def delete_manutencao(id_manutencao):
    try:
        with open("manutencoes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("manutencoes.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_manutencao:
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Manutenção {id_manutencao} deletada com sucesso!")
            else:
                print(f"Manutenção {id_manutencao} não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhuma manutenção cadastrada.")

# SEARCH - Pesquisar
def search_manutencao(id_manutencao):
    try:
        with open("manutencoes.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_manutencao:
                    print("\nManutenção encontrada:")
                    print(f"ID: {dados[0]}")
                    print(f"Data de Ingresso: {dados[1]}")
                    print(f"Data de Saída: {dados[2]}")
                    print(f"Caminhão (ID): {dados[3]}")
                    print(f"Mecânico (ID): {dados[4]}")
                    print(f"Peças (ID): {dados[5]}")
                    return
            print(f"Manutenção com ID {id_manutencao} não encontrada.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhuma manutenção cadastrada.")

# Função para ler datas
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
        print("\n=== CRUD Manutenções ===")
        print("1. Adicionar Manutenção")
        print("2. Atualizar Manutenção")
        print("3. Deletar Manutenção")
        print("4. Pesquisar Manutenção pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            manutencao = {}
            manutencao["data_ingresso"] = input_date("Data de Ingresso (DD/MM/AAAA): ")
            manutencao["data_saida"] = input_date("Data de Saída (DD/MM/AAAA): ")
            manutencao["caminhao"] = input("Caminhão (ID do Caminhão): ")
            if not search_caminhao(manutencao["caminhao"]):
                print("Caminhão não encontrado. Manutenção não será adicionada.")
                continue
            manutencao["mecanico"] = input("Mecânico (ID do Funcionário): ")
            if not search_funcionario(manutencao["mecanico"]):
                print("Mecânico não encontrado. Manutenção não será adicionada.")
                continue
            manutencao["pecas"] = input("Peças (ID do Produto): ")
            if not search_produto(manutencao["pecas"]):
                print("Peças não encontradas. Manutenção não será adicionada.")
                continue
            create_manutencao(
                manutencao["data_ingresso"],
                manutencao["data_saida"],
                manutencao["caminhao"],
                manutencao["mecanico"],
                manutencao["pecas"]
            )
        elif opcao == "2":
            id_manutencao = input("ID da Manutenção a ser atualizada: ")
            manutencao = {}
            manutencao["data_ingresso"] = input_date("Nova Data de Ingresso (DD/MM/AAAA): ")
            manutencao["data_saida"] = input_date("Nova Data de Saída (DD/MM/AAAA): ")
            manutencao["caminhao"] = input("Novo Caminhão (ID do Caminhão): ")
            if not search_caminhao(manutencao["caminhao"]):
                print("Caminhão não encontrado. Manutenção não será atualizada.")
                continue
            manutencao["mecanico"] = input("Novo Mecânico (ID do Funcionário): ")
            if not search_funcionario(manutencao["mecanico"]):
                print("Mecânico não encontrado. Manutenção não será atualizada.")
                continue
            manutencao["pecas"] = input("Novas Peças (ID do Produto): ")
            if not search_produto(manutencao["pecas"]):
                print("Peças não encontradas. Manutenção não será atualizada.")
                continue
            update_manutencao(
                id_manutencao,
                manutencao["data_ingresso"],
                manutencao["data_saida"],
                manutencao["caminhao"],
                manutencao["mecanico"],
                manutencao["pecas"]
            )
        elif opcao == "3":
            id_manutencao = input("ID da Manutenção a ser deletada: ")
            delete_manutencao(id_manutencao)
        elif opcao == "4":
            id_manutencao = input("ID da Manutenção a ser pesquisada: ")
            search_manutencao(id_manutencao)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
