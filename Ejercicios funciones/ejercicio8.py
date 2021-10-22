"""Construir una función que tire los dados. La función recibe un entero que corresponde a la cantidad
de dados a tirar. Todos los dados son de 6 caras. La función devuelve la suma de los valores de los
dados. Investigar cómo obtener números al azar."""

def TirarDados(CantidadTiradaDados):
    import random
    sumaAcumulada=0
    for i in range(CantidadTiradaDados):
        tirada = random.randint(1,6)
        sumaAcumulada+=tirada
        print("El resultado de la tirada",i+1,"fue de",tirada)
    print("La suma acumulada es de",sumaAcumulada)

CantidadVecesTiradaDados = int(input("Ingrese la cantidad dados que desea tirar:"))
TirarDados(CantidadVecesTiradaDados)