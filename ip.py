def converter_ip():
    """
    Recebe um endereço de IP em formato decimal, valida-o
    e exibe cada octeto em decimal e binário.
    """
    try:
        ip_decimal_str = input("Digite um endereço de IP (ex: 192.168.1.1): ")
        
        # Divide a string do IP em uma lista de strings de octetos
        octetos_str = ip_decimal_str.split('.')
        
        # Verifica se o IP tem exatamente 4 octetos
        if len(octetos_str) != 4:
            print("Erro: O endereço de IP deve conter 4 octetos separados por pontos.")
            return

        print("\n--- Conversão do IP ---")
        
        # Converte cada octeto e exibe os resultados
        for i, octeto_str in enumerate(octetos_str):
            # Tenta converter o octeto para um número inteiro
            octeto_decimal = int(octeto_str)
            
            # Valida se o octeto está no intervalo de 0 a 255
            if not (0 <= octeto_decimal <= 255):
                print(f"Erro: O octeto '{octeto_str}' não é válido. Os octetos devem estar entre 0 e 255.")
                return
            
            # Converte o octeto decimal para binário
            # bin() retorna uma string do tipo '0bXXXX'
            # O fatiamento [2:] remove o prefixo '0b'
            octeto_binario_sem_prefixo = bin(octeto_decimal)[2:]
            
            # Adiciona zeros à esquerda para garantir 8 bits (o formato de um octeto)
            octeto_binario_completo = octeto_binario_sem_prefixo.zfill(8)
            
            print(f"Octeto {i + 1}:")
            print(f"  Decimal: {octeto_decimal}")
            print(f"  Binário: {octeto_binario_completo}")
            print("-" * 20)

    except ValueError:
        print("Erro: O endereço de IP contém caracteres inválidos. Digite apenas números e pontos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa a função principal do programa
converter_ip()