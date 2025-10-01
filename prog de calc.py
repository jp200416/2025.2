valor_1 = 195
valor_2 = 89

#1. Operação AND bit a bit (&)

and_result = valor_1 & valor_2

#2. Operação OR bit a bit (|)

or_result = valor_1 | valor_2


#3. Operação XOR bit a bit (^)

xor_result = valor_1 ^ valor_2

print(f"Valor 1: {valor_1} (binário: {valor_1:08b})")
print(f"Valor 2: {valor_2} (binário: {valor_2:08b})")
print("-" * 30)

print(f"valor_1 & valor_2 = {and_result}")
print(f"  Em binário: {and_result:08b}")
print("-" * 30)

print(f"valor_1 | valor_2 = {or_result}")
print(f"  Em binário: {or_result:08b}")
print("-" * 30)

print(f"valor_1 ^ valor_2 = {xor_result}")
print(f"  Em binário: {xor_result:08b}")