"""
Dada la siguiente lista de palabras

palabras = [ " C ó ncavo " , " Autopista " , " Diagonal " , " Equipaje " , " Ardilla " , " Consultorio " , " Roma " , " Loco " , " Marciano " , " Karateca " , " Aniversario " , " Topadora " , " Grabador " , " Salir " , " Ventoso " , " Anunciar " ," R ó tula " , " Estanque " , " Quedarse " , " Nuevo " , " Sordo " , " Madurar " , " Vestir " , " Retoque " , " Desvelo " , " Hora " , " Cochera " , " Metal " , " Nudo " , " Maquillaje " , " Barco " , " Soda " , " Lagartija " ]

¿Cuántas palabras hay en total?
¿Cuántas empiezan con ’A’ ?
¿Cuántas terminan con ’o’ ?
¿Cuántas empiezan con alguna vocal?
¿Cuántas terminan con alguna consonante?
Seleccionar la última palabra que empiece con una consonante.
"""
print('ultimo pepe')
palabras = [ "Cóncavo" , "Autopista" , "Diagonal" , "Equipaje" , "Ardilla" , "Consultorio" , "Roma" , "Loco" ,
             "Marciano" , "Karateca" , "Aniversario" , "Topadora" , "Grabador" , "Salir" , "Ventoso" ,
             "Anunciar" ,"Rótula" , "Estanque" , "Quedarse" , "Nuevo" , "Sordo" , "Madurar" , "Vestir" ,
             "Retoque" , "Desvelo" , "Hora" , "Cochera" , "Metal" , "Nudo" , "Maquillaje" ,
             "Barco" , "Soda" , "Lagartija" ]
empiezaA = 0
empiezaO = 0
empiezaV = 0
finConsonantes = 0

for i in palabras:
    if i[0] == 'A':
        empiezaA+=1

    if i[0] == 'o':
        empiezaO+=1

    if i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U' :
        empiezaV+=1

    if i[len(i)-1] != 'A' or i[len(i)-1] != 'E' or i[len(i)-1] != 'I' or i[len(i)-1] != 'O' or i[len(i)-1] != 'U':
        finConsonantes +=1


print('¿Cuántas palabras hay en total?%d'%len(palabras))
print('¿Cuántas empiezan con ’A’ ?%d'%empiezaA)
print('¿Cuántas terminan con ’o’ ?%d'%empiezaO)
print('¿Cuántas empiezan con alguna vocal?%d'%empiezaV)
print('¿Cuántas terminan con alguna consonante?%d'%finConsonantes)

#reverso lista
for i in range(len(palabras)-1,0,-1):
    if palabras[i][0] != 'A' or palabras[i][0] != 'E' or palabras[i][0] != 'I' or \
            palabras[i][0] != 'O' or palabras[i][0] != 'U':
        print('Seleccionar la última palabra que empiece con una consonante %s'%palabras[i])
        break