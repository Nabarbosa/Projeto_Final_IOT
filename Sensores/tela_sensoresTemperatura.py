import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, StringVar
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Painel de Controle - Sensores e Alarme")
        self.geometry("700x550") 
        self.resizable(False, False)

        primary_sensor_frame = Frame(self, bd=2, relief=tk.GROOVE)
        primary_sensor_frame.pack(padx=10, pady=10, fill=tk.X)
        Label(primary_sensor_frame, text="Sensor Primário (A0) e LEDs", font=("Helvetica", 12, "bold")).pack(pady=5)
        
        self.primary_sensor_var = StringVar(value="Valor A0: ---")
        Label(primary_sensor_frame, textvariable=self.primary_sensor_var, font=("Helvetica", 14)).pack(pady=5)

        leds_sub_frame = Frame(primary_sensor_frame)
        leds_sub_frame.pack(pady=5)

        self.led_verde_var = StringVar(value="Verde: OFF")
        self.led_verde_label = Label(leds_sub_frame, textvariable=self.led_verde_var, font=("Helvetica", 12), fg="gray")
        self.led_verde_label.pack(side=tk.LEFT, padx=10)

        self.led_amarelo_var = StringVar(value="Amarelo: OFF")
        self.led_amarelo_label = Label(leds_sub_frame, textvariable=self.led_amarelo_var, font=("Helvetica", 12), fg="gray")
        self.led_amarelo_label.pack(side=tk.LEFT, padx=10)

        self.led_branco_var = StringVar(value="Branco: OFF")
        self.led_branco_label = Label(leds_sub_frame, textvariable=self.led_branco_var, font=("Helvetica", 12), fg="gray")
        self.led_branco_label.pack(side=tk.LEFT, padx=10)

        hazard_sensor_frame = Frame(self, bd=2, relief=tk.GROOVE)
        hazard_sensor_frame.pack(padx=10, pady=10, fill=tk.X)
        Label(hazard_sensor_frame, text="Sensor de Fumaça/Temperatura (A1)", font=("Helvetica", 12, "bold")).pack(pady=5)
        
        self.hazard_sensor_var = StringVar(value="Valor A1: --- (Normal)")
        self.hazard_display_label = Label(
            hazard_sensor_frame, 
            textvariable=self.hazard_sensor_var, 
            font=("Helvetica", 14, "bold"), 
            fg="blue" 
        )
        self.hazard_display_label.pack(pady=10)

        siren_frame = Frame(self, bd=2, relief=tk.GROOVE)
        siren_frame.pack(padx=10, pady=10, fill=tk.X)
        Label(siren_frame, text="Status da Sirene", font=("Helvetica", 12, "bold")).pack(pady=5)
        self.siren_status_var = StringVar(value="Sirene DESATIVADA")
        self.siren_display_label = Label(
            siren_frame, 
            textvariable=self.siren_status_var, 
            font=("Helvetica", 18, "bold"), 
            fg="gray" 
        )
        self.siren_display_label.pack(pady=10)

        control_btn = Button(
            self, 
            text="Simular Ambiente", 
            command=self.simulate_environment,
            font=("Helvetica", 10),
            bg="#4682B4", 
            fg="white", 
            relief=tk.RAISED, 
            bd=3 
        )
        control_btn.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.LED_VERDE = 100
        self.LED_AMARELO = 200
        self.LED_BRANCO = 300
        self.SIREN = 350

    def simulate_environment(self):
        valor_sensor_a0 = random.randint(0, 400) 
        self.primary_sensor_var.set(f"Valor A0: {valor_sensor_a0}")

        if valor_sensor_a0 > self.LED_VERDE:
            self.led_verde_var.set("Verde: ON")
            self.led_verde_label.config(fg="green")
        else:
            self.led_verde_var.set("Verde: OFF")
            self.led_verde_label.config(fg="gray")

        if valor_sensor_a0 > self.LED_AMARELO:
            self.led_amarelo_var.set("Amarelo: ON")
            self.led_amarelo_label.config(fg="gold")
        else:
            self.led_amarelo_var.set("Amarelo: OFF")
            self.led_amarelo_label.config(fg="gray")

        if valor_sensor_a0 > self.LED_BRANCO:
            self.led_branco_var.set("Branco: ON")
            self.led_branco_label.config(fg="white") # Cor branca para o texto do LED branco
        else:
            self.led_branco_var.set("Branco: OFF")
            self.led_branco_label.config(fg="gray")

        if valor_sensor_a0 > self.SIREN:
            self.hazard_sensor_var.set(f"Valor A0: {valor_sensor_a0} (PERIGO!)")
            self.hazard_display_label.config(fg="red")
            self.siren_status_var.set("Sirene ATIVADA!")
            self.siren_display_label.config(fg="red")
            print(f"ALERTA: Sirene ativada! Valor A0 = {valor_sensor_a0}")
        else:
            self.hazard_sensor_var.set(f"Valor A1: {valor_sensor_a0} (Normal)")
            self.hazard_display_label.config(fg="blue")
            self.siren_status_var.set("Sirene DESATIVADA")
            self.siren_display_label.config(fg="gray")
            print(f"Sirene desativada. Valor A1 = {valor_sensor_a0}")

        print(f"Simulação completa: Sensor A0={valor_sensor_a0}, Sensor A1={valor_sensor_a0}")

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
