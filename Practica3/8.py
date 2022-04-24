"""
8. Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:
Item Rosario Funes Rold´an
Zapatillas 30 % 40 % 25 %
Remeras 20 % 30 % 15 %
Pantalones 10 % 5 % 20 %
Dado un item y la sede del local, devolver el descuento que se recibir´a.
"""
item = input('ingrese item')
if (item == 'Zapatillas' or item == 'Remeras' or item == 'Pantalones'):
    sucursal = input('ingrese sucursal')
    if(sucursal == 'Rosario' or sucursal == 'Funes' or sucursal == 'Roldan'):
        if(item == 'Zapatillas' and sucursal == 'Rosario'):
            print("30%")
        if (item == 'Zapatillas' and sucursal == 'Funes'):
            print("40%")
        if (item == 'Zapatillas' and sucursal == 'Roldan'):
            print("25%")

        if (item == 'Remeras' and sucursal == 'Rosario'):
            print("20%")
        if (item == 'Remeras' and sucursal == 'Funes'):
            print("30%")
        if (item == 'Remeras' and sucursal == 'Roldan'):
            print("15%")

        if (item == 'Pantalones' and sucursal == 'Rosario'):
            print("10%")
        if (item == 'Pantalones' and sucursal == 'Funes'):
            print("5%")
        if (item == 'Pantalones' and sucursal == 'Roldan'):
            print("20%")
    else:
        print('No existe sucursal')
else:
    print('El item no exite')