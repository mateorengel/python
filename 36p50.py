# Solicitar el valor de n al usuario
n = int(input("Ingrese el valor de n: "))

# Encontrar la suma de los divisores propios de un número
for num1 in range(1, n + 1):
    suma_divisores_num1 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            suma_divisores_num1 += i

    for num2 in range(num1 + 1, n + 1):
        suma_divisores_num2 = 0
        for j in range(1, num2):
            if num2 % j == 0:
                suma_divisores_num2 += j

        if suma_divisores_num1 == num2 and suma_divisores_num2 == num1:
            print(f"{num1} y {num2} son números amigos")

# Ejemplo de salida para n = 300:
# Ingrese el valor de n: 300
# 220 y 284 son números amigos
