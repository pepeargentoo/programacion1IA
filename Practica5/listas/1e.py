"""
e. Dada una lista de números, calcule, por un lado,
la suma de los elementos que se encuentran en
un índice par en la lista y, por otro lado, el producto
de los elementos de posiciones con índice
impar.
"""
def sumDyC(array,ini,fin):
    if ini == fin:
        if array[ini] %2 ==0:
            return array[ini]
        else:
            return 0
    mid = int((ini+fin)/2)
    inf = sumDyC(array,ini,mid)
    sup = sumDyC(array,mid+1,fin)
    return inf+sup




numeros = [0 ,1 ,2 ,3 ,4 ,5]
sumapares=0
prodimpares = 1

for i in numeros:
    if i%2==0:
        sumapares +=i
    else:
        prodimpares *=i
print("La suma de í ndices pares es ",sumapares)
print("El producto de í ndices impares es ",prodimpares)
print(sumDyC(numeros, 0, len(numeros)-1))