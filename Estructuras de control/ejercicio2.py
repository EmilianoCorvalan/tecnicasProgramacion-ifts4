"""Para un programa se necesita imprimir por pantalla un listado de las fichas de dominó. Se puede
utilizar el “0” (cero) para representar las fichas sin puntos. Tener en cuenta que, por ejemplo, “4-5” y
“5-4” son la misma ficha y no puede estar duplicada en el listado."""

for i in range(0,7):
    for x in range(0,i+1):
        print(i,x)