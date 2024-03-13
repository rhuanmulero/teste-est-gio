import tkinter as tk

class LampadaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descobrir Interruptores")
        
        self.estado_lampadas = [False, False, False]  # Estado inicial das lâmpadas
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_instrucao = tk.Label(self.root, text="Pressione os interruptores e clique no botão para verificar as lâmpadas:")
        self.label_instrucao.pack(pady=10)
        
        self.interruptor1 = tk.Button(self.root, text="Interruptor 1", command=lambda: self.toggle_interruptor(1))
        self.interruptor1.pack(pady=5)
        
        self.interruptor2 = tk.Button(self.root, text="Interruptor 2", command=lambda: self.toggle_interruptor(2))
        self.interruptor2.pack(pady=5)
        
        self.interruptor3 = tk.Button(self.root, text="Interruptor 3", command=lambda: self.toggle_interruptor(3))
        self.interruptor3.pack(pady=5)
        
        self.verificar_button = tk.Button(self.root, text="Verificar Lâmpadas", command=self.verificar_lampadas)
        self.verificar_button.pack(pady=10)
        
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack(pady=10)
        
    def toggle_interruptor(self, num_interruptor):
        self.estado_lampadas[num_interruptor - 1] = not self.estado_lampadas[num_interruptor - 1]
        print("Interruptor", num_interruptor, "clicado. Estado das lâmpadas:", self.estado_lampadas)
        
    def verificar_lampadas(self):
        liga = sum(self.estado_lampadas)
        if liga == 0:
            self.resultado_label.config(text="Nenhuma lâmpada acesa. Todos os interruptores controlam a lâmpada 3.")
        elif liga == 1:
            index_lampada_acesa = self.estado_lampadas.index(True)
            self.resultado_label.config(text=f"A lâmpada {index_lampada_acesa + 1} está acesa. O interruptor {index_lampada_acesa + 1} controla essa lâmpada.")
        else:
            self.resultado_label.config(text="Mais de uma lâmpada acesa. Algo deu errado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LampadaApp(root)
    root.mainloop()
