import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, StringVar
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Painel de Controle - Sensores de Presença")
        self.geometry("400x250") 
        self.resizable(False, False)
        presence_frame = Frame(self, bd=2, relief=tk.GROOVE)
        presence_frame.pack(padx=10, pady=10, fill=tk.X)

        Label(presence_frame, text="Status da Presença", font=("Helvetica", 12, "bold")).pack(pady=5)

        self.presence_status_var = StringVar(value="Nenhuma Presença (0)")
        
        self.presence_display_label = Label(
            presence_frame, 
            textvariable=self.presence_status_var, 
            font=("Helvetica", 16, "bold"), 
            fg="green"
        )
        self.presence_display_label.pack(pady=10)

        toggle_presence_btn = Button(
            presence_frame, 
            text="Gerar Movimento", 
            command=self.generate_fictitious_movement,
            font=("Helvetica", 10),
            bg="#4CAF50", 
            relief=tk.RAISED, 
        )
        toggle_presence_btn.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def generate_fictitious_movement(self):
        fictitious_value = random.randint(0, 10) 
        
        new_status_text = ""
        color = "green"

        if fictitious_value > 0:
            new_status_text = f"Presença Detectada! ({fictitious_value})"
            color = "red" 
        else:
            new_status_text = f"Nenhuma Presença ({fictitious_value})"
            color = "green" 
        self.presence_status_var.set(new_status_text)
        self.presence_display_label.config(fg=color)
        
        print(f"Status de presença gerado: {new_status_text}")

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
