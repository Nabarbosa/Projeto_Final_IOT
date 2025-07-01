"""
Nome do arquivo: TELA_Principal.py
Equipe: Clara, Rayanne e Tainá 
Turma: G91164
Semestre: 2025.11

"""
from tkinter import *
import tkinter.messagebox as messagebox 
import tkinter as tk

def abrir_tela(modulo, classe=None):
    try:
        janela = Toplevel(menu_principal) 
        janela.title(f"Tela de {modulo}") 
        janela.geometry("800x600+350+100") 
        janela.resizable(True, True) 
        janela['bg'] = "#f0f0f0" 

        if classe:
            modulo_carregado = __import__(modulo)
            TelaClasse = getattr(modulo_carregado, classe)
            tela_instancia = TelaClasse(janela)
        else:
            __import__(modulo)
            messagebox.showinfo("Informação", f"Módulo '{modulo}' importado, mas nenhuma classe foi especificada para instanciar.")

    except ImportError:
        messagebox.showerror("Erro de Importação", f"Não foi possível encontrar o módulo '{modulo}.py'. Certifique-se de que o arquivo existe e está no mesmo diretório.")
    except AttributeError:
        messagebox.showerror("Erro de Atributo", f"A classe '{classe}' não foi encontrada no módulo '{modulo}.py'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir a tela: {e}")

def abrir_clientes():
    abrir_tela("TELA_Clientes", "ClientesScreen")

def abrir_funcionarios():
    abrir_tela("TELA_Funcionarios", "FuncionariosScreen")

def abrir_caminhoes():
    abrir_tela("TELA_Caminhoes", "CaminhoesScreen")

def abrir_contatos():
    abrir_tela("TELA_Contatos", "ContatosScreen")

def abrir_entrada_saida():
    abrir_tela("TELA_Entrada_Saida", "EntradaSaidaScreen")

def abrir_sensores():
    abrir_tela("TELA_Sensores", "SensoresScreen")

def abrir_enderecos():
    abrir_tela("TELA_Endereco", "EnderecoScreen")

def abrir_produtos():
    abrir_tela("TELA_Produtos", "ProdutosScreen")

def abrir_fornecedor():
    abrir_tela("TELA_Fornecedores", "FornecedoresScreen")

def abrir_manutencao():
    abrir_tela("TELA_Manutencao", "ManutencaoScreen")

menu_principal = Tk()
menu_principal.title("Página Principal")
menu_principal.geometry("700x600+300+50")
menu_principal.resizable(False, False) 
menu_principal['bg'] = "white"

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

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

Label(
    scrollable_frame,
    text="Sistema Principal",
    bg="white",
    font=("Arial", 28, "bold")
).grid(row=0, column=0, columnspan=5, pady=40) 

botoes = [
    ("Clientes", abrir_clientes),
    ("Funcionários", abrir_funcionarios),
    ("Caminhões", abrir_caminhoes),
    ("Contatos", abrir_contatos),
    ("Entrada/Saída", abrir_entrada_saida),
    ("Sensores", abrir_sensores),
    ("Endereços", abrir_enderecos),
    ("Produtos", abrir_produtos),
    ("Fornecedores", abrir_fornecedor),
    ("Manutenção", abrir_manutencao),
]

for i, (texto, comando) in enumerate(botoes):
    row = (i // 3) + 1 # 
    col = (i % 3) + 1 
    Button(
        scrollable_frame,
        text=texto,
        width=15,
        height=3,
        font=("Helvetica", 14, "bold"),
        command=comando,
        bg="#E0E7DE",
        fg="black", 
        activebackground="#000000", 
        activeforeground="black", 
        bd=8, 
        relief= tk.RAISED, 
        cursor="hand2" 
    ).grid(row=row, column=col, padx=15, pady=15, sticky="nsew") 

scrollable_frame.grid_columnconfigure(0, weight=1) 
scrollable_frame.grid_columnconfigure(1, weight=1)
scrollable_frame.grid_columnconfigure(2, weight=1) 
scrollable_frame.grid_columnconfigure(3, weight=1) 
scrollable_frame.grid_columnconfigure(4, weight=1) 

menu_principal.mainloop()
