# Solicitar al usuario el valor numérico
numero = int(input("Ingrese un número entre 1 y 9999: "))

# Validar si el número está en el rango permitido
if 1 <= numero <= 9999:
    # Definir los símbolos y sus valores correspondientes
    simbolos = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    # Inicializar la cadena de número romano
    romano = ''

    # Iterar sobre los valores en orden decreciente
    for valor, simbolo in sorted(simbolos.items(), reverse=True):
        while numero >= valor:
            romano += simbolo
            numero -= valor

    print("El número romano equivalente es:", romano)
else:
    print("El número está fuera del rango permitido.")
