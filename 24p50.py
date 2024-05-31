# Solicitar la cantidad de vendedoras
n = int(input("Ingrese la cantidad de vendedoras: "))

# Inicializar listas para almacenar la información de cada vendedora
antiguedades = []
total_vendidos = []
sueldos_basicos = []
comisiones = []
sueldos_totales = []

# Solicitar la información de cada vendedora
for i in range(n):
    print(f"\nVendedora {i + 1}")
    antiguedad = int(input("Ingrese la antigüedad en años: "))
    total_vendido = float(input("Ingrese el total vendido en el mes: "))

    # Sueldo básico basado en antigüedad
    sueldo_basico = 1000 + (antiguedad * 50)  # Ejemplo: 1000 de base + 50 por cada año de antigüedad
    
    # Comisión por ventas
    comision = 0.10 * total_vendido
    
    # Sueldo total
    sueldo_total = sueldo_basico + comision
    
    # Almacenar la información
    antiguedades.append(antiguedad)
    total_vendidos.append(total_vendido)
    sueldos_basicos.append(sueldo_basico)
    comisiones.append(comision)
    sueldos_totales.append(sueldo_total)

# Mostrar el resultado
for i in range(n):
    print(f"\nVendedora {i + 1}:")
    print(f"Antigüedad: {antiguedades[i]} años")
    print(f"Total vendido: {total_vendidos[i]:.2f}")
    print(f"Sueldo básico: {sueldos_basicos[i]:.2f}")
    print(f"Comisión: {comisiones[i]:.2f}")
    print(f"Sueldo total: {sueldos_totales[i]:.2f}")