def numeroPrimoFor(numero):
    if numero > 1:
        contador=0
        for i in range (2,numero):
            resto = numero % i
            if resto == 0:
                contador+=1
        if contador==0:
            return True
        else:
            return False

#Este programa hecho con FOR, no es optimo si se ingresan numeros grandes.
numero = int(input("Ingrese un numero entero:"))
verificacionNroPrimo = numeroPrimoFor(numero)
if verificacionNroPrimo == True:
    print("El numero es primo.")
elif verificacionNroPrimo == False:
    print("El numero no es primo.")
else:
    print("El numero ingresado no es valido.")