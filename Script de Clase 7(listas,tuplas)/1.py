"""
Escriba un programa que dada una lista de números calcule la suma acumulada
de sus elementos.
Es decir, una nueva lista donde el primer elemento es el mismo que en la
lista original,el segundo elemento es la suma del primer y segundo elemento
de la lista original,el tercer elemento es la suma del resultado anterior
con el tercer elemento de la lista original y así sucesivamente.
Por ejemplo, dada la lista [1, 2, 3], la suma acumulada debería ser [1, 3, 6].
"""
lista = [1, 2, 3]

for i in range(1, len(lista)):
    lista[i] = lista[i] + (lista[i - 1])

print(lista)
