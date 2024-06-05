# Imprimir la cabecera de la tabla
print("Celsius\tFahrenheit")

# Iterar sobre las temperaturas de 0 a 100 grados Celsius en múltiplos de 10
for celsius in range(0, 101, 10):
    # Calcular la temperatura en Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32
    # Imprimir la temperatura en Celsius y su equivalente en Fahrenheit
    print(f"{celsius}\t{fahrenheit:.1f}")
