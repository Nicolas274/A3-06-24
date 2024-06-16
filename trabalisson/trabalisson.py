import customtkinter as ctk
import tkinter as tk

# Configuração inicial do customtkinter
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

class SemPararApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela principal
        self.title("App Sem Parar")
        self.geometry("600x400")
        self.configure(bg='black')  # Fundo preto
        self.center_window(600, 400)  # Centraliza a janela principal

        # Label para mostrar o saldo do cliente
        self.saldo_label = ctk.CTkLabel(self, text="Saldo do Cliente: R$ 100,00", text_color="white", font=("Arial", 24))
        self.saldo_label.pack(pady=20)

        # Botão para cadastro do veículo
        self.cadastro_veiculo_button = ctk.CTkButton(self, text="Cadastro do Veículo", command=self.open_cadastro_veiculo)
        self.cadastro_veiculo_button.pack(pady=10)

        # Botão para cálculo de rota
        self.calculo_rota_button = ctk.CTkButton(self, text="Cálculo de Rota", command=self.open_calculo_rota)
        self.calculo_rota_button.pack(pady=10)

        # Botão para adicionar saldo
        self.adicionar_saldo_button = ctk.CTkButton(self, text="Adicionar Saldo", command=self.open_adicionar_saldo)
        self.adicionar_saldo_button.pack(pady=10)

    def open_cadastro_veiculo(self):
        self.withdraw()  # Esconde a janela principal
        CadastroVeiculoWindow(self)

    def open_calculo_rota(self):
        self.withdraw()  # Esconde a janela principal
        CalculoRotaWindow(self)

    def open_adicionar_saldo(self):
        self.withdraw()  # Esconde a janela principal
        AdicionarSaldoWindow(self)

    def center_window(self, width, height):
        # Centraliza a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

class CadastroVeiculoWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Cadastro do Veículo")
        self.geometry("400x300")
        self.configure(bg='black')
        self.center_window(400, 300)  # Centraliza a janela secundária

        # Exemplo de conteúdo para a janela de cadastro de veículo
        self.label = ctk.CTkLabel(self, text="Janela de Cadastro do Veículo", text_color="white")
        self.label.pack(pady=20)

        # Fecha a janela ao clicar no botão e reabre a janela principal
        self.close_button = ctk.CTkButton(self, text="Fechar", command=self.close_window)
        self.close_button.pack(pady=10)

    def close_window(self):
        self.parent.deiconify()  # Mostra novamente a janela principal
        self.destroy()  # Fecha a janela atual

    def center_window(self, width, height):
        # Centraliza a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

class CalculoRotaWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Cálculo de Rota")
        self.geometry("400x300")
        self.configure(bg='black')
        self.center_window(400, 300)  # Centraliza a janela secundária

        # Exemplo de conteúdo para a janela de cálculo de rota
        self.label = ctk.CTkLabel(self, text="Janela de Cálculo de Rota", text_color="white")
        self.label.pack(pady=20)

        # Fecha a janela ao clicar no botão e reabre a janela principal
        self.close_button = ctk.CTkButton(self, text="Fechar", command=self.close_window)
        self.close_button.pack(pady=10)

    def close_window(self):
        self.parent.deiconify()  # Mostra novamente a janela principal
        self.destroy()  # Fecha a janela atual

    def center_window(self, width, height):
        #Centraliza a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

class AdicionarSaldoWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Adicionar Saldo")
        self.geometry("400x300")
        self.configure(bg='black')
        self.center_window(400, 300)  #Centraliza a janela secundária

        #Exemplo de conteúdo para a janela de adicionar saldo
        self.label = ctk.CTkLabel(self, text="Janela de Adicionar Saldo", text_color="white")
        self.label.pack(pady=20)

        #Fecha a janela ao clicar no botão e reabre a janela principal
        self.close_button = ctk.CTkButton(self, text="Fechar", command=self.close_window)
        self.close_button.pack(pady=10)

    def close_window(self):
        self.parent.deiconify()  #Mostra novamente a janela principal
        self.destroy()  #Fecha a janela atual

    def center_window(self, width, height):
        #Centraliza a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

# Executa a aplicação
if __name__ == "__main__":
    app = SemPararApp()
    app.mainloop()
