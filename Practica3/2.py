"""
2. Escribir un programa que verifique si un n´umero es divisible por 4
"""
try:
    numero = int(input('ingrese numero\n'))

    if (numero % 4==0):
        print('Es divisible por 4')
    else:
        print('No es idivisible por 4')
except:
  print('no ingresaste un numero')