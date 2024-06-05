#aproximaciones de pi

# Inicializar lista para las aproximaciones de pi
aproximaciones_pi = []

# Calcular las aproximaciones de pi
for i in range(1, 16):  # 15 aproximaciones
    suma = 0
    for j in range(1, i + 1):
        term = 4 / ((2 * j) * (2 * j + 1) * (2 * j + 2))
        if j % 2 == 0:
            suma -= term
        else:
            suma += term
    aproximaciones_pi.append(suma)

# Imprimir las aproximaciones de pi
for idx, aprox in enumerate(aproximaciones_pi):
    print(f"Aproximación {idx + 1}: {aprox}")