# Solicitar al usuario el monto
monto = float(input("Ingrese el monto: "))

# Definir los valores de los billetes y monedas disponibles
valores = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]

# Inicializar un diccionario para contar la cantidad de cada billete o moneda necesaria
cantidad = {}

# Iterar sobre los valores de los billetes y monedas
for valor in valores:
    # Calcular la cantidad de billetes o monedas necesarias para el monto actual
    cantidad[valor] = int(monto // valor)
    # Actualizar el monto restando el valor de los billetes o monedas ya considerados
    monto -= cantidad[valor] * valor

# Imprimir la cantidad de cada billete o moneda necesaria
for valor, cant in cantidad.items():
    if cant > 0:
        if valor >= 1:
            print(f"{cant} billetes de {valor} Bs")
        else:
            print(f"{cant} monedas de {valor} Bs")
