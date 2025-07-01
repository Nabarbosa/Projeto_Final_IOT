def adicionar_caminhao():
    renavam = input("Digite o Renavam: ")
    modelo = input("Digite o Modelo: ")
    marca = input("Digite a Marca: ")
    cor = input("Digite a Cor: ")
    placa = input("Digite a Placa: ")
    chassi = input("Digite o Chassi: ")
    status = input("Digite o Status: ")
    tipo = input("Digite o Tipo: ")
    peso = input("Digite o Peso: ")
    capacidade = input("Digite a Capacidade: ")

    with open("caminhoes.txt", "a") as arquivo:
        arquivo.write(f"{renavam},{modelo},{marca},{cor},{placa},{chassi},{status},{tipo},{peso},{capacidade}\n")
    print("Caminhão adicionado com sucesso!")

def listar_caminhoes():
    with open("caminhoes.txt", "r") as arquivo:
        for linha in arquivo:
            caminhao = linha.strip().split(",")
            print(f"Renavam: {caminhao[0]}, Modelo: {caminhao[1]}, Marca: {caminhao[2]}, Cor: {caminhao[3]}, "
                  f"Placa: {caminhao[4]}, Chassi: {caminhao[5]}, Status: {caminhao[6]}, Tipo: {caminhao[7]}, "
                  f"Peso: {caminhao[8]}, Capacidade: {caminhao[9]}")
            
def alterar_caminhao():
    renavam = input("Digite o Renavam do caminhão a ser alterado: ")
    encontrado = False
    linhas = []

    with open("caminhoes.txt", "r") as arquivo:
        for linha in arquivo:
            caminhao = linha.strip().split(",")
            if caminhao[0] == renavam:
                encontrado = True
                caminhao[1] = input("Digite o novo Modelo: ")
                caminhao[2] = input("Digite a nova Marca: ")
                caminhao[3] = input("Digite a nova Cor: ")
                caminhao[4] = input("Digite a nova Placa: ")
                caminhao[5] = input("Digite o novo Chassi: ")
                caminhao[6] = input("Digite o novo Status: ")
                caminhao[7] = input("Digite o novo Tipo: ")
                caminhao[8] = input("Digite o novo Peso: ")
                caminhao[9] = input("Digite a nova Capacidade: ")
            linhas.append(",".join(caminhao))

    if encontrado:
        with open("caminhoes.txt", "w") as arquivo:
            for linha in linhas:
                arquivo.write(linha + "\n")
        print("Caminhão alterado com sucesso!")
    else:
        print("Caminhão não encontrado.")

def excluir_caminhao():
    renavam = input("Digite o Renavam do caminhão a ser excluído: ")
    encontrado = False
    linhas = []

    with open("caminhoes.txt", "r") as arquivo:
        for linha in arquivo:
            caminhao = linha.strip().split(",")
            if caminhao[0] != renavam:
                linhas.append(linha.strip())
            else:
                encontrado = True

    if encontrado:
        with open("caminhoes.txt", "w") as arquivo:
            for linha in linhas:
                arquivo.write(linha + "\n")
        print("Caminhão excluído com sucesso!")
    else:
        print("Caminhão não encontrado.")