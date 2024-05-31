# Solicitar el primer número entero al usuario
num1 = int(input("Ingrese el primer número entero: "))

# Solicitar el segundo número entero al usuario
num2 = int(input("Ingrese el segundo número entero: "))

# Verificar que los números sean distintos
if num1 == num2:
    print("Los números deben ser distintos.")
else:
    # Generar la serie dependiendo del orden de los números
    if num1 > num2:
        # Serie descendente
        print("Serie descendente:")
        for i in range(num1, num2 - 1, -1):
            print(i, end=' ')
    else:
        # Serie ascendente
        print("Serie ascendente:")
        for i in range(num1, num2 + 1):
            print(i, end=' ')