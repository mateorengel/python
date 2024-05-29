# Leer tres números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar que los tres números sean distintos
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Los números no son distintos. Inténtelo de nuevo.")
else:
    # Crear una lista con los números
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de mayor a menor
    numeros_ordenados = sorted(numeros, reverse=True)
    
    # Mostrar los números ordenados
    print("Números ordenados de mayor a menor:", numeros_ordenados)
