def inverter_string(string):
    # Inicializa uma string vazia para armazenar o resultado da inversão
    inverted_string = ""
    
    # Percorre a string de trás para frente e concatenamos cada caractere à nova string
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    
    return inverted_string

# Exemplo de utilização
entrada = input("Digite um texto para inverter: ")
string_invertida = inverter_string(entrada)
print("String invertida:", string_invertida)
