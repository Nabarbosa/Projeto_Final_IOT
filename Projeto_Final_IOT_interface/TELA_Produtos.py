"""
Nome do arquivo: TELA_Produtos.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Produtos")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="produtos.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Produtos", bg="white", font=("Arial", 16)).pack(pady=5)       

Label(menu_inicial, text="Descrição:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_descricao = Entry(menu_inicial, width=30)
entrada_descricao.place(x=200, y=50)

Label(menu_inicial, text="Tipo:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_tipo = Entry(menu_inicial, width=30)
entrada_tipo.place(x=200, y=90)

Label(menu_inicial, text="Validade:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_validade = Entry(menu_inicial, width=30)
entrada_validade.place(x=200, y=130)

Label(menu_inicial, text="Observação:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_observacao = Entry(menu_inicial, width=30)
entrada_observacao.place(x=200, y=170)

def pegar_dados():
    descricao = entrada_descricao.get()
    tipo = entrada_tipo.get()
    validade = entrada_validade.get()
    observacao = entrada_observacao.get()

    print(f"Descrição: {descricao}")
    print(f"Tipo: {tipo}")
    print(f"Validade: {validade}")
    print(f"Observação: {observacao}")

def limpar_campos():
    entrada_descricao.delete(0, END)
    entrada_tipo.delete(0, END)
    entrada_validade.delete(0, END)
    entrada_observacao.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=250)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=250)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=250)

menu_inicial.mainloop()