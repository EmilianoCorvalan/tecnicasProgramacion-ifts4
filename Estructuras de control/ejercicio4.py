"""En una fábrica, una balanza automática pesa tandas de galletitas. Para el ejercicio, los valores se
ingresan por teclado. Las galletitas se acumulan, cuando el peso acumulado es igual o superior al peso
que debe tener el paquete, se informa por pantalla para cambiar el paquete. El peso del paquete debe
ser un parámetro en el programa y puede cambiarse en cada ejecución"""

pesoPaqueteKg = float(input("Ingrese el peso en kilos que debe tener el paquete:"))
tandasAcumuladas = 0
while True:
    tanda = float(input("Ingrese el peso en kilos de esta tanda de galletitas:"))
    tandasAcumuladas =  tandasAcumuladas + tanda
    if tandasAcumuladas >= pesoPaqueteKg:
        print("Paquete lleno. Por favor, cambiar el paquete.")
        break