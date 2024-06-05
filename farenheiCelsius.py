#Escribe un programa que imprima un tabla de conversión de temperaturas de grados Celsius a grados Fahrenheit. 
# La tabla debe incluir filas para todas las temperaturas de 0 a 100 grados Celsius en multiplos de 10, 
# con su conversión a Fahrenheit. Incluya una cabecera apropiada para las columnas de la tabla. La formula de conversión de pueden encontrarla en internet
# Inicializar las listas
celsius_list = []
fahrenheit_list = []

# Calcular las temperaturas y llenar las listas
celsius = 0
while celsius <= 100:
    fahrenheit = celsius * 9 / 5 + 32
    celsius_list.append(celsius)
    fahrenheit_list.append(fahrenheit)
    celsius += 10

# Imprimir la cabecera de la tabla
print("Celsius\tFahrenheit")

# Imprimir las filas de la tabla utilizando las listas
for i in range(len(celsius_list)):
    print(celsius_list[i], "\t", fahrenheit_list[i])
