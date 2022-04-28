"""
8. Resuelva los siguientes ejercicios
a. Calcular el cuadrado de los primeros 10 números enteros.
b. Calcular la suma de los números enteros entre 0 y 100 inclusive.
c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a
100?
d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores
a 100?
"""
print("A)")
for i in range(10):
    print((i + 1) ** 2)

print("B)")
suma = 0
for i in range(101):
    suma += i
print(suma)
print("C)")
sump = 0
countp = 0
for i in range(100):
    if i % 2 == 0:
        sump += i
        countp += 1
print("SUma de Pares:%d" % sump)
print("cant de Pares:%d" % countp)
print("D)")

sumi = 0
counti = 0
for i in range(100):
    if i % 2 != 0:
        sumi += i
        counti += 1

print("SUma de ImPares:%d" % sumi)
print("cant de ImPares:%d" % counti)
