"""
EJERCICIO 1
Luego de recabar datos de los socios en cada uno de los 17
clubes más importantes de la ciudad
se quiere determinar, para cada una de ellos,
entre los censados mayores de edad (tienen 18 años o más)
quienes son más numerosos, los que son temporales (código 1) o
los que son permanentes (código 2).
Para resolver esto se dispone, por cada socio de cada uno de los
clubes, su código de asociado
(1 para temporal, 2 para permanente) y edad.
Un código de asociado 0 (cero) indica que no hay más datos de ese club
"""


def cargar_datos(club):
    for j in range(2):  # tome 2 clubes me daba paja llenar 17 jajaja
        while True:
            try:
                codigo = int(
                    input(
                        "Ingrese codigo:\n"
                        "1)temporales\n"
                        "2)permanentes\n"
                        "0)salir\n"
                    )
                )
                if codigo == 0:
                    break
                if codigo == 1 or codigo == 2:
                    edad = int(input("ingrese la edad del socio"))
                    if edad < 18:
                        print("Solo personas de 18 o mas")
                    else:
                        club.append(
                            {"club": j + 1, "codigo": codigo, "edad": edad})
            except ValueError:
                print("Valor no admitido")
    return club


def get_info(aclubs, nclub):
    temporales = 0
    permanentes = 0
    for k in aclubs:
        if k["club"] == nclub:
            if k["codigo"] == 1:
                temporales += 1
            else:
                permanentes += 1
    print("club %d resultados:" % nclub)
    print("temporales", temporales)
    print("permanentes", permanentes)


clubs = []
clubs = cargar_datos(clubs)

for i in range(2):  # tomo 2 en vez de 17 porque me da paja cargar 17 clubs
    get_info(clubs, i + 1)
