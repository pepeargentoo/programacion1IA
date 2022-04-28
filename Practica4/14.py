"""
14. Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero
hay, que sean menores que el segundo.
a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor
que el segundo.
c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
la implemntacion con el for, es mucho mas clara
"""
try:
    num1 = int(input("ingrese numero 1"))
    num2 = int(input("ingrese numero 2"))
    numltip = 0
    for i in range(1, num2):
        if num1 % i == 0:
            numltip += 1
    print(numltip)
except ValueError:
    print("no ingresaste un numero jeje")

try:
    num1 = int(input("ingrese numero 1"))
    num2 = int(input("ingrese numero 2"))
    numltip = 0
    auximult = 1
    while True:
        if auximult * num1 > num2:
            break
        if num1 % auximult == 0:
            numltip += 1
        auximult += 1
    print(numltip)
except ValueError:
    print("no ingresaste un numero jeje")
