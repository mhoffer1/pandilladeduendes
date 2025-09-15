from utilidades import *
def mostrar_reporte_inventario():
    
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("REPORTE DE INVENTARIO")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
def mostrar_reporte_venta():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("REPORTE DE VENTA")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_reporte_empleados():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("mostrar reporte de empleados.")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
