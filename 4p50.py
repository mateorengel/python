# Leer un número entero
numero = int(input("Ingrese un número entero: "))

# Si el número es negativo, convertirlo a positivo
if numero < 0:
    numero = -numero

# Contar los dígitos usando un bucle
num_digitos = 0
if numero == 0:
    num_digitos = 1
else:
    while numero > 0:
        numero //= 10
        num_digitos += 1

# Mostrar el número de dígitos
print(f"El número tiene {num_digitos} dígitos.")