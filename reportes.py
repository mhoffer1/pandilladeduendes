from utilidades import *
def mostrar_reporte_inventario(sucursal):
    """
    Podes ver el reporte de inventario.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE INVENTARIO")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
def mostrar_reporte_venta(sucursal):
    """
    Ver el reporte de ventas.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE VENTA")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_reporte_empleados(sucursal):
    """
    Ver el reporte de los empleados.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTE DE EMPLEADOS")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
