"""
f. Dada una lista cualquiera, cree una nueva lista con los mismos elementos pero en el orden inverso
"""
numeros = [123 ,1 ,2 ,3 ,4 ,5]
numerosnueva = []
for i in range(len(numeros)-1,-1,-1):
    numerosnueva.append(numeros[i])

print(numerosnueva)