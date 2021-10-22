contador=0
numero = None
while True:
    if numero == 0:
        break
    numero = int(input("Ingrese un numero:"))
    contador = contador + numero
    print("La suma total es:",contador)