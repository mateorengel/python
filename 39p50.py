# Solicitar los valores de N y M al usuario
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

# Intentar encontrar capicúas en el rango de N a M
for num in range(N, M + 1):
    print(f"Procesando el número {num}...")
    original = num
    iteraciones = 0
    encontrado_capicua = False
    
    while True:
        # Verificar si el número actual es capicúa
        if str(original) == str(original)[::-1]:
            encontrado_capicua = True
            break
        
        # Invertir el número actual
        invertido = 0
        temp = original
        while temp > 0:
            invertido = invertido * 10 + temp % 10
            temp //= 10
        
        # Sumar el número original y el invertido
        original += invertido
        iteraciones += 1
        print(f"Iteración {iteraciones}: {original}")
        
        # Evitar bucles infinitos (por ejemplo, si no se encuentra un capicúa en 1000 iteraciones)
        if iteraciones > 1000:
            break
    
    if encontrado_capicua:
        print(f"El número {num} se convirtió en el capicúa {original} en {iteraciones} iteraciones.")
    else:
        print(f"No se pudo convertir el número {num} en un capicúa.")
