"""
9. Ahora, supongamos que ademas dependiendo del dıa de la semana se puede recibir un descuento
adicional acumulable.
Es decir, si se recibi´o un descuento del 10 % seg´un el ´ıtem y la sede y la compra
se realiza un lunes, el descuento total ser´a un 20 % . Escribir un programa en el que la persona pueda
ingresar el d´ıa de la semana, el item a comprar y la sede del local. Luego, informar el descuento total
a recibir. Utilizar la siguiente tabla de descuentos
Lunes Mi´ercoles Jueves
Descuento 10 % 8 % 5 %
"""
item = input("ingrese item")
if item == "Zapatillas" or item == "Remeras" or item == "Pantalones":
    sucursal = input("ingrese sucursal")
    if sucursal == "Rosario" or sucursal == "Funes" or sucursal == "Roldan":
        dia = input("Ingrese Dia de la Semana")
        descdia = 0
        if dia == "Lunes":
            descdia = 10
        if dia == "Miercoles":
            descdia = 8
        if dia == "Jueves":
            descdia = 5
        if item == "Zapatillas" and sucursal == "Rosario":
            desc = 30
            print(desc + descdia, end="%")
        if item == "Zapatillas" and sucursal == "Funes":
            desc = 40
            print(desc + descdia, end="%")

        if item == "Zapatillas" and sucursal == "Roldan":
            desc = 25
            print(desc + descdia, end="%")

        if item == "Remeras" and sucursal == "Rosario":
            desc = 20
            print(desc + descdia, end="%")
        if item == "Remeras" and sucursal == "Funes":
            desc = 30
            print(desc + descdia, end="%")
        if item == "Remeras" and sucursal == "Roldan":
            desc = 15
            print(desc + descdia, end="%")

        if item == "Pantalones" and sucursal == "Rosario":
            desc = 10
            print(desc + descdia, end="%")
        if item == "Pantalones" and sucursal == "Funes":
            desc = 5
            print(desc + descdia, end="%")
        if item == "Pantalones" and sucursal == "Roldan":
            desc = 20
            print(desc + descdia, end="%")

    else:
        print("No existe sucursal")
else:
    print("El item no exite")
