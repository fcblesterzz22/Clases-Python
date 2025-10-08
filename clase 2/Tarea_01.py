#Ejercicio 4
# Escribir un programa que determine el rango de edad de una persona.
# Si la edad es menor de 12 años, debe imprimir "Niño".
# Si la edad está entre 12 y 18 años, debe imprimir "Adolescente".
# Si es mayor de 18 años, debe imprimir "Adulto".

edad = int(input("Por favor, escriba su edad: "))
if edad <= 12:
    print("Niño")
elif edad >= 12 <= 18:
    print("Adolescente")
else:
    print("Adulto")