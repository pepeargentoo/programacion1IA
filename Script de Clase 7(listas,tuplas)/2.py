"""
Genere una lista llamada datosPersonales, mediante el uso de un
bucle donde en cada iteración se pida un solo dato de los
siguientes: Nombre, Apellido, Localidad, Edad, DNI,
Carrera en curso (en esta última ingrese: Tecnicatura),
año de inicio de la carrera.
Luego, imprima por pantalla la lista con los datos completados.
(Ingrese las palabras como cadenas y los números como enteros)
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
        datosPersonales.append(
            {
                "nombre": nombre,
                "apellido": apellido,
                "localidad": localidad,
                "edad": edad,
                "dni": dni,
                "carrera": carrera,
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
        print("la edad y el Dni tienen que ser un numero")

for i in datosPersonales:
    print("Nombre: %s" % i["nombre"])
    print("Apellido: %s" % i["apellido"])
    print("Localidad: %s" % i["localidad"])
    print("Edad: %d" % i["edad"])
    print("DNI: %d" % i["dni"])
    print("Carrera: %s" % i["carrera"])
