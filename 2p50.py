# Leer dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si uno es múltiplo del otro
if numero1 % numero2 == 0:
    print(f"{numero1} es múltiplo de {numero2}.")
elif numero2 % numero1 == 0:
    print(f"{numero2} es múltiplo de {numero1}.")
else:
    print(f"Ni {numero1} ni {numero2} son múltiplos uno del otro.")
