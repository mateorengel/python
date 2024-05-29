import math

# Leer los coeficientes de la ecuación de segundo grado
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Determinar las soluciones basadas en el valor del discriminante
if discriminante > 0:
    # Dos soluciones reales y distintas
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son: x1 = {x1} y x2 = {x2}")
elif discriminante == 0:
    # Una solución real (raíz doble)
    x = -b / (2*a)
    print(f"Hay una solución real: x = {x}")
else:
    # No hay soluciones reales
    print("No existen soluciones reales.")