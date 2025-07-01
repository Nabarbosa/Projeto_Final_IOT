"""
Nome do arquivo: TELA_Manutencao.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Manutencao")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="manutencao.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Manutencao", bg="white", font=("Arial", 16)).pack(pady=5) 

Label(menu_inicial, text="Data/Hora Entrada:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50 )
entrada_data_hora_entrada = Entry(menu_inicial, width=30)
entrada_data_hora_entrada.place(x=200, y=50)

Label(menu_inicial, text="Solicitante:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_solicitante = Entry(menu_inicial, width=30)
entrada_solicitante.place(x=200, y=90)

Label(menu_inicial, text="Queixa:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_queixa = Entry(menu_inicial, width=30)
entrada_queixa.place(x=200, y=130)

Label(menu_inicial, text="Serviço:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_servico = Entry(menu_inicial, width=30)
entrada_servico.place(x=200, y=170)

Label(menu_inicial, text="Data/Hora Entrega:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=210)
entrada_data_hora_entrega = Entry(menu_inicial, width=30)
entrada_data_hora_entrega.place(x=200, y=210)

def pegar_dados():
    data_hora_entrada = entrada_data_hora_entrada.get()
    solicitante = entrada_solicitante.get()
    queixa = entrada_queixa.get()
    servico = entrada_servico.get()
    data_hora_entrega = entrada_data_hora_entrega.get()

    print(f"Data/Hora Entrada: {data_hora_entrada}")
    print(f"Solicitante: {solicitante}")
    print(f"Queixa: {queixa}")
    print(f"Serviço: {servico}")
    print(f"Data/Hora Entrega: {data_hora_entrega}")

def limpar_campos():
    entrada_data_hora_entrada.delete(0, END)
    entrada_solicitante.delete(0, END)
    entrada_queixa.delete(0, END)
    entrada_servico.delete(0, END)
    entrada_data_hora_entrega.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=250)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=250)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=250)  

menu_inicial.mainloop()