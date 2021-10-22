suma=0
contador=0
while suma <= 20:
    numero=int(input("Ingrese un numero:"))
    suma = suma + numero
    contador = contador + 1
    print("La suma total es:",suma)

print("El promedio es:", (suma/contador))

