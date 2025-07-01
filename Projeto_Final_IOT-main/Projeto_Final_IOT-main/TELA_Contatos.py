from tkinter import *
import tkinter as tk
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Contatos")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="contato.png") 
menu_inicial.iconphoto(False, icon)

Label(menu_inicial, text="Cadastro de Contatos", bg="white", font=("Arial", 16, "bold")).pack(pady=5)

Label(menu_inicial, text="Telefone:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_telefone = Entry(menu_inicial, width=35)
entrada_telefone.place(x=200, y=50)

Label(menu_inicial, text="Celular:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=110)
entrada_celular = Entry(menu_inicial, width=35)
entrada_celular.place(x=200, y=110)

Label(menu_inicial, text="Email:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=80)
entrada_email = Entry(menu_inicial, width=35)
entrada_email.place(x=200, y=80)

def pegar_dados():
    telefone = entrada_telefone.get()
    celular = entrada_celular.get()
    email = entrada_email.get()

    print(f"Telefone: {telefone}, Celular: {celular}, Email: {email}")

def limpar_campos():
    entrada_telefone.delete(0, END)
    entrada_celular.delete(0, END)
    entrada_email.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, relief= tk.RAISED,  font=("Arial", 9, "bold")).place(x=140, y=200)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, relief= tk.RAISED, font=("Arial", 9, "bold")).place(x=220, y=200)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, relief= tk.RAISED, font=("Arial", 9, "bold")).place(x=300, y=200)

menu_inicial.mainloop()