"""
La lista en el siguiente bloque de código contiene números enteros.
Crear una lista para los números pares y otra para los números impares.
"""
numeros = [3 , 5 , 2 , 9 , 2 , 6 , 6 , 4 , 3 , 9 , 6 , 7 , 8 , 5 , 11]
pares = []
impares = []
for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print('lista de pares: ',pares)
print('lista de impares: ',impares)
