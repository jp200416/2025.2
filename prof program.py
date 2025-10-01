# Operações bit a bit (bitwise) com strings em Python
strTexto_1 = 'P'
strTexto_2 = 'd'

# --- 1. Exibir Entradas ---
print(f'Texto 1................: {strTexto_1} -> ASCII = {ord(strTexto_1):>3}')
print(f'Texto 2................: {strTexto_2} -> ASCII = {ord(strTexto_2):>3}')
print("-" * 40)

# --- 2. Realizar Operações bit a bit (bitwise) ---
# A função ord() converte o caractere para seu valor inteiro (ASCII/Unicode)
andResultado = ord(strTexto_1) & ord(strTexto_2)
orResultado  = ord(strTexto_1) | ord(strTexto_2)
xorResultado = ord(strTexto_1) ^ ord(strTexto_2)

# --- 3. Exibir Resultados ---
# Usamos f-strings para formatar a saída.
# O ">3" garante que o número ASCII tenha pelo menos 3 espaços, alinhando a saída.

print(f'Resultado AND (&): ASCII = {andResultado:>3} -> Caractere = {chr(andResultado)}')
print(f'Resultado OR (|):  ASCII = {orResultado:>3} -> Caractere = {chr(orResultado)}')
print(f'Resultado XOR (^): ASCII = {xorResultado:>3} -> Caractere = {chr(xorResultado)}')