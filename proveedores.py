from utilidades import limpiar_pantalla

def menu_proveedores(sucursal):
    """"
    menu de proveedores, te permite hacer todas las acciones.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(f"    PROVEEDORES -- Sucursal: {sucursal['nombre']}")
        print("=" * 50)
        print("1.Registrar Proveedor")
        print("2.Solicitar productos a proveedor.")
        print("3.Ver pagos pendientes")
        print("4.Ver historial de Compra de Cada Proveedor.")
        print("5.Ver proveedor por Nombre.")
        print("0. Volver al Menu Principal")
        print("=" * 50)
        opcion = input("Ingrese una opcion: ")
    
        if opcion == "1":
            registrar_provedores(sucursal)
        elif opcion == "2":
            solicitar_productos_a_proveedor(sucursal)
        elif opcion == "3":
            pagos_pendientes(sucursal)
        elif opcion == "4":
            historial_de_compras_a_cada_proveedor(sucursal)
        elif opcion == "5":
            buscar_proveedor_por_nombre(sucursal)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            

def registrar_provedores(sucursal):
    """"
    Registra provedores con su nombre.
    """

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
def solicitar_productos_a_proveedor(sucursal):
    """
    Sirve para solicitar productos a un proveedor, debe ingresarse el provedor, producto/s
    y cantidad.
    """
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
def pagos_pendientes(sucursal):
    """
    Podes ver pagos pendientes a proveedores
    """
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

def historial_de_compras_a_cada_proveedor(sucursal):
    while True:
        """
        Podes ver el historial de compras a cada proveedor
        """
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

def buscar_proveedor_por_nombre(sucursal):
    """
    Podes buscar proveedores por nombre y apellido.
    """
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
        