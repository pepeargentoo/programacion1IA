"""
12. Escriba un programa que solicite un numero entero al usuario
y compute la suma de todos los numeros
naturales menores a él. Este programa debe ser interactivo.
Es decir, el programa solicita un numero al
usuario, devuelve la suma, y solicita un nuevo número. Esto continúa
así hasta que el usuario ingresa
"salir", determinando que el programa debe terminar. Utilice un bucle
while para resolver este
problema. Tenga en cuenta la sentencia break para determinar la
interrupción del bucle. Ejemplos:
Ingrese un numero o 'salir ' para terminar : 10
La suma es 45
Ingrese un numero o 'salir ' para terminar : 50
La suma es 1225
Ingrese un numero o 'salir ' para terminar : salir
"""
while True:
    ingreso = input("Ingrese un numero o 'salir' para terminar :")
    if ingreso == "salir":
        break
    else:
        suma = 0
        try:
            for i in range(int(ingreso)):
                suma += i
            print(suma)
        except ValueError:
            print("no ingreso un numero")
