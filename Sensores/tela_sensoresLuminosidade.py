import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, StringVar
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Painel de Controle - Luminosidade Fictícia")
        self.geometry("450x300") 
        self.resizable(False, False)

        light_frame = Frame(self, bd=2, relief=tk.GROOVE)
        light_frame.pack(padx=10, pady=20, fill=tk.X)
        Label(light_frame, text="Status do Sensor de Luminosidade (LDR)", font=("Helvetica", 12, "bold")).pack(pady=5)
        
        self.light_status_var = StringVar(value="Dia Claro (Valor: ---)")
        self.light_display_label = Label(
            light_frame, 
            textvariable=self.light_status_var, 
            font=("Helvetica", 16, "bold"), 
            fg="orange"
        )
        self.light_display_label.pack(pady=10)

        led_frame = Frame(self, bd=2, relief=tk.GROOVE)
        led_frame.pack(padx=10, pady=10, fill=tk.X)
        Label(led_frame, text="Status do LED", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.led_status_var = StringVar(value="LED DESLIGADO")
        self.led_display_label = Label(
            led_frame, 
            textvariable=self.led_status_var, 
            font=("Helvetica", 18, "bold"), 
            fg="gray"
        )
        self.led_display_label.pack(pady=10)
        
        control_btn = Button(
            self, 
            text="Simular Luminosidade", 
            command=self.simulate_luminosity,
            font=("Helvetica", 10),
            bg="#4682B4", 
            fg="white", 
            relief=tk.RAISED, 
            bd=3 
        )
        control_btn.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        
        self.LDR_DARK_THRESHOLD = 300 

    def simulate_luminosity(self):
       
        fictitious_light_value = random.randint(0, 1000) 

        is_dark = False
        if fictitious_light_value > self.LDR_DARK_THRESHOLD:
            self.light_status_var.set(f"Noite / Escuro (Valor: {fictitious_light_value})")
            self.light_display_label.config(fg="purple")
            is_dark = True
        else:
            self.light_status_var.set(f"Dia Claro (Valor: {fictitious_light_value})")
            self.light_display_label.config(fg="orange")
            is_dark = False

        if is_dark:
            self.led_status_var.set("LED LIGADO")
            self.led_display_label.config(fg="green")
            print(f"LED LIGADO: Luminosidade simulada = {fictitious_light_value} (Escuro).")
        else:
            self.led_status_var.set("LED DESLIGADO")
            self.led_display_label.config(fg="gray")
            print(f"LED DESLIGADO: Luminosidade simulada = {fictitious_light_value} (Claro).")

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()