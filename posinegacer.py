# Crear una lista para almacenar los números
numeros = []

# Pedir al usuario que ingrese 20 números enteros
print("Ingrese 20 números enteros (positivos, ceros o negativos):")
for i in range(20):
    numero = int(input(f"Numero {i+1}: "))
    numeros.append(numero)

# Inicializar contadores para negativos, ceros y positivos
cantidad_negativos = 0
cantidad_ceros = 0
cantidad_positivos = 0

# Contar negativos, ceros y positivos
for numero in numeros:
    if numero < 0:
        cantidad_negativos += 1
    elif numero == 0:
        cantidad_ceros += 1
    else:
        cantidad_positivos += 1

# Ordenar la lista de menor a mayor usando un algoritmo de ordenamiento (burbuja)
for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Mostrar los resultados
print(f"Cantidad de números negativos: {cantidad_negativos}")
print(f"Cantidad de ceros: {cantidad_ceros}")
print(f"Cantidad de números positivos: {cantidad_positivos}")
print("Lista de números ordenada de menor a mayor:")
print(numeros)