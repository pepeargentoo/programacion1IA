"""
d. Dada una lista palabras de cadenas de texto,
devuelva una nueva lista formada sólo por las
cadenas de palabras que empiezan con "a".
"""
palabras = ["arbol ", "barco ", " artificial ", " casa ", " dado ", "a"]

nuevalista = list()

for i in palabras: #O(n)
    if i[0] == 'a':
        nuevalista.append(i)

print(nuevalista)