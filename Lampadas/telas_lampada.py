import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Entry, StringVar
import serial
import serial.tools.list_ports
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Painel de Controle de Luzes IoT")
        self.geometry("650x600") 
        
        self.arduino = None 

        conn_frame = Frame(self, bd=2, relief=tk.GROOVE)
        conn_frame.pack(padx=10, pady=10, fill=tk.X)

        Label(conn_frame, text="Porta COM do Arduino:").pack(side=tk.LEFT, padx=5)
        
        porta_sugerida = self.find_arduino_port()
        self.port_entry_var = StringVar(value=porta_sugerida or "Digite a porta (ex: COM3)")
        self.port_entry = Entry(conn_frame, textvariable=self.port_entry_var, width=25)
        self.port_entry.pack(side=tk.LEFT, padx=5)

        self.connect_button = Button(conn_frame, text="Conectar", command=self.toggle_connection)
        self.connect_button.pack(side=tk.LEFT, padx=5)

        self.status_label = Label(self, text="Status: Desconectado", fg="red", pady=5)
        self.status_label.pack()

        main_frame = Frame(self)
        main_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        setores = {
            "Oficina": ('A', 'a'),
            "Galpão - Bloco 1": ('B', 'b'),
            "Galpão - Bloco 2": ('C', 'c'),
            "Galpão - Bloco 3": ('D', 'd'),
            "Escritório": ('E', 'e'),
            "Corredor": ('F', 'f'),
            "Área de Serviço": ('G', 'g'),
            "Área Externa": ('H', 'h')
        }

        for i, (nome, chars) in enumerate(setores.items()):
            row = i // 2
            col = i % 2
            
            setor_frame = Frame(main_frame, bd=1, relief=tk.SOLID)
            setor_frame.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

            Label(setor_frame, text=nome, width=20, font=("Helvetica", 10, "bold")).pack(pady=(5,0))
            
            btn_frame = Frame(setor_frame)
            btn_frame.pack(pady=5)
       
            ligar_btn = Button(btn_frame, text="Ligar", bg="#90EE90", command=lambda c=chars[0]: self.send_command(c))
            ligar_btn.pack(side=tk.LEFT, padx=10)

            desligar_btn = Button(btn_frame, text="Desligar", bg="#F08080", command=lambda c=chars[1]: self.send_command(c))
            desligar_btn.pack(side=tk.LEFT, padx=10)
        
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        galpao_general_frame = Frame(self, bd=2, relief=tk.GROOVE)
        galpao_general_frame.pack(padx=10, pady=10, fill=tk.X)
        Label(galpao_general_frame, text="Comandos do Galpão (Blocos 1, 2, 3)", font=("Helvetica", 12, "bold")).pack()
        
        btn_frame_galpao = Frame(galpao_general_frame)
        btn_frame_galpao.pack(pady=10)

        ligar_galpoes_btn = Button(btn_frame_galpao, text="Ligar Galpões", font=("Helvetica", 10), bg="#4682B4", fg="white", width=18, command=lambda: self.send_command('5'))
        ligar_galpoes_btn.pack(side=tk.LEFT, padx=20)

        desligar_galpoes_btn = Button(btn_frame_galpao, text="Desligar Galpões", font=("Helvetica", 10), bg="#696969", fg="white", width=18, command=lambda: self.send_command('4'))
        desligar_galpoes_btn.pack(side=tk.LEFT, padx=20)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def find_arduino_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "CH340" in port.description or "USB-SERIAL CH340" in port.description:
                return port.device
        return None

    def toggle_connection(self):
        if self.arduino and self.arduino.is_open:
            self.disconnect()
        else:
            self.connect()

    def connect(self):
        port = self.port_entry.get()
        try:
            self.arduino = serial.Serial(port, 9600, timeout=1)
            time.sleep(2) 
            
            self.status_label.config(text=f"Status: Conectado a {port}", fg="green")
            self.connect_button.config(text="Desconectar")
            print(f"Conexão com {port} estabelecida.")

        except serial.SerialException as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar à porta {port}.\nVerifique a porta e tente novamente.\n\nErro: {e}")
            self.arduino = None

    def disconnect(self):
        if self.arduino:
            self.arduino.close()
            self.status_label.config(text="Status: Desconectado", fg="red")
            self.connect_button.config(text="Conectar")
            print("Conexão encerrada.")

    def send_command(self, char_command):
        if self.arduino and self.arduino.is_open:
            try:
                self.arduino.write(char_command.encode('utf-8'))
                print(f"Comando enviado: '{char_command}'")
            except Exception as e:
                messagebox.showerror("Erro de Comunicação", f"Falha ao enviar dados: {e}")
                self.disconnect() 
        else:
            messagebox.showwarning("Não Conectado", "Por favor, conecte ao Arduino primeiro.")

    def on_closing(self):
        self.disconnect()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()