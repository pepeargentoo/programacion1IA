viajes = []
totviajes = 0
tottiempo = 0
tiempoviaje= 0
diasconmenos = 'A'
for i in range(2):
    cviajes = 0
    tiempoviaje = 0
    while True:
        nrobici = int(input('ingrese  nro bicicleta '))
        if nrobici == 0:
            viajes.append({'cantviajes': cviajes, 'duracion': tiempoviaje})
            totviajes += cviajes
            tottiempo += tiempoviaje
            if diasconmenos == 'A':
                diasconmenos = totviajes
            if diasconmenos > totviajes:
                diasconmenos = totviajes
            break
        duracion = int(input('ingrese duracion'))
        cviajes += 1
        tiempoviaje += duracion

if totviajes != 0:
    print("“tiempo promedio” de viaje Mensual de las bicicletas", tiempoviaje / totviajes)

for i in viajes:
    if i['cantviajes'] == 0:
        continue
    if (i['duracion'] / i['cantviajes']) > (tiempoviaje / totviajes):
        print('Este dia Supero al promedio')
    print("cantidad de viajes : ", i['cantviajes'])
    print("tiempo promedio", i['duracion'] / i['cantviajes'])
    print('el dia con menos uso de bicis', diasconmenos)