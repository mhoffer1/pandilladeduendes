import utilidades as util
from datetime import datetime
datos_proveedores = util.cargar_datos_json(util.ARCHIVO_PROVEEDORES)
def menu_proveedores():
    """"
    menu de proveedores, te permite hacer todas las acciones.
    """
    while True:
        util.limpiar_pantalla()
        opciones_prov = ("Registrar Proveedor", "Solicitar Productos a Proveedor", "Ver Pagos Pendientes", "Ver Historial de Compras", "Buscar Proveedores", "Volver al Menú Principal")
        util.opciones("PROVEEDORES", opciones_prov)
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
        validacion = lambda x,y: x != "" or y != "" #para chequear datos en linea 48!
        util.limpiar_pantalla()
        opciones_prov = ("Registrar Proveedor","Salir")
        util.opciones("REGISTAR PROVEEDORES", opciones_prov)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        elif opcion == "1":
            nombre = input("Ingrese el nombre del proveedor.").strip().lower()
            marca = input("Ingrese la marca con la que trabaja con el proveedor(si no trabaja con una marca en especico, presiona enter):").lower().strip()
            tipo_de_productos = input("Ingres el tipo de productos con el que trabaja el proveedor(si no traba con un tipo de productos en especifico, presiona enter).").lower().strip()
            if validacion(marca,tipo_de_productos):
                if marca != "" and tipo_de_productos != "":
                    proveedor = {
                            "nombre": nombre,
                            "marca" : marca,
                            "tipo_de_producto": tipo_de_productos,
                            "fecha_alta": str(datetime.now().date())
                                }
                elif marca != "" and tipo_de_productos == "":
                    proveedor = {
                            "nombre": nombre,
                            "marca" : marca,
                            "tipo_de_producto" : "NO INFO.",
                            "fecha_alta": str(datetime.now().date()),
                            
                                }
                else:
                    proveedor = {
                            "nombre" :nombre,
                            "marca" : "NO INFO",
                            "tipo_de_producto" : tipo_de_productos,
                            "fecha_alta": str(datetime.now().date())
                    }
                datos_proveedores["proveedores"].append(proveedor)
                datos_proveedores["prox_id"] += 1
                util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
                print("Se Registro el proveedor correctamente.")
                input("Presione Enter para continuar...")
                break
            else:
                print("Debe cargar por lo menos una marca o tipo de productos especifico.")
                input("Enter para continuar.")

def solicitar_productos():  
    """
    Sirve para solicitar productos a un proveedor, debe ingresarse el provedor, producto/s
    y cantidad.
    """
    while True:
        util.limpiar_pantalla()
        util.guiones()
        print("SOLICITAR A PROVEEDORES")
        util.guiones()
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
        util.limpiar_pantalla()
        util.guiones()
        print("PAGOS PENDIENTES")
        util.guiones()
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
        util.limpiar_pantalla()
        util.guiones()
        print("HISTORIAL DE COMPRAS")
        util.guiones()
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
        util.limpiar_pantalla()
        opciones_proveedor = ("Buscar Proveedor","Salir")
        util.opciones("BUSCAR PROVEEDORES",opciones_proveedor)
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        elif opcion == "1":
            enumerador = 1
            busqueda = input("Ingrese un nombre,marca o producto para buscar proveedor:").strip().lower()
            encontrado = False
            for proveedor in datos_proveedores["proveedores"]:
                if proveedor["nombre"] == busqueda or proveedor["marca"] == busqueda or proveedor["tipo_de_producto"] == busqueda:
                    encontrado = True
                    print(f"{enumerador}.{proveedor["nombre"].capitalize()}     -{proveedor["marca"].capitalize()}        -{proveedor["tipo_de_producto"].capitalize()}")
                    enumerador+= 1
            if not encontrado:
                print("No hay informacion.")
            input("enter para continuar...")

        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        