#Escribe un programa que calcule el perímetro de un polígono. 
# Empieza por pedir al usuario el valor de x y y del primer punto del perímetro. 
# Luego continua leyendo pares de coordendas x y y hasta que el usuario ingrese una línea en blanco para la coordenanda x,
# cada vez que se ingrese un nuevo par de coordenadas se debe calcular la distancia entre el anterior punto y el nuevo. 
# Cuando se ingrese una linea blanca en la coordenada x, se debe calcular la distancia entre el último punto ingresado y el primer punto, para cerrar el polígono.

# Inicializar las listas para almacenar las coordenadas
x_coords = []
y_coords = []

# Leer el primer punto del perímetro
x = input("Ingrese la coordenada x del primer punto: ")
y = input("Ingrese la coordenada y del primer punto: ")

# Agregar el primer punto a las listas
x_coords.append(int(x))
y_coords.append(int(y))

# Continuar leyendo pares de coordenadas hasta que se ingrese una línea en blanco para x
while True:
    x = input("Ingrese la coordenada x del siguiente punto (deje en blanco para terminar): ")
    if x == "":
        break
    y = input("Ingrese la coordenada y del siguiente punto: ")
    
    # Agregar el nuevo punto a las listas
    x_coords.append(int(x))
    y_coords.append(int(y))

# Calcular el perímetro del polígono
perimetro = 0

# Calcular la distancia entre el anterior punto y el nuevo punto
for i in range(1, len(x_coords)):
    dx = x_coords[i] - x_coords[i - 1]
    dy = y_coords[i] - y_coords[i - 1]
    distancia = (dx * dx + dy * dy) ** 0.5
    perimetro += distancia

# Calcular la distancia entre el último punto ingresado y el primer punto
dx = x_coords[0] - x_coords[-1]
dy = y_coords[0] - y_coords[-1]
distancia = (dx * dx + dy * dy) ** 0.5
perimetro += distancia

# Imprimir el perímetro del polígono
print("El perímetro del polígono es:", perimetro)
