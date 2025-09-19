from utilidades import limpiar_pantalla
def mostrar_reporte_inventario():
    """
    Podes ver el reporte de inventario.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE INVENTARIO")

        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
def mostrar_reporte_venta():
    """
    Ver el reporte de ventas.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE VENTA")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_reporte_empleados():
    """
    Ver el reporte de los empleados.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE EMPLEADOS")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
