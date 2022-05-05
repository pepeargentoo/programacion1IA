"""
EJERCICIO 2 Una central telefónica registra la duración
de cada llamada, expresada en segundos. A partir de esta
información se quiere convertir la duración
de cada llamada a horas, minutos y segundos.
Luego, al finalizar el ingreso de datos y el proceso de
conversión, determinar:
La cantidad de llamadas que superaron los 10 minutos.
El promedio de duración de las llamadas (en segundos).
La mínima duración de llamada (en segundos).
No se sabe cuántas llamadas se han registrado, proponer un fin de datos.
"""


def carga_datos(llamadas):
    while True:
        duracion = input("Ingrese Duracion de llamada o 'S' para salir")
        if duracion == "S":
            break
        else:
            try:
                duracion = int(duracion)
                llamadas.append(duracion)
            except ValueError:
                continue


llamadas = []
llamadas10min = 0
totallamadas = 0
minllamadas = 1000000000000000000000
carga_datos(llamadas)

for i in llamadas:
    totallamadas += i
    if i > 600:
        llamadas10min += 1
    if i < minllamadas:
        minllamadas = i

print(
    "La cantidad de llamadas que superaron "
    "los 10 minutos %d" %
    llamadas10min)
print(
    "El promedio de duración de las llamadas (en segundos)",
    totallamadas / len(llamadas),
)
print("La mínima duración de llamada (en segundos). ", minllamadas)
