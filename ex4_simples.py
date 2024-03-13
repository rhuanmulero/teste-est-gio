def primeira_visita():
    # Simulando a primeira visita à sala das lâmpadas
    print("Primeira visita à sala das lâmpadas:")
    estado_lampadas = [False, False, False]  # Inicialmente, todas as lâmpadas estão apagadas
    print("Estado inicial das lâmpadas:", estado_lampadas)
    
    # Simulando ligar e desligar os interruptores
    for i in range(3):
        # Ligar o i-ésimo interruptor
        estado_lampadas[i] = True
        print("Interruptor", i+1, "ligado. Estado das lâmpadas:", estado_lampadas)
        
        # Desligar todos os outros interruptores
        for j in range(3):
            if j != i:
                estado_lampadas[j] = False
        print("Todos os outros interruptores desligados. Estado das lâmpadas:", estado_lampadas)

# Função para verificar o estado das lâmpadas na segunda visita
def segunda_visita(interruptor_correto):
    print("\nSegunda visita à sala das lâmpadas:")
    for i in range(3):
        # Simula ligar apenas um interruptor por vez
        estado_lampadas = [False, False, False]
        estado_lampadas[interruptor_correto - 1] = True if i == 0 else False
        print("Testando interruptor", interruptor_correto, "ligado:", estado_lampadas)


# Simulação
primeira_visita()
interruptor_correto = int(input("\nDigite o número do interruptor que controla a lâmpada que está acesa (1, 2 ou 3): "))
segunda_visita(interruptor_correto)
