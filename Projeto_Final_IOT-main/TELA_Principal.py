# Nome do arquivo:
# Equipe: Clara, Rayanne e Tainá 
# Turma: G91164
# Semestre: 2025.1

from tkinter import *

def abrir_clientes():
    import TELA_Clientes
def abrir_funcionarios():
    import TELA_Funcionários
def abrir_caminhoes():
    import TELA_Caminhões
def abrir_contatos():
    import TELA_Contatos
def abrir_entrada_saida():
    import TELA_Entrada_Saida
def abrir_sensores():
    import TELA_Sensores
def abrir_enderecos():
    import TELA_Endereco
def abrir_produtos():
    import TELA_Produtos
def abrir_fornecedor():
    import TELA_Fornecedores
def abrir_manutencao():
    import TELA_Manutencao

menu_principal = Tk()
menu_principal.title("Página Principal")
menu_principal.geometry("600x600+600+150")
menu_principal.resizable(False, False)
menu_principal['bg'] = "white"

# Canvas e Scrollbar
canvas = Canvas(menu_principal, bg="white", highlightthickness=0)
scrollbar = Scrollbar(menu_principal, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.config(width=340)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

Label(scrollable_frame, text="Sistema Principal", bg="white", font=("Arial", 18, "bold")).pack(pady=30)

Button(scrollable_frame, text="Clientes", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_clientes).pack(pady=10)
Button(scrollable_frame, text="Funcionários", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_funcionarios).pack(pady=10)
Button(scrollable_frame, text="Caminhões", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_caminhoes).pack(pady=10)
Button(scrollable_frame, text="Contatos", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_contatos).pack(pady=10)
Button(scrollable_frame, text="Entrada/Saída", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_entrada_saida).pack(pady=10)
Button(scrollable_frame, text="Sensores", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_sensores).pack(pady=10)
Button(scrollable_frame, text="Endereços", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_enderecos).pack(pady=10)
Button(scrollable_frame, text="Produtos", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_produtos).pack(pady=10)
Button(scrollable_frame, text="Fornecedores", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_fornecedor).pack(pady=10)
Button(scrollable_frame, text="Manutenção", width=20, height=2, font=("Arial", 12, "bold"), command=abrir_manutencao).pack(pady=10)

menu_principal.mainloop()