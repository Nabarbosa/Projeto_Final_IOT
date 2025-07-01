"""
Nome do arquivo: TELA_Endereco.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Endereços")
menu_inicial.geometry("500x500+500+100")
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="endereco.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Endereços", bg="white", font=("Arial", 16)).pack(pady=5)

Label(menu_inicial, text="Logradouro:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_logradouro = Entry(menu_inicial, width=35)
entrada_logradouro.place(x=200, y=50)

Label(menu_inicial, text="Número:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=80)
entrada_numero = Entry(menu_inicial, width=35)  
entrada_numero.place(x=200, y=80)

Label(menu_inicial, text="Bairro:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=110)
entrada_bairro = Entry(menu_inicial, width=35)
entrada_bairro.place(x=200, y=110)

Label(menu_inicial, text="Cep:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=140)
entrada_cep = Entry(menu_inicial, width=35)
entrada_cep.place(x=200, y=140)

Label(menu_inicial, text="Cidade:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_cidade = Entry(menu_inicial, width=35)  
entrada_cidade.place(x=200, y=170)

Label(menu_inicial, text="Uf:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=200)
entrada_uf = Entry(menu_inicial, width=35)
entrada_uf.place(x=200, y=200)

def pegar_dados():
    logradouro = entrada_logradouro.get()
    numero = entrada_numero.get()
    bairro = entrada_bairro.get()
    cep = entrada_cep.get()
    cidade = entrada_cidade.get()
    uf = entrada_uf.get()
    
    print(f"Logradouro: {logradouro}, Número: {numero}, Bairro: {bairro}, Cep: {cep}, Cidade: {cidade}, Uf: {uf}")  

def limpar_campos():
    entrada_logradouro.delete(0, END)
    entrada_numero.delete(0, END)
    entrada_bairro.delete(0, END)
    entrada_cep.delete(0, END)
    entrada_cidade.delete(0, END)
    entrada_uf.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=250)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=250)
Button(menu_inicial, text="Sair", command=menu_inicial.destroy, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=250)

menu_inicial.mainloop()
