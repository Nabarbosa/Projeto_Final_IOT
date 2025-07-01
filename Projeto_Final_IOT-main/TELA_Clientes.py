# Nome do arquivo: TELA_Clientes.py
# Equipe: Clara, Rayanne e Tainá 
# Turma: G91164
# Semestre: 2025.1

from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Clientes")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="cliente.png") 
menu_inicial.iconphoto(False, icon) 

Label(menu_inicial, text="Cadastro de Clientes", bg="white", font=("Arial", 16)).pack(pady=5)

Label(menu_inicial, text="Nome:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_nome = Entry(menu_inicial, width=35)
entrada_nome.place(x=200, y=50)

Label(menu_inicial, text="Tipo:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=80)
entrada_tipo = Entry(menu_inicial, width=35)
entrada_tipo.place(x=200, y=80)

Label(menu_inicial, text="CPF:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=110)
entrada_cpf = Entry(menu_inicial, width=35)
entrada_cpf.place(x=200, y=110)

Label(menu_inicial, text="Cnpj:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=140)
entrada_cnpj = Entry(menu_inicial, width=35)
entrada_cnpj.place(x=200, y=140)

Label(menu_inicial, text="Observadores:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_observadores = Entry(menu_inicial, width=35)
entrada_observadores.place(x=200, y=170)

def pegar_dados():
    nome = entrada_nome.get()
    tipo = entrada_tipo.get()
    cpf = entrada_cpf.get()
    cnpj = entrada_cnpj.get()
    observadores = entrada_observadores.get()

    print(f"Nome: {nome}, Tipo: {tipo}, CPF: {cpf}, CNPJ: {cnpj}, Observadores: {observadores}")

def limpar_campos():
    entrada_nome.delete(0, END)
    entrada_tipo.delete(0, END)
    entrada_cpf.delete(0, END)
    entrada_cnpj.delete(0, END)
    entrada_observadores.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=250)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=250)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=250)

menu_inicial.mainloop()