# Importações necessárias
from CRUD_Caminhões import search_caminhao
from CRUD_Funcionários import search_funcionario
from datetime import datetime

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("registro_entrada_saida.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])
            return ultimo_id + 1
    except FileNotFoundError:
        return 1

# CREATE - Criar
def create_registro(data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, caminhao, motorista):
    id_registro = gerar_proximo_id()
    with open("registro_entrada_saida.txt", "a") as arquivo:
        arquivo.write(f"{id_registro},{data_entrada},{data_saida},{hora_entrada},{hora_saida},{destino},{roteiro},{peso},{km_saida},{km_chegada},{caminhao},{motorista}\n")
    print(f"Registro {id_registro} adicionado com sucesso!")

# UPDATE - Atualizar
def update_registro(id_registro, data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, caminhao, motorista):
    try:
        with open("registro_entrada_saida.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("registro_entrada_saida.txt", "w") as arquivo:
            atualizado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] == id_registro:
                    arquivo.write(f"{id_registro},{data_entrada},{data_saida},{hora_entrada},{hora_saida},{destino},{roteiro},{peso},{km_saida},{km_chegada},{caminhao},{motorista}\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
            if atualizado:
                print(f"Registro {id_registro} atualizado com sucesso!")
            else:
                print(f"Registro {id_registro} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum registro cadastrado.")

# DELETE - Deletar
def delete_registro(id_registro):
    try:
        with open("registro_entrada_saida.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("registro_entrada_saida.txt", "w") as arquivo:
            deletado = False
            for linha in linhas:
                dados = linha.strip().split(",")
                if dados[0] != id_registro:
                    arquivo.write(linha)
                else:
                    deletado = True
            if deletado:
                print(f"Registro {id_registro} deletado com sucesso!")
            else:
                print(f"Registro {id_registro} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum registro cadastrado.")

# SEARCH - Pesquisar
def search_registro(id_registro):
    try:
        with open("registro_entrada_saida.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == id_registro:
                    print("\nRegistro encontrado:")
                    print(f"ID: {dados[0]}")
                    print(f"Data de Entrada: {dados[1]}")
                    print(f"Data de Saída: {dados[2]}")
                    print(f"Hora de Entrada: {dados[3]}")
                    print(f"Hora de Saída: {dados[4]}")
                    print(f"Destino: {dados[5]}")
                    print(f"Roteiro: {dados[6]}")
                    print(f"Peso: {dados[7]}")
                    print(f"KM de Saída: {dados[8]}")
                    print(f"KM de Chegada: {dados[9]}")
                    print(f"Caminhão (ID): {dados[10]}")
                    print(f"Motorista (ID): {dados[11]}")
                    return
            print(f"Registro com ID {id_registro} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum registro cadastrado.")

# Função para ler datas e horas
def input_date(msg):
    while True:
        valor = input(msg)
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA.")

def input_time(msg):
    while True:
        valor = input(msg)
        try:
            return datetime.strptime(valor, "%H:%M").time()
        except ValueError:
            print("Hora inválida. Use o formato HH:MM.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n=== CRUD Registro de Entrada e Saída ===")
        print("1. Adicionar Registro")
        print("2. Atualizar Registro")
        print("3. Deletar Registro")
        print("4. Pesquisar Registro pelo ID")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registro_entrada_saida = {}
            registro_entrada_saida["data_entrada"] = input_date("Data de Entrada (DD/MM/AAAA): ")
            registro_entrada_saida["data_saida"] = input_date("Data de Saída (DD/MM/AAAA): ")
            registro_entrada_saida["hora_entrada"] = input_time("Hora de Entrada (HH:MM): ")
            registro_entrada_saida["hora_saida"] = input_time("Hora de Saída (HH:MM): ")
            registro_entrada_saida["destino"] = input("Destino: ")
            registro_entrada_saida["roteiro"] = input("Roteiro: ")
            try:
                registro_entrada_saida["peso"] = float(input("Peso: "))
            except ValueError:
                print("Peso deve ser um número real.")
                continue
            registro_entrada_saida["km_saida"] = input("KM de Saída: ")
            registro_entrada_saida["km_chegada"] = input("KM de Chegada: ")
            registro_entrada_saida["caminhao"] = input("Caminhão (ID do Caminhão): ")
            if not search_caminhao(registro_entrada_saida["caminhao"]):
                print("Caminhão não encontrado. Registro não será adicionado.")
                continue
            registro_entrada_saida["motorista"] = input("Motorista (ID do Motorista): ")
            if not search_funcionario(registro_entrada_saida["motorista"]):
                print("Motorista não encontrado. Registro não será adicionado.")
                continue
            create_registro(
                registro_entrada_saida["data_entrada"],
                registro_entrada_saida["data_saida"],
                registro_entrada_saida["hora_entrada"],
                registro_entrada_saida["hora_saida"],
                registro_entrada_saida["destino"],
                registro_entrada_saida["roteiro"],
                registro_entrada_saida["peso"],
                registro_entrada_saida["km_saida"],
                registro_entrada_saida["km_chegada"],
                registro_entrada_saida["caminhao"],
                registro_entrada_saida["motorista"]
            )
        elif opcao == "2":
            id_registro = input("ID do Registro a ser atualizado: ")
            registro_entrada_saida = {}
            registro_entrada_saida["data_entrada"] = input_date("Nova Data de Entrada (DD/MM/AAAA): ")
            registro_entrada_saida["data_saida"] = input_date("Nova Data de Saída (DD/MM/AAAA): ")
            registro_entrada_saida["hora_entrada"] = input_time("Nova Hora de Entrada (HH:MM): ")
            registro_entrada_saida["hora_saida"] = input_time("Nova Hora de Saída (HH:MM): ")
            registro_entrada_saida["destino"] = input("Novo Destino: ")
            registro_entrada_saida["roteiro"] = input("Novo Roteiro: ")
            try:
                registro_entrada_saida["peso"] = float(input("Novo Peso: "))
            except ValueError:
                print("Peso deve ser um número real.")
                continue
            registro_entrada_saida["km_saida"] = input("Novo KM de Saída: ")
            registro_entrada_saida["km_chegada"] = input("Novo KM de Chegada: ")
            registro_entrada_saida["caminhao"] = input("Novo Caminhão (ID do Caminhão): ")
            if not search_caminhao(registro_entrada_saida["caminhao"]):
                print("Caminhão não encontrado. Registro não será atualizado.")
                continue
            registro_entrada_saida["motorista"] = input("Novo Motorista (ID do Motorista): ")
            if not search_funcionario(registro_entrada_saida["motorista"]):
                print("Motorista não encontrado. Registro não será atualizado.")
                continue
            update_registro(
                id_registro,
                registro_entrada_saida["data_entrada"],
                registro_entrada_saida["data_saida"],
                registro_entrada_saida["hora_entrada"],
                registro_entrada_saida["hora_saida"],
                registro_entrada_saida["destino"],
                registro_entrada_saida["roteiro"],
                registro_entrada_saida["peso"],
                registro_entrada_saida["km_saida"],
                registro_entrada_saida["km_chegada"],
                registro_entrada_saida["caminhao"],
                registro_entrada_saida["motorista"]
            )
        elif opcao == "3":
            id_registro = input("ID do Registro a ser deletado: ")
            delete_registro(id_registro)
        elif opcao == "4":
            id_registro = input("ID do Registro a ser pesquisado: ")
            search_registro(id_registro)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
