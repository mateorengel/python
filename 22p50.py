# Inicializar el total de la compra en 0
total_compra = 0.0

# Bucle para solicitar los artículos y sus precios
while True:
    # Solicitar el precio del artículo
    precio = input("Ingrese el precio del artículo (o presione Enter para finalizar): ")
    
    # Verificar si el usuario ha terminado de ingresar artículos
    if precio == "":
        break
    
    # Convertir el precio a un número flotante
    precio = float(precio)
    
    # Solicitar la cantidad del artículo
    cantidad = int(input("Ingrese la cantidad del artículo: "))
    
    # Calcular el costo total del artículo actual y sumarlo al total de la compra
    total_compra += precio * cantidad

# Mostrar el total de la compra
print(f"El total de la compra es: {total_compra:.2f}")