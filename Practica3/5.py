"""
5. Convertir las calificaciones alfab´eticas
‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en calificaciones num´ericas
5, 6, 7, 8, 9 y 10
respectivamente. Ingresar una calificaci´on alfab´etica e informar por pantalla la calificaci´on num´erica
correspondiente, en caso de ingresar cualquier otra letra mostrar ((error calificaci´on inexistente)).
"""
calificacion = input('ingrese letra:\n')
if(calificacion == 'I' or calificacion =='A' or calificacion == 'B'
   or calificacion =='M' or calificacion == 'D' or calificacion == 'E' ):
    if(calificacion =='I'):
        print(5)
    if (calificacion == 'A'):
        print(6)
    if (calificacion == 'B'):
        print(7)
    if (calificacion == 'M'):
        print(8)
    if (calificacion == 'D'):
        print(9)
    if (calificacion == 'E'):
        print(10)
else:
    print('error calificacion inexistente')