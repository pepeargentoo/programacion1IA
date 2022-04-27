"""
1. Dada una contrase˜na verificar que su longitud es superior a 8 caracteres.
"""
password = input("ingrese contraseña\n")
if len(password) > 8:
    print("La contraseña tine mas de 8 carcateres")
else:
    print("La contraseña no tiene mas de 8 carcateres")
