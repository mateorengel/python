# Función para convertir una fecha (año, mes, día) en el número total de días
def convertir_a_dias(año, mes, dia):
    return año * 360 + mes * 30 + dia

# Leer la primera fecha
año1 = int(input("Ingrese el año de la primera fecha: "))
mes1 = int(input("Ingrese el mes de la primera fecha: "))
dia1 = int(input("Ingrese el día de la primera fecha: "))

# Leer la segunda fecha
año2 = int(input("Ingrese el año de la segunda fecha: "))
mes2 = int(input("Ingrese el mes de la segunda fecha: "))
dia2 = int(input("Ingrese el día de la segunda fecha: "))

# Convertir ambas fechas a días
dias1 = convertir_a_dias(año1, mes1, dia1)
dias2 = convertir_a_dias(año2, mes2, dia2)

# Calcular la diferencia en días
diferencia_dias = abs(dias2 - dias1)

# Mostrar la diferencia en días
print(f"La diferencia en días entre las dos fechas es: {diferencia_dias} días.")