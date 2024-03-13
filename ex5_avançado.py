import tkinter as tk

class InverterStringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inverter String")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_instrucao = tk.Label(self.root, text="Digite uma frase e clique no botão para inverter:")
        self.label_instrucao.pack(pady=10)
        
        self.input_entry = tk.Entry(self.root, width=30)
        self.input_entry.pack(pady=5)
        
        self.inverter_button = tk.Button(self.root, text="Inverter", command=self.inverter_string)
        self.inverter_button.pack(pady=5)
        
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack(pady=10)
        
    def inverter_string(self):
        entrada = self.input_entry.get()
        string_invertida = self.inverter(entrada)
        self.resultado_label.config(text="String invertida: " + string_invertida)
        
    def inverter(self, string):
        inverted_string = ""
        for i in range(len(string) - 1, -1, -1):
            inverted_string += string[i]
        return inverted_string

if __name__ == "__main__":
    root = tk.Tk()
    app = InverterStringApp(root)
    root.mainloop()
