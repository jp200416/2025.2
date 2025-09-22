try:
    numero_decimal = int(input("Digite um número inteiro para converter em binário: "))
    
    binario_com_prefixo = bin(numero_decimal)
    
    binario_sem_prefixo = binario_com_prefixo[2:]
    
    print(f"O número {numero_decimal} em binário é: {binario_sem_prefixo}")
    
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")