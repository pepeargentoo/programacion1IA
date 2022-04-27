"""Escriba un programa que dada una lista de números y un valor de umbral vaya sumando los números de la lista hasta
que la suma alcance el umbral. Utilice un bucle while y el metodo .pop(0) para seleccionar al primer elemento de la
lista. Utilice break para terminar la ejecución del bucle cuando la suma alcance el umbral. """
try:
    umbral = int(input("ingrese umbral"))
    valores = [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]
    suma = 0
    print(valores)
    while len(valores) > 0:
        if suma < umbral:
            suma += valores.pop(0)
        else:
            break
    print("suma = %d" % suma)
except ValueError:
    print("no ingresaste numero ")
