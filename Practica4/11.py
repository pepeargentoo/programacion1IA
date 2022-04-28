"""
11. Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice
un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
Resultados esperados:
valores = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
# suma -> 30
valores = [1 , 4 , 7 , 10]
# suma -> 14
"""
suma = 0
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in valores:
    if i % 2 == 0:
        suma += i
print(suma)
