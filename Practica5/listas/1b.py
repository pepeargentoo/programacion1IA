def maxDyC(array, ini, fin):
    if ini == fin:
        return array[ini]

    mid = int((ini + fin) / 2)
    inf = maxDyC(array, ini, mid)
    sup = maxDyC(array, mid + 1, fin)
    if sup > inf:
        return sup
    else:
        return inf

def minDyC(array, ini, fin):
    if ini == fin:
        return array[ini]
    mid = int((ini + fin) / 2)
    inf = minDyC(array, ini, mid)
    sup = minDyC(array, mid + 1, fin)
    if inf < sup:
        return inf
    else:
        return sup


numeros = [11, 25, 3, -4, 95]

print('maximo con dyc', maxDyC(numeros, 0, len(numeros) - 1))

maximo = -100000000000
for i in numeros:
    if maximo < i:
        maximo = i

minimo = 999999999999999999999999999
for i in numeros:
    if i < minimo:
        minimo = i

print('maximo :', maximo)
print('minimoDyc:', minDyC(numeros, 0, len(numeros) - 1))
print('minimo:', minimo)
