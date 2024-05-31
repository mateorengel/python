# Solicitar al usuario el número de cubos a generar
n = int(input("Ingrese el número de cubos a generar: "))

# Inicializar la variable para almacenar el número de cubo
cubo = 1

# Inicializar el número impar inicial
impar = 1

# Generar los n primeros cubos
for i in range(n):
    # Inicializar la suma de los números impares secuenciales para cada cubo
    suma_impares = 0
    
    # Imprimir la secuencia de números impares para el cubo actual
    for j in range(i + 1):
        print(impar, end=" ")
        suma_impares += impar
        impar += 2
    
    # Calcular el cubo actual e imprimirlo
    cubo = suma_impares ** 3
    print("= ", cubo)
