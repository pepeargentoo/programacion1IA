"""
13. Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera.
 A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que
la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar
a resolver el problema:
billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # altura en metros
billetes_n = 1
dia = 1
Utilice un bucle while para resolver el problema
"""
billete_grosor = 0.11 * 0.001
altura_monumento = 70
cantbilletes = 1
dias = 0
while True:
    cantbilletes=cantbilletes*2
    dias +=1
    if (cantbilletes*billete_grosor)>= altura_monumento:
        break
print(dias)