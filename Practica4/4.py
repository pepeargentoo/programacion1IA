"""
4. Dada la siguiente secuencia de números:
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
imprimir los números divisibles por 5 menores a 150.
"""
numeros = [12, 75, 150, 180, 145, 525, 50]
for i in numeros:
    if i % 5 == 0 and i < 150:
        print(i)
