# Escribir un programa que determine 
# si un número ingresado por el usuario es positivo, negativo o cero.

numero = int(input("Ingrese un numero: "))
if numero > 1:
    print("Tu numero es positivo")
elif numero < 0:
    print("Tu numero es negativo")
else:
    print("Tu numero es 0")