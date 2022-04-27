"""
3. Determinar e informar el mayor valor de 3 n´umeros enteros. ¿Qu´e cambiarıas en el algoritmo si se
trataran de 3 n´umeros reales o de 3 caracteres o de 3 palabras?. ¿Y si se buscara el menor valor?
"""
try:
    num1 = int(input("numero1:\n"))
    num2 = int(input("numero1:\n"))
    num3 = int(input("numero1:\n"))

    if (num1 > num2) and (num1 > num3):
        print("El numero %d es el mayor" % num1)
    else:
        if (num2 > num1) and (num2 > num3):
            print("El numero %d es el mayor" % num2)
        else:
            print("El numero %d es el mayor" % num3)
except ValueError:
    print("no ingresaste un numero")
"""
la solucion es cambiar el cast en ves de int() es float() o n caso de string no se necesita cast
si es menor solo se necesita cambiar el simbolo > por <

"""
