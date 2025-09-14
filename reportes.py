from utilidades import *
def mostrar_reporte_inventario():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("REPORTE DE INVENTARIO")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break

def mostrar_reporte_venta():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("REPORTE DE VENTA")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break

def mostrar_reporte_empleados():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("mostrar reporte de empleados.")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break
