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

while True:
    entrada = input("Digite um número para verificar se pertence à sequência de Fibonacci (ou 'Sair' para sair): ")
    
    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break
    
    try:
        numero_desejado = int(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido ou 'Sair' para sair.")
        continue
    
    sequencia_fibonacci = fibonacci(numero_desejado)
    print("A sequência de Fibonacci até o número", numero_desejado, "é:", sequencia_fibonacci)

    if verifica_pertence(numero_desejado, sequencia_fibonacci):
        print(numero_desejado, "pertence à sequência de Fibonacci.")
    else:
        print(numero_desejado, "não pertence à sequência de Fibonacci.")
