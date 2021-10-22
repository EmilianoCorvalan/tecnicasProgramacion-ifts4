contador=0
marcador=0
numero = None

while True:
    if numero==0:
        break
    numero = int(input("Ingrese un numero:"))
    contador = contador + numero
    marcador = marcador+1
    print("La suma total es:",contador)
print("El promedio es de:",(contador/(marcador-1)))