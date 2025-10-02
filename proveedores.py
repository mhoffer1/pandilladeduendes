from utilidades import limpiar_pantalla, guiones, opciones

def menu_proveedores():
    """"
    menu de proveedores, te permite hacer todas las acciones.
    """
    while True:
        limpiar_pantalla()
        opciones_prov = ("Registrar Proveedor", "Solicitar Productos a Proveedor", "Ver Pagos Pendientes", "Ver Historial de Compras", "Buscar Proveedores", "Volver al Menú Principal")
        opciones("PROVEEDORES", opciones_prov)
        opcion = input("Ingrese una opcion: ")
    
        if opcion == "1":
            registrar_provedores()
        elif opcion == "2":
            solicitar_productos()
        elif opcion == "3":
            pagos_pendientes()
        elif opcion == "4":
            historial_de_compras()
        elif opcion == "5":
            buscar_proveedor()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            

def registrar_provedores():
    """"
    Registra provedores con su nombre.
    """

    while True:
        limpiar_pantalla()
        guiones()
        print("REGISTRAR PROVEEDORES")
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def solicitar_productos():
    """
    Sirve para solicitar productos a un proveedor, debe ingresarse el provedor, producto/s
    y cantidad.
    """
    while True:
        limpiar_pantalla()
        guiones()
        print("SOLICITAR A PROVEEDORES")
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def pagos_pendientes():
    """
    Podes ver pagos pendientes a proveedores
    """
    while True:
        limpiar_pantalla()
        guiones()
        print("PAGOS PENDIENTES")
        guiones()
        opcion = input("Ingrese 0 para retroceder:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def historial_de_compras():
    while True:
        """
        Podes ver el historial de compras a cada proveedor
        """
        limpiar_pantalla()
        guiones()
        print("HISTORIAL DE COMPRAS")
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def buscar_proveedor():
    """
    Podes buscar proveedores por nombre y apellido.
    """
    while True:
        limpiar_pantalla()
        guiones()
        print("BUSCAR PROVEEDOR")
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        