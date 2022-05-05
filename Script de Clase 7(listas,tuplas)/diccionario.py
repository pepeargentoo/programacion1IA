"""
7. Escribir un programa que recibe un diccionario que
tiene como llave a alumnos y los valores asociados una
lista con las notas de parciales de los alumnos.
 El programa debe calcular el promedio de cada alumno e
 imprimirlo en pantalla.
 Por ejemplo para alumnos = { " Juan " : [6 ,9 ,8] ,
 " Manuel " : [9 ,10 ,9] , " Martin " : [5 ,6 ,7]}
 Debería mostrar:
El promedio de Juan es 7.666666
El promedio de Manuel es 9.333333
El promedio de Martin es 6
"""
alumnos = {"Juan": [6, 9, 8], "Manuel": [9, 10, 9], "Martin": [5, 6, 7]}
for i in alumnos:
    print("El promedio de %s es %f" % (i, sum(alumnos[i]) / len(alumnos[i])))
