def menorDeTres(A,B,C):
    if A<B and A<C :
        print(A,"es el numero menor de los 3.")
    elif B<A and B<C: 
        print(B,"es el numero menor de los 3.")
    elif C<A and C<B:
        print(C,"es el numero menor de los 3.")
    else:
        print("Los numeros son iguales")

primerNro = int(input("Ingrese un numero:"))
segundoNro = int(input("Ingrese un segundo numero:"))
tercerNro = int(input("Ingrese el tercer numero:"))
menorDeTres(primerNro,segundoNro,tercerNro)
#Funciona pero al poner dos numeros iguales en el primer y tercer numero, se rompe el programa.