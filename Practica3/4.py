"""
4. Dados 3 lados de un tri´angulo, informar si el mismo es
equil´atero, is´osceles o escaleno.
"""

try:
    lado1 = int(input("ingrese lado"))
    lado2 = int(input("ingrese lado"))
    lado3 = int(input("ingrese lado"))

    if (lado1 == lado2) and (lado1 == lado3) and (lado2 == lado3):
        print("Es equilatero")
    else:
        if (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
            print("escaleno")
        else:
            print("isosceles")
except ValueError:
    print("no ingresaste un numero")
