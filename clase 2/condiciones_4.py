#Ejercicio 03:
#Escribir un programa que determine si un estudiante aprobo o reprobo
#Si la nota es mayor o igual a 7, debe imprimir aprobado
#Si la nota es menor, debe imprimir reprobado

nota = float(input("Ingrese la nota del estudiante: "))

if nota >= 7:
    print("Aprobo")
else:
    print("Reprobo")