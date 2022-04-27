"""
Repetir el ejercicio anterior pero garantizando que las listas resultantes no tengan resultados repetidos.
"""
numeros = [3, 5, 2, 9, 2, 6, 6, 4, 3, 9, 6, 7, 8, 5, 11]
pares = []
impares = []
for i in numeros:
    if i % 2 == 0:
        if i not in pares:
            pares.append(i)
    else:
        if i not in impares:
            impares.append(i)

print("lista de pares: ", pares)
print("lista de impares: ", impares)
