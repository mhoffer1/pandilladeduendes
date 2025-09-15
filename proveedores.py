from utilidades import *

def menu_proveedores():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" Ventas")
        print("=" * 50)
        print("1.Registrar Proveedor")
        print("2.Solicitar productos a proveedor.")
        print("3.Ver pagos pendientes")
        print("4.Ver historial de Compra de Cada Proveedor.")
        print("5.Ver proveedor por Nombre.")
        print("0.Salir")
        opcion = input("Ingrese una opcion:")
    
        if opcion == "1":
            registrar_provedores()
        elif opcion == "2":
            solicitar_productos_a_proveedor()
        elif opcion == "3":
            pagos_pendientes()
        elif opcion == "4":
            historial_de_compras_a_cada_proveedor()
        elif opcion == "5":
            buscar_proveedor_por_nombre()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            

def registrar_provedores():

    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Registrar proveedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def solicitar_productos_a_proveedor():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Solicitar productos A Provedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def pagos_pendientes():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Pagos pendientes a proveedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def historial_de_compras_a_cada_proveedor():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Historial de compras de cada proveedor")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def buscar_proveedor_por_nombre():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Buscar proveedor por nombre.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        