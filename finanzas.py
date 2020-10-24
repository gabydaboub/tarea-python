from ingresos import ingresos
from egresos import egresos



ingresos = ingresos()
egresos = egresos()

while True:

    print("Menú:")
    print("0. Salir")
    print("1. Registrar ingreso.")
    print("2. Registrar egreso.")
    print("3. Reporte de ingresos.")
    print("4. Reporte de egresos.")
    print("5. Reporte de transacciones.")
    print("6. Total de la cuenta.")
    numero = input("Ingrese un número: ")

    

    if numero == 0:
        break 

    elif numero == 1:
        ingreso = float(input("Ingrese el monto del ingreso: "))
        ingresos.agegarIngreso(ingreso)
        print("Su transferencia se realizo con exito")
    
    elif numero == 2:

        egreso = float(input("Ingrese el monto del egreso: "))
        engresos.agegarEgreso(egreso)

        print("Su transferencia se realizo con exito")

    elif numero == 3:
        montoIngresos = ingresos.getMontoTotal()
        print(f"Total dinero ingresado {montoIngresos}")

    elif numero == 4:
        montoEgresos = egresos.getMontoTotal()
        print(f"Total dinero egresado {montoEgresos}")

    elif numero == 5:
        montoTotal = ingresos.getMontoTotal() - egresos.getMontoTotal()
        print(f"Total dinero en la cuenta {montoIngresos}")

    elif numero == 6:
        tIngresos = ingreos.getTransacciones()
        tEgresos = egresos.getTransacciones()
        tTotales = tIngresos + tEgresos
        print(f"La cantidad de transacciones de ingresos son {tIngreos}")
        print(f"La cantidad de transacciones de ingresos son {tEgresos}")
        print(f"Su número total de transacciones es {tTotales}")


    