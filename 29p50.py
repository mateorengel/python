# Solicitar los números y la operación al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

# Inicializar el resultado
resultado = None

# Realizar la operación solicitada
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 == 0:
        resultado = "Error: División por cero"
    else:
        resultado = num1 / num2
else:
    resultado = "Operación no válida"

# Mostrar el resultado
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
