"""
5. Imprimir los primeros 10 valores de la secuencia de
Fibonacci. La secuencia de Fibonacci es una serie
de números en la cual los dos primeros números son 0 y 1,
 y el siguiente número se corresponde a la
suma de los dos números anteriores. Resultado esperado:
0 1 1 2 3 5 8 13 21 34
"""
c1 = 0
c2 = 1
print(c1, end=" ")
print(c2, end=" ")
for i in range(8):
    aux = c1 + c2
    print(aux, end=" ")
    c1 = c2
    c2 = aux
