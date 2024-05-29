# Leer un número entero
numero = int(input("Ingrese un número entero: "))

# Manejar el caso del signo negativo
es_negativo = numero < 0
if es_negativo:
    numero = -numero

# Invertir el número usando operaciones matemáticas
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

# Restaurar el signo negativo si es necesario
if es_negativo:
    numero_invertido = -numero_invertido

# Mostrar el número invertido
print(f"El número invertido es: {numero_invertido}")