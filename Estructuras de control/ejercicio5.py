"""En una fábrica de panificados se tiene un silo para almacenar la harina. La capacidad del silo debe ser
un parámetro del programa y se puede cambiar en cada ejecución. Un operario le ingresa la cantidad
de harina requerida para la preparación (ingreso por teclado). El programa debe informar si la
cantidad de harina del silo suficiente para realizar la preparación. Si la cantidad es suficiente lo informa
y actualiza la cantidad harina restante en el silo. Si no es suficiente, lo informa y cancela la
preparación."""

capacidadSiloenKg = float(input("Ingrese la capacidad del silo en kilos:"))
while capacidadSiloenKg >= 0:
    harinaRequeridaenKg = float(input("Ingrese la cantidad de harina requerida en kilos:"))
    capacidadSiloEnKg = capacidadSiloenKg - harinaRequeridaenKg
    if capacidadSiloEnKg >= 0:
        print("La cantidad requerida está disponible. Quedan",capacidadSiloEnKg,"Kg en el silo")
    while capacidadSiloEnKg >=0:
        if capacidadSiloEnKg >= 0:
            harinaRequeridaenKg=float(input("Ingrese la cantidad de harina requerida en kilos:"))
            capacidadSiloEnKg = capacidadSiloEnKg - harinaRequeridaenKg
            if capacidadSiloEnKg >= 0:
                print("La cantidad requerida está disponible. Quedan",capacidadSiloEnKg,"Kg en el silo")
    else:
        print("Cantidad no disponible. Se cancela la operacion.")
        break