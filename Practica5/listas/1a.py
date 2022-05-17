"""
a. Dada una lista de números list y un número n,
determine en qué índice de la lista list se encuentra
el número n.
En caso de no encontrarlo, el programa mostrará -1. Ejemplos
"""
lista = [11, 25, 3, -4, 95]
pos = -1
try:
    n = int(input("ingrese numero a buscar"))
    for i in range(len(lista)):
        if lista[i] == n:
            pos = i
            break
    print(pos)

except ValueError:
    print("debe ingresar un numero")
