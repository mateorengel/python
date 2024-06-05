# Solicitar la cadena al usuario
cadena = input("Ingrese una cadena: ")

# Convertir la cadena a minúsculas para ignorar diferencias de mayúsculas/minúsculas
cadena_min = ""
for char in cadena:
    if 'A' <= char <= 'Z':
        cadena_min += chr(ord(char) + 32)
    else:
        cadena_min += char

# Eliminar espacios y caracteres no alfabéticos
cadena_limpia = ""
for char in cadena_min:
    if 'a' <= char <= 'z':
        cadena_limpia += char

# Crear la cadena invertida
cadena_invertida = ""
for i in range(len(cadena_limpia) - 1, -1, -1):
    cadena_invertida += cadena_limpia[i]

# Verificar si la cadena es palíndroma
es_palindroma = True
for i in range(len(cadena_limpia)):
    if cadena_limpia[i] != cadena_invertida[i]:
        es_palindroma = False
        break

# Imprimir el resultado
if es_palindroma:
    print("Es palíndroma")
else:
    print("No es palíndroma")