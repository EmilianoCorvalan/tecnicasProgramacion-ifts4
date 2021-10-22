def promedio(valor1,valor2):
    """Funcion promedio calcula el promedio de 2 numeros
    Entrada: valor1, valor2
    Salida: Promedio (float)
    """
    promedio = (valor1+valor2) /2.0
    return promedio #Este ejercicio no tenia el return definido.

#Programa principal 
n1 = float(input("Ingrese el valor 1:"))
n2 = float(input("Ingrese el valor 2:"))
prom = promedio(n1,n2)
print ("Promedio:", prom)