# quero que mude algumas informações nesse código. 
# o nome da variável é "registro_entrada_saida" e ele possui as seguintes informações:
#  data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso,
#  km_saida, km_chegada, caminhao (importar CRUD_Caminhões), 
# motorista (importar CRUD_Funcionário). 
# mantenha a base do arquivo como está apenas mude os nomes.


# Importações necessárias
from CRUD_Caminhões import search_caminhao
from CRUD_Funcionários import search_funcionario

# Função para gerar o próximo ID automaticamente
def gerar_proximo_id():
    try:
        with open("registro_entrada_saida.txt", "r") as arquivo:
            ultimo_id = 0
            for linha in arquivo:  # Lê linha por linha
                dados = linha.strip().split(",")
                ultimo_id = int(dados[0])  # Atualiza o último ID encontrado
            return ultimo_id + 1  # Retorna o próximo ID
    except FileNotFoundError:
        return 1  # Retorna 1 se o arquivo não existir

# CREATE - Criar
def create_registro(data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, caminhao, motorista):
    id_registro = gerar_proximo_id()  # Gera o próximo ID automaticamente
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
                if dados[0] == id_registro:  # Verifica pelo ID
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
                if dados[0] != id_registro:  # Verifica pelo ID
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
                if dados[0] == id_registro:  # Verifica pelo ID
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
            data_entrada = input("Data de Entrada (DD/MM/AAAA): ")
            data_saida = input("Data de Saída (DD/MM/AAAA): ")
            hora_entrada = input("Hora de Entrada (HH:MM): ")
            hora_saida = input("Hora de Saída (HH:MM): ")
            destino = input("Destino: ")
            roteiro = input("Roteiro: ")
            peso = input("Peso: ")
            km_saida = input("KM de Saída: ")
            km_chegada = input("KM de Chegada: ")
            caminhao = input("Caminhão (ID do Caminhão - importar de CRUD_Caminhoes): ")
            motorista = input("Motorista (ID do Motorista - importar de CRUD_Funcionario): ")
            create_registro(data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, caminhao, motorista)
        elif opcao == "2":
            id_registro = input("ID do Registro a ser atualizado: ")
            data_entrada = input("Nova Data de Entrada (DD/MM/AAAA): ")
            data_saida = input("Nova Data de Saída (DD/MM/AAAA): ")
            hora_entrada = input("Nova Hora de Entrada (HH:MM): ")
            hora_saida = input("Nova Hora de Saída (HH:MM): ")
            destino = input("Novo Destino: ")
            roteiro = input("Novo Roteiro: ")
            peso = input("Novo Peso: ")
            km_saida = input("Novo KM de Saída: ")
            km_chegada = input("Novo KM de Chegada: ")
            caminhao = input("Novo Caminhão (ID do Caminhão - importar de CRUD_Caminhoes): ")
            motorista = input("Novo Motorista (ID do Motorista - importar de CRUD_Funcionario): ")
            update_registro(id_registro, data_entrada, data_saida, hora_entrada, hora_saida, destino, roteiro, peso, km_saida, km_chegada, caminhao, motorista)
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