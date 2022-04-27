"""
7. En el centro de la ciudad de Rosario el estacionamiento en vıa se encuentra tarifado y esta dividido
en tres zonas con tarifas diferenciadas. El vehıculo puede estacionarse como maximo por 3 horas en
el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el vehıculo.
La siguinte tabla muestra los costos por hora en cada una de las zonas:
Zona Primer hora Segunda hora Tercer Hora
A $57,00 $71,20 $85,50
B $47,00 $58,70 $70,50
C $37,00 $46,20 $55,50
Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el veh´ıculo estar´a
estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento supere las 3 horas,
imprimir un mensaje de error acorde.
"""
zona = input("ingrese zona A,B,C")
zona = zona.upper()
if zona == "A" or zona == "B" or zona == "C":
    try:
        horas = int(input("ingrese cantidad de hora a estacionar"))
        if 3 >= horas >= 1:
            if zona == "A" and horas == 1:
                print("$57,00")
            if zona == "A" and horas == 2:
                print("$71,20")
            if zona == "A" and horas == 3:
                print("$85,50")

            if zona == "B" and horas == 1:
                print("$47,00")
            if zona == "B" and horas == 2:
                print("$58,70")
            if zona == "B" and horas == 3:
                print("$70,50")

            if zona == "C" and horas == 1:
                print("$37,00")
            if zona == "C" and horas == 2:
                print("$46,20")
            if zona == "C" and horas == 3:
                print("$55,50")
        else:
            print("El tiempo de estacionamiento supere las 3 horas")
    except ValueError:
        print("Debe ingresar solo numeros")
else:
    print("La zona no existe")
