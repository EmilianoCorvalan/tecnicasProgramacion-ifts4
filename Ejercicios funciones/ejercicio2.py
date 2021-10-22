def es_triangulo(A,B,C):
    """Funcion es_triangulo: Verifica si se puede formar un triangulo, dadas las medidas de 3 segmentos.
    Si la suma de 2 lados es menor que el tercero, no se puede hacer un triangulo"""
    if (A+B)>C:
        return True
    elif (A+C)>B:
        return True
    elif (B+C)>A:
        return True
    else:
        return False

#Programa principal
L1 = float(input("Ingrese la longitud del primer lado:"))
L2 = float(input("Ingrese la longitud del segundo lado:"))
L3 = float(input("Ingrese la longitud del tercer lado:"))
if es_triangulo(L1,L2,L3) == True :
    print("Se puede formar un triangulo")
else:
    print("No se puede formar un triangulo")