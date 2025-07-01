# Nome do arquivo: TELA_Entrada_Saida.py
# Equipe: Clara, Rayanne e Tainá 
# Turma: G91164
# Semestre: 2025.1

from tkinter import *
from tkinter import PhotoImage

menu_inicial = Tk()
menu_inicial.title ("Sistema de Entrada e Saída")
menu_inicial.geometry("500x500+500+100") 
menu_inicial.resizable(False, False) 
menu_inicial['bg'] = "white" 
icon = PhotoImage(file="relogio.png") 
menu_inicial.iconphoto(False, icon) 

Label(menu_inicial, text="Entrada e Saída", bg="white", font=("Arial", 16)).pack(pady=5)

Label(menu_inicial, text="Data/Hora Saída:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=50)
entrada_data_hora_saida = Entry(menu_inicial, width=30)
entrada_data_hora_saida.place(x=200, y=50)

Label(menu_inicial, text="Km Saída:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=90)
entrada_km_saida = Entry(menu_inicial, width=30)
entrada_km_saida.place(x=200, y=90)

Label(menu_inicial, text="Destino:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=130)
entrada_destino = Entry(menu_inicial, width=30)
entrada_destino.place(x=200, y=130)

Label(menu_inicial, text="Peso:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=170)
entrada_peso = Entry(menu_inicial, width=30)
entrada_peso.place(x=200, y=170)

Label(menu_inicial, text="Data/Hora Retorno:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=210)
entrada_data_hora_retorno = Entry(menu_inicial, width=30)
entrada_data_hora_retorno.place(x=200, y=210)

Label(menu_inicial, text="Km Retorno:", bg="white", font=("Arial", 12, "bold")).place(x=50, y=250)
entrada_km_retorno = Entry(menu_inicial, width=30)
entrada_km_retorno.place(x=200, y=250)

def pegar_dados():
    data_hora_saida = entrada_data_hora_saida.get()
    km_saida = entrada_km_saida.get()
    destino = entrada_destino.get()
    peso = entrada_peso.get()
    data_hora_retorno = entrada_data_hora_retorno.get()
    km_retorno = entrada_km_retorno.get()

    print(f"Data/Hora Saída: {data_hora_saida}")
    print(f"Km Saída: {km_saida}")
    print(f"Destino: {destino}")
    print(f"Peso: {peso}")
    print(f"Data/Hora Retorno: {data_hora_retorno}")
    print(f"Km Retorno: {km_retorno}")

def limpar_campos():
    entrada_data_hora_saida.delete(0, END)
    entrada_km_saida.delete(0, END)
    entrada_destino.delete(0, END)
    entrada_peso.delete(0, END)
    entrada_data_hora_retorno.delete(0, END)
    entrada_km_retorno.delete(0, END)

Button(menu_inicial, text="Salvar", command=pegar_dados, width=8, height=2, font=("Arial", 9, "bold")).place(x=140, y=300)
Button(menu_inicial, text="Limpar", command=limpar_campos, width=8, height=2, font=("Arial", 9, "bold")).place(x=220, y=300)
Button(menu_inicial, text="Sair", command=menu_inicial.quit, width=8, height=2, font=("Arial", 9, "bold")).place(x=300, y=300)

menu_inicial.mainloop()