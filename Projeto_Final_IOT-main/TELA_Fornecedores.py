# Nome do arquivo: TELA_Fornecedores.py
# Equipe: Clara, Rayanne e Tainá 
# Turma: G91164
# Semestre: 2025.1

from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Fornecedores")
menu_inicial.geometry("500x500+500+100")
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="fornecedor.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Fornecedores", bg="white", font=("Arial", 16, "bold")).place(x=120, y=10)

Label(menu_inicial, text="Cnpj:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_cnpj = Entry(menu_inicial, width=35)
entrada_cnpj.place(x=200, y=50)

Label(menu_inicial, text="Razão:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_razao = Entry(menu_inicial, width=35)
entrada_razao.place(x=200, y=90)

Label(menu_inicial, text="Nome:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_nome = Entry(menu_inicial, width=35)
entrada_nome.place(x=200, y=130)

Label(menu_inicial, text="Segmento:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_segmento = Entry(menu_inicial, width=35)
entrada_segmento.place(x=200, y=170)

def pegar_dados():
    cnpj = entrada_cnpj.get()
    razao = entrada_razao.get()
    nome = entrada_nome.get()
    segmento = entrada_segmento.get()

    print(f"CNPJ: {cnpj}, Razão: {razao}, Nome: {nome}, Segmento: {segmento}")

def limpar_campos():
    entrada_cnpj.delete(0, END)
    entrada_razao.delete(0, END)
    entrada_nome.delete(0, END)
    entrada_segmento.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=250)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=250)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=250)

menu_inicial.mainloop()