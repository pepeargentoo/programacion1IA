"""
Escriba un programa que dada una lista numérica compute la suma de los números pares.
Utilice un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
"""
# maximo la longitud de las listas que ingresa
# si queres tener listas mas grande cambia el 4 por el numero que quieras jejej
maximo = 4
try:
    valores = []
    num = 0
    while True:
        if num < maximo:
            valores.append(int(input("ingrese numero")))
            num += 1
        else:
            break
    pares = 0

    for i in valores:
        if i % 2 == 0:
            pares += i
    print("la suma de pares %d" % pares)
except ValueError:
    print("ingreso algo raro")
