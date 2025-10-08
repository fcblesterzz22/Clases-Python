#escribir un programa que verifique si un numero ingresado por el usuario es mayor, o menor o igual a 10.
     
#input representa pedirle una consulta al usuario

numero = int(input("Ingresa un número: "))
if numero > 10:
    print("El número es mayor que 10")
elif numero < 10:
    print("El número es menor que 10")  
else: 
    print("El numero es igual a 10")