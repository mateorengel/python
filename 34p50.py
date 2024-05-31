# Solicitar el valor de n al usuario
n = int(input("Ingrese el valor de n: "))

# Generar las secuencias
for i in range(n, 0, -1):  # Bucle exterior que controla la longitud de cada secuencia
    for j in range(1, i + 1):  # Bucle interior que genera cada secuencia
        print(j, end=" ")
    print()  # Imprimir nueva línea después de cada secuencia
