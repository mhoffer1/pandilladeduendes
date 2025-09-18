from utilidades import *
def mostrar_reporte_inventario(sucursal):
    
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
