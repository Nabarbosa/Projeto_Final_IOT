"""
Nome do arquivo: TELA_Sensores.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Sensores")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="sensores.png") 
menu_inicial.iconphoto(False, icon) 

Label(menu_inicial, text="Sistema de Sensores", bg="white", font=("Arial", 16, "bold")).pack(pady=5)

Label(menu_inicial, text="Temperatura:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_temperatura = Entry(menu_inicial, width=30)
entrada_temperatura.place(x=200, y=50)

Label(menu_inicial, text="Luminosidade:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_luminosidade = Entry(menu_inicial, width=30)
entrada_luminosidade.place(x=200, y=90)

Label(menu_inicial, text="Gás:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_gas = Entry(menu_inicial, width=30)
entrada_gas.place(x=200, y=130)

Label(menu_inicial, text="Presença:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_presenca = Entry(menu_inicial, width=30)
entrada_presenca.place(x=200, y=170)

def pegar_dados():
    temperatura = entrada_temperatura.get()
    luminosidade = entrada_luminosidade.get()
    gas = entrada_gas.get()
    presenca = entrada_presenca.get()
    
    print(f"Temperatura: {temperatura}")
    print(f"Luminosidade: {luminosidade}")
    print(f"Gás: {gas}")
    print(f"Presença: {presenca}")

def limpar_campos():
    entrada_temperatura.delete(0, END)
    entrada_luminosidade.delete(0, END)
    entrada_gas.delete(0, END)
    entrada_presenca.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=220)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=220)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=220)  

menu_inicial.mainloop()