import datetime

"""
A partir de la lista del ejercicio anterior, genere un programa que calcule
los años que lleva cursando la carrera en curso y los agregue como un dato
más a la lista.
Finalmente, imprima el nombre, el apellido y cantidad de años cursados de
la persona a partir del uso de índice o indexación para cada elemento y de
manera concatenada, en una cadena que puede incluir otras palabras para dar
formato a la frase.
"""
datosPersonales = []
while True:
    try:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        localidad = input("Localidad: ")
        edad = int(input("Edad: "))
        dni = int(input("Dni: "))
        carrera = input("Carrera: ")
        if carrera != "Tecnicatura":
            print("Ingrese Tecnicatura en carrera")
            continue
        ingreso = int(input("Año de Ingreso: "))
        datosPersonales.append(
            {
                "nombre": nombre,
                "apellido": apellido,
                "localidad": localidad,
                "edad": edad,
                "dni": dni,
                "carrera": carrera,
                "ingreso": ingreso,
            }
        )
        while True:
            opcion = int(
                input(
                    "Ingrese: \n"
                    "1) ingresar otro dato \n"
                    "2) salir\n"))
            if opcion == 1 or opcion == 2:
                break

        if opcion == 2:
            break

    except ValueError:
        print("la edad, el Dni y el Año de ingreso tienen que ser un numero")

fecha = datetime.datetime.now()
for i in datosPersonales:
    i['cursando'] = i['ingreso'] - fecha.year
    print('Nombre: %s \nApellido: %s \nAños de Cursado: %s' %
          (i['nombre'], i['apellido'], i['cursando']))
