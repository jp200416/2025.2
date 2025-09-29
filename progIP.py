print("--- Calculadora de Endereço de Rede e Último Host (Manual) ---")
print("Exemplo de entrada: 192.168.1.50/24")
entrada = input("Digite o IP com o prefixo CIDR (ex: 192.168.1.50/24): ").strip()

try:
    ip_string, prefixo_string = entrada.split('/')
    prefixo = int(prefixo_string)
    ip_octetos = [int(x) for x in ip_string.split('.')]
except ValueError:
    print("\nERRO: Formato de entrada inválido. Use o formato IP/Prefixo (ex: 192.168.1.50/24).")
    exit()

mascara_binaria = '1' * prefixo + '0' * (32 - prefixo)
mascara_octetos = []

for i in range(0, 32, 8):
    octeto_binario = mascara_binaria[i:i+8]
    mascara_octetos.append(int(octeto_binario, 2))

rede_octetos = []
for ip, mask in zip(ip_octetos, mascara_octetos):
    rede_octetos.append(ip & mask)

broadcast_octetos = []
for i in range(4):
     broadcast_octetos.append(rede_octetos[i] | (255 - mascara_octetos[i]))


endereco_rede = ".".join(map(str, rede_octetos))
endereco_broadcast = ".".join(map(str, broadcast_octetos))

broadcast_int = (broadcast_octetos[0] << 24) + \
                (broadcast_octetos[1] << 16) + \
                (broadcast_octetos[2] << 8) + \
                broadcast_octetos[3]

ultimo_host_int = broadcast_int - 1

if prefixo < 31:
    ultimo_host_octetos = [
        (ultimo_host_int >> 24) & 0xFF,
        (ultimo_host_int >> 16) & 0xFF,
        (ultimo_host_int >> 8) & 0xFF,
        ultimo_host_int & 0xFF
    ]
    ultimo_host = ".".join(map(str, ultimo_host_octetos))
elif prefixo == 31:
    ultimo_host = "N/A (Rede Ponto-a-Ponto, sem hosts utilizáveis tradicionais)"
else:
     ultimo_host = "N/A (Host Único)"

print("\n--- Resultado ---")
print(f"Endereço de Rede (Network ID): {endereco_rede}")
print(f"Endereço de Broadcast: {endereco_broadcast}")
print(f"Último Host Utilizável: {ultimo_host}")