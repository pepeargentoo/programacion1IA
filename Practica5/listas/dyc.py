"""
dado un arrglo de 1 y 0 determinar la cantidad de ceros
"""
def cuatoszeros(array,ini,fin,cant):
    if ini == fin:
        if array[ini] == 0:
            return 1
        else:
            return 0

    mid = int((ini+fin)/2)
    inf = cuatoszeros(array,ini,mid,cant)
    sup = cuatoszeros(array,mid+1,fin,cant)
    return sup+inf



def progresionDyC(array,ini,fin):
    if ini==fin:
        print('fin')
    medio = int((ini+fin)/2)
    inf = progresionDyC(array,ini,medio)
    sup = progresionDyC(array,medio,fin)
    

numeros = [0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0]
cantzeros = 0
for i in numeros:
    if i == 0:
        cantzeros+=1
print(cantzeros)
cant =0
print(cuatoszeros(numeros,0,len(numeros)-1,cant))


numeros = [2,4,8,10,12,14,16]
numeros = [1,6,11,16,21,31]
factor = numeros[1]-numeros[0]
for i in range(len(numeros)-1):
    if (numeros[i+1]- numeros[i]) != factor:
        print(numeros[i]+factor)
        break