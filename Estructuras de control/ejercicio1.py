"""Para una aplicación se necesita validar la fecha ingresada por el usuario. El usuario ingresa un entero
para el día, un entero para el mes y un entero para el año (año completo, 4 dígitos). No hay que validar
si los datos ingresados son eneros o no, solo si la fecha es válida. Salida: imprimir “Fecha valida” o
“Fecha invalida”.
NOTA: Está prohibido utilizar la librería estándar datetime.
dia=int(input(“Ingrese el día:”))
mes=int(input(“Ingrese el mes:”))
anio=int(input(“Ingrese el año:”))
#utilizo la variable anio para evitar la ñ en la variable
…continuar el programa."""

dia=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:"))
anio=int(input("Ingrese el año:"))

#Verifico datos de entrada.
if dia<1 or dia>31:
    print("Fecha invalida")
    quit()
if mes<1 or mes>12:
    print("Fecha invalida")
    quit()
if anio<1000 or anio>2100:
    print("Fecha invalida")
    quit()

#Verifico dias de cada mes y años bisiestos.
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print("Fecha valida")

if mes==4 or mes==6 or mes==9 or mes==11:
    if dia >=1 and dia <=30:
        print("Fecha valida")
    else:
        print("Fecha invalida")

if mes==2:
    if (anio % 4) == 0:
        if dia>= 1 and dia <=29:
             print("Fecha valida.")
        else:
            print("Fecha invalida.")
    elif (anio % 4) != 0:
        if dia>= 1 and dia <=28:
            print("Fecha valida")
        else:
            print("Fecha invalida")