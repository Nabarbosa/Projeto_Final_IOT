from tkinter import *

menu_incial = Tk()
menu_incial.title("Sistema de Controle de Estoque")
menu_incial.geometry("500x800")
menu_incial.resizable(False,False)
menu_incial.state("iconic")
menu_incial.configure(bg="#f9f9f9")

w = Label(menu_incial, text="Bem vindo!", width=300, font=30)
w.pack()


menu_incial.mainloop()