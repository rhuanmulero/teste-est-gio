import tkinter as tk

def next_elements():
    # Função para calcular os próximos elementos das sequências
    
    # Sequência a)
    next_a = a_sequence[-1] + 2
    label_a.config(text=f"a) 1, 3, 5, 7, ___ {next_a}")

    # Sequência b)
    next_b = b_sequence[-1] * 2
    label_b.config(text=f"b) 2, 4, 8, 16, 32, 64, ____ {next_b}")

    # Sequência c)
    next_c = c_sequence[0] + 7**2
    label_c.config(text=f"c) 0, 1, 4, 9, 16, 25, 36, ____ {next_c}")

    # Sequência d)
    next_d = 10**2
    label_d.config(text=f"d) 4, 16, 36, 64, ____ {next_d}")

    # Sequência e)
    next_e = e_sequence[-1] + e_sequence[-2]
    label_e.config(text=f"e) 1, 1, 2, 3, 5, 8, ____ {next_e}")

    # Sequência f)
    next_f = f_sequence[-1] + 1
    label_f.config(text=f"f) 2, 10, 12, 16, 17, 18, 19, ____ {next_f}")

# Criar a janela principal
root = tk.Tk()
root.title("Próximo Elemento")

# Sequências dadas
a_sequence = [1, 3, 5, 7]
b_sequence = [2, 4, 8, 16, 32, 64]
c_sequence = [0, 1, 4, 9, 16, 25, 36]
d_sequence = [4, 16, 36, 64]
e_sequence = [1, 1, 2, 3, 5, 8]
f_sequence = [2, 10, 12, 16, 17, 18, 19]

# Criar rótulos para exibir os resultados
label_a = tk.Label(root, text="a) 1, 3, 5, 7, ___")
label_a.pack()
label_b = tk.Label(root, text="b) 2, 4, 8, 16, 32, 64, ____")
label_b.pack()
label_c = tk.Label(root, text="c) 0, 1, 4, 9, 16, 25, 36, ____")
label_c.pack()
label_d = tk.Label(root, text="d) 4, 16, 36, 64, ____")
label_d.pack()
label_e = tk.Label(root, text="e) 1, 1, 2, 3, 5, 8, ____")
label_e.pack()
label_f = tk.Label(root, text="f) 2, 10, 12, 16, 17, 18, 19, ____")
label_f.pack()

# Botão para calcular os próximos elementos
calculate_button = tk.Button(root, text="Calcule", command=next_elements)
calculate_button.pack()

# Rodar a aplicação
root.mainloop()
