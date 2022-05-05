"""
Cartas como tuplas.
a. Proponer una representación con tuplas para
las cartas de la baraja francesa.
b. Escribir un programa de poker que reciba cinco
cartas de la baraja francesa
e informe (devuelva el valor lógico correspondiente)
si esas cartas forman o
no un poker (es decir que hay 4 cartas con el mismo número).
"""
import random
cartas = ('Trebol', 'Diamante', 'Corazones', 'Picas')
mazo = []
for i in range(50):
    if i < 12:
        if i == 10 or i == 11 or i == 12:
            if i == 10:
                mazo.append(('Jota', 'Trebol'))
            if i == 11:
                mazo.append(('Reyna', 'Trebol'))
            if i == 12:
                mazo.append(('Rey', 'Trebol'))
        else:
            if (i + 1) == 10:
                continue
            if (i + 1) == 1:
                mazo.append(('AS', 'Trebol'))
            else:
                mazo.append((i + 1, 'Trebol'))

    if i >= 12 and i < 25:
        if i - 12 == 10 or i - 12 == 11 or i - 12 == 12:
            if i - 12 == 10:
                mazo.append(('Jota', 'Dimante'))
            if i - 12 == 11:
                mazo.append(('Reyna', 'Dimante'))
            if i - 12 == 12:
                mazo.append(('Rey', 'Dimante'))
        else:
            if (i - 12) == 10:
                continue
            if i == 12:
                mazo.append(('AS', 'Dimante'))
            else:
                mazo.append((i - 12, 'Dimante'))

    if i >= 25 and i < 38:
        if i - 25 == 10 or i - 25 == 11 or i - 25 == 12:
            if i - 25 == 10:
                mazo.append(('Jota', 'Corazones'))
            if i - 25 == 11:
                mazo.append(('Reyna', 'Corazones'))
            if i - 25 == 12:
                mazo.append(('Rey', 'Corazones'))
        else:
            if (i - 25) == 10:
                continue
            if i == 25:
                mazo.append(('AS', 'Corazones'))
            else:
                mazo.append((i - 25, 'Corazones'))

    if i >= 38 and i < 50:

        if i - 37 == 10 or i - 37 == 11 or i - 37 == 12:
            if i - 37 == 10:
                mazo.append(('Jota', 'Picas'))
            if i - 37 == 11:
                mazo.append(('Reyna', 'Picas'))
            if i - 37 == 12:
                mazo.append(('Rey', 'Picas'))
        else:
            if (i - 37) == 10:
                continue
            if i == 38:
                mazo.append(('AS', 'Picas'))
            else:
                mazo.append((i - 37, 'Picas'))


carta1 = random.choice(mazo)
carta2 = random.choice(mazo)
carta3 = random.choice(mazo)
carta4 = random.choice(mazo)
carta5 = random.choice(mazo)

iguales = 0
mano = []
mano_original = []
for i in range(5):
    carta = random.choice(mazo)
    mano_original.append(carta)
    if carta[0] in mano:
        iguales += 1
    else:
        mano.append(carta[0])
if iguales == 4:
    print('POKER')
else:
    print('No Es PoKER:')
    print('Cartas iguales: ', iguales)
    print('Mano: ', mano_original)
