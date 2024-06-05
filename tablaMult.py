# Crear una lista para almacenar las filas de la tabla de multiplicación
tabla = []

# Generar la tabla de multiplicación
for i in range(1, 11):
    fila = []
    for j in range(1, 11):
        fila.append(i * j)
    tabla.append(fila)

# Imprimir la cabecera de la tabla
print("Tabla de multiplicación:")
print()

# Imprimir la tabla de multiplicación
for fila in tabla:
    for valor in fila:
        print(valor, end='\t')
    print()