"""
Nome do arquivo: TELA_Funcionários.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Funcionários")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="funcionario.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Funcionários", bg="white", font=("Arial", 16)).pack(pady=5)

Label(menu_inicial, text="Nome:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_nome = Entry(menu_inicial, width=30)   
entrada_nome.place(x=220, y=50)

Label(menu_inicial, text="CPF:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_cpf = Entry(menu_inicial, width=30)
entrada_cpf.place(x=220, y=90)

Label(menu_inicial, text="Cargo:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_cargo = Entry(menu_inicial, width=30)
entrada_cargo.place(x=220, y=130)

Label(menu_inicial, text="Data de Nascimento:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_data_nascimento = Entry(menu_inicial, width=30)
entrada_data_nascimento.place(x=220, y=170)

def pegar_dados():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    cargo = entrada_cargo.get()
    data_nascimento = entrada_data_nascimento.get()

    print(f"Nome: {nome}, CPF: {cpf}, Cargo: {cargo}, Data de Nascimento: {data_nascimento}")

def limpar_campos():
    entrada_nome.delete(0, END)
    entrada_cpf.delete(0, END)
    entrada_cargo.delete(0, END)
    entrada_data_nascimento.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=220)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=220)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=220)

menu_inicial.mainloop()