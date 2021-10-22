"""En un juego se mide el tiempo que tardó en completarlo en segundos (entero), para el trabajo, se
ingresa por teclado. Se pide que se muestre el tiempo en el formato HH:MM:SS, utilizando 2 cifras
para la hora (HH), 2 cifras para los minutos (MM) y 2 cifras para los segundos (SS).
NOTA: Está prohibido utilizar la librería estándar datetime.
segundos=int(input(“Ingrese el tiempo en segundos:”))
…continuar el programa.
Nota: En las especificaciones del problema falta indicar que debe hace el programa en ciertos casos.
Identificar los casos no especificados. Decidir como debe actuar el programa en esos casos. Informen
sus decisiones y ajusten el programa para implementar sus decisiones."""

# El programa convierte los segundos en horas y/o minutos segun corresponda. 
# Se utiliza la funcion format() para que siempre los valores sean de 2 cifras.
# Al ingresar un valor mayor a 360000 segundos, el programa entra en conflicto. Se soluciona agregando un cero más en la variable HH modificada con la funcion format().
# Se puede agregar tantos ceros en la funcion format() como sea necesario. Aunque en este caso el ejercicio pide 2 cifras.
segundos=int(input("Ingrese el tiempo en segundos:"))
minutoEnSegundos = 60
horaEnSegundos = 3600
HH = 00
MM = 00
SS = 00

if segundos >= 3600:
    HH = segundos // horaEnSegundos 
    residuoHH = segundos % horaEnSegundos
    if residuoHH >= 60:
        MM = residuoHH // minutoEnSegundos
        residuoMMEnSegundos = residuoHH % minutoEnSegundos
        print (format(HH,'02'),":",format(MM,'02'),":",format(residuoMMEnSegundos,'02'))
    else:
        print (format(HH,'002'),":",format(MM,'02'),":",format(residuoHH,'02'))

elif segundos < 3600 and segundos >=60:
    MM = segundos // minutoEnSegundos
    residuoMMEnSegundos = segundos % minutoEnSegundos
    print (format(HH,'02'),":",format(MM,'02'),":",format(residuoMMEnSegundos,'02'))
else: 
    print (format(HH,'02'),":",format(MM,'02'),":",format(segundos,'02'))