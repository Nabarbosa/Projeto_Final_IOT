from tkinter import *
from tkinter import PhotoImage
import tkinter as tk

menu_inicial = Tk()
menu_inicial.title ("Sistema de Caminhões")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white"
icon = PhotoImage(file="caminhão.png") 
menu_inicial.iconphoto(False, icon) 

Label(menu_inicial, text="Cadastro de Caminhões", bg="white", font=("Arial", 16)).pack(pady=5)

Label(menu_inicial, text="Renavam:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_renavam = Entry(menu_inicial, width=35)
entrada_renavam.place(x=200, y=50)

Label(menu_inicial, text="Modelo:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=80)
entrada_modelo = Entry(menu_inicial, width=35)
entrada_modelo.place(x=200, y=80)

Label(menu_inicial, text="Marca:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=110)
entrada_marca = Entry(menu_inicial, width=35)
entrada_marca.place(x=200, y=110)

Label(menu_inicial, text="Cor:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=140)
entrada_cor = Entry(menu_inicial, width=35)
entrada_cor.place(x=200, y=140)

Label(menu_inicial, text="Placa:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_placa = Entry(menu_inicial, width=35)
entrada_placa.place(x=200, y=170)

Label(menu_inicial, text="Chassi:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=200)
entrada_chassi = Entry(menu_inicial, width=35)
entrada_chassi.place(x=200, y=200)

Label(menu_inicial, text="Status:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=230)
entrada_status = Entry(menu_inicial, width=35)
entrada_status.place(x=200, y=230)

Label(menu_inicial, text="Tipo:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=260)
entrada_tipo = Entry(menu_inicial, width=35)
entrada_tipo.place(x=200, y=260)

Label(menu_inicial, text="Peso:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=290)
entrada_peso = Entry(menu_inicial, width=35)
entrada_peso.place(x=200, y=290)

Label(menu_inicial, text="Capacidade:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=320)
entrada_capacidade = Entry(menu_inicial, width=35)
entrada_capacidade.place(x=200, y=320)

# Botão para pegar os dados (exemplo)
def pegar_dados():
    renavam = entrada_renavam.get()
    modelo = entrada_modelo.get()
    marca = entrada_marca.get()
    cor = entrada_cor.get()
    placa = entrada_placa.get()
    chassi = entrada_chassi.get()
    tipo = entrada_tipo.get()
    peso = entrada_peso.get()
    capacidade = entrada_capacidade.get()
    print(f"Renavam: {renavam}, Modelo: {modelo}, Marca: {marca}, Cor: {cor}, Placa: {placa}, Chassi: {chassi}, Tipo: {tipo}, Peso: {peso}, Capacidade: {capacidade}")

def limpar_campos():
    entrada_renavam.delete(0, END)
    entrada_modelo.delete(0, END)
    entrada_marca.delete(0, END)
    entrada_cor.delete(0, END)
    entrada_placa.delete(0, END)
    entrada_chassi.delete(0, END)
    entrada_status.delete(0, END)
    entrada_tipo.delete(0, END)
    entrada_peso.delete(0, END)
    entrada_capacidade.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=400)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=400)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=400)

menu_inicial.mainloop()