# Solicitar el primer punto al usuario
x1 = input("Ingrese la coordenada x del primer punto (o presione Enter para terminar): ")

if x1 != "":
    x1 = float(x1)
    y1 = float(input("Ingrese la coordenada y del primer punto: "))

    # Inicializar las variables para almacenar los puntos inicial y anterior
    x_inicial = x1
    y_inicial = y1
    x_anterior = x1
    y_anterior = y1

    # Inicializar el perímetro
    perimetro = 0

    while True:
        # Solicitar el siguiente punto al usuario
        x = input("Ingrese la coordenada x del siguiente punto (o presione Enter para terminar): ")
        if x == "":
            break
        y = float(input("Ingrese la coordenada y del siguiente punto: "))
        x = float(x)

        # Calcular la distancia entre el punto anterior y el nuevo punto
        distancia = ((x - x_anterior) ** 2 + (y - y_anterior) ** 2) ** 0.5
        perimetro += distancia

        # Actualizar el punto anterior
        x_anterior = x
        y_anterior = y

    # Calcular la distancia entre el último punto y el primer punto para cerrar el polígono
    distancia = ((x_inicial - x_anterior) ** 2 + (y_inicial - y_anterior) ** 2) ** 0.5
    perimetro += distancia

    # Imprimir el perímetro del polígono
    print("El perímetro del polígono es:", perimetro)
else:
    print("No se ingresaron suficientes puntos para formar un polígono.")
