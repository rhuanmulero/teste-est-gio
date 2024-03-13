import tkinter as tk
from tkinter import messagebox

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return True
    else:
        return False

def verificar_numero():
    entrada = entry_numero.get()
    
    if entrada.lower() == "sair":
        messagebox.showinfo("Informação", "Programa encerrado.")
        root.quit()
        return
    
    try:
        numero_desejado = int(entrada)
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida. Por favor, insira um número válido ou 'Sair' para sair.")
        return
    
    sequencia_fibonacci = fibonacci(numero_desejado)
    mensagem = f"A sequência de Fibonacci até o número {numero_desejado} é: {sequencia_fibonacci}\n"
    if verifica_pertence(numero_desejado, sequencia_fibonacci):
        mensagem += f"{numero_desejado} pertence à sequência de Fibonacci."
    else:
        mensagem += f"{numero_desejado} não pertence à sequência de Fibonacci."
    
    messagebox.showinfo("Resultado", mensagem)

root = tk.Tk()
root.title("Verificador de Sequência de Fibonacci")

label_numero = tk.Label(root, text="Digite um número (ou 'Sair' para encerrar):")
label_numero.pack()

entry_numero = tk.Entry(root)
entry_numero.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar_numero)
button_verificar.pack()

root.mainloop()
