def promedioDeTresNros(A,B,C):
    sumaTotal = A+B+C
    promedio = sumaTotal / 3
    return promedio

primerNro=float(input("Ingrese un numero:"))
segundoNro=float(input("Ingrese un segundo numero:"))
tercerNro=float(input("Ingrese un tercer numero:"))
promedio = promedioDeTresNros(primerNro,segundoNro,tercerNro)
print("El promedio de los tres numeros es:",promedio)