"""
Dada una lista de tuplas donde el elemento en la
posición 0 es el DNI de
la persona y en la posición 1 es el ingreso,
identificar todas las personas cuyo ingreso es:

a. Menor que el salario mínimo, vital y móvil (SMVM)
b. Entre un SMVM y dos SMVM
c. Entre dos SMVM y 4 SMVM
d. Mayor a 4 SMVM
Crear una lista de tuplas donde el primer elemento indica
el rango de ingresos y el
segundo elemento la cantidad de personas en ese segmento
"""
import random
tuplas = []
smvm = 45000  # hoy

for i in range(20):
    tuplas.append((random.randint(100000, 400000),
                   random.randint(30000, 945000)))

mienorsmvm = 0
dossmvm = 0
cuatrosmvm = 0
mascuatrosmvm = 0

for i in tuplas:
    if i[1] < 45000:
        mienorsmvm += 1
    if i[1] >= 45000 and i[1] < 90000:
        dossmvm += 1
    if i[1] >= 90000 and i[1] < 180000:
        cuatrosmvm += 1
    if i[1] > 180000:
        mascuatrosmvm += 1

tuplassmvm = [('<45000', mienorsmvm),
              ('45000-90000', dossmvm),
              ('90000-180000', cuatrosmvm),
              ('>180000', mascuatrosmvm),
              ]
for i in tuplassmvm:
    print('Rango: %s\nCantidad: %s' % (i[0], i[1]))
