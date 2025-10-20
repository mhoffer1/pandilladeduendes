import utilidades as util
from datetime import datetime
datos_proveedores = util.cargar_datos_json(util.ARCHIVO_PROVEEDORES)
def menu_proveedores():
    """"
    menu de proveedores, te permite hacer todas las acciones.
    """
    while True:
        util.limpiar_pantalla()
        opciones_prov = ("Registrar Proveedor", "Pedidos", "Buscar Proveedores","Mostrar proveedores", "Volver al Menú Principal")
        util.opciones("PROVEEDORES", opciones_prov)
        opcion = input("Ingrese una opcion: ")
    
        if opcion == "1":
            registrar_provedores()
        elif opcion == "2":
            pedidos()
        elif opcion == "3":
            buscar_proveedor()
        elif opcion == "4":
            mostrar_proveedores()
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
                            "fecha_alta": str(datetime.now().date()),
                            "pedido" : []
                                }
                elif marca != "" and tipo_de_productos == "":
                    proveedor = {
                            "nombre": nombre,
                            "marca" : marca,
                            "tipo_de_producto" : "NO INFO.",
                            "fecha_alta": str(datetime.now().date()),
                            "pedido" : []
                            
                                }
                else:
                    proveedor = {
                            "nombre" :nombre,
                            "marca" : "NO INFO",
                            "tipo_de_producto" : tipo_de_productos,
                            "fecha_alta": str(datetime.now().date()),
                            "pedido" : []
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

def pedidos():  
    """
    Sirve para solicitar productos a un proveedor, debe ingresarse el provedor, producto/s
    y cantidad.
    """
    while True:
        pedido = list()
        util.limpiar_pantalla()
        opciones_ = ("Registrar pedido","ver pedidos","eliminar pedidos","salir")
        util.opciones("PEDIDOS A PROVEEDORES",opciones_)
        opcion = input("Ingrese una opcion (0 para retroceder): ")
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_pedidos()
        
        elif opcion == "2":
            ver_pedidos()
        
        elif opcion == "3":
            eliminar_pedidos()
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

            
def registrar_pedidos() ->None:
            pedido = list()
            busqueda = input("Ingrese el nombre del proveedor:").strip().lower()
            encontrado = False
            for proveedor in datos_proveedores["proveedores"]:
                if proveedor["nombre"].strip().lower() == busqueda:
                    encontrado = True
                    pedido_hecho = False
                    print("nota: Se le enviara un whatsapp automaticamente, tambien podras ver el pedido en el sistema.")
                    while True:
                        prod = input("Ingrese el producto que quiere pedir(0 para salir):")
                        if prod == "0":
                            break
                        else:
                            while True:
                                cantidad = input("Ingrese la cantidad de productos:")
                                try:
                                    cantidad = int(cantidad)
                                    break
                                except Exception as e:
                                    print("Debe ser un numero entero.")
                            pedido_hecho = True
                            subpedido = (prod,cantidad)
                            pedido.append(subpedido)
                    if pedido_hecho:
                        proveedor["pedido"] = pedido
                        util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
                        print("Pedido realizado con exito.")
                        input("Enter para continuar...")
                        break
            if not encontrado:
                print("No encontrado.")
                input("enter para continuar...")



def ver_pedidos()->None:
    "se invoca desde solicitar_productos. Sirve para ver los pedidos hacia los proveedores."
    listado = 1
    for proveedor in datos_proveedores["proveedores"]:
        if len(proveedor["pedido"]) > 0: #osea, si el pedido  existe(todos tienen el key de pedido para evitar errores.)
            print(f"{listado}.{proveedor["nombre"]}")
            listado += 1
            for producto,cantidad in (proveedor["pedido"]):
                print(f"-{producto}:{cantidad}")
    input("enter para continuar...")
                
def eliminar_pedidos()->None:
    ""
    while True:
        util.limpiar_pantalla()
        opciones_ = ("eliminar pedido","salir")
        util.opciones("PEDIDOS A PROVEEDORES",opciones_)
        opcion = input("Ingrese una opcion: ").lower().strip()
    
        if opcion == "0":
            break
        elif opcion == "1":
            nombre = input("Ingrese el nombre del proveedor:")
            encontrado = False
            for proveedor in datos_proveedores["proveedores"]:
                if nombre == proveedor["nombre"]:
                    encontrado = True
                    if len(proveedor["pedido"]) > 0:
                        proveedor["pedido"] = [] #vuelve a estar vacia, como de manera default
                        print("Pedido eliminado correctamente!")
                        util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
                        input("Ingrese enter para continuar...")
                        break
                    else:
                        print(f"el proveedor {proveedor["nombre"]} no tiene pedidos registrados.")
                        input("Enter para continuar...")
                        break
            if not encontrado:
                    print("Vendedor no encontrado.")
                    input("Ingrese enter para continuar...")
                    break
        else:
            print("Opcion invalida.")
            input("Enter para continuar...")



#pagos pendientes eliminado.



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


def mostrar_proveedores():
    while True:
        util.limpiar_pantalla()
        util.guiones()
        print("Los proveedores son los siguientes.")
        util.guiones()

        if not datos_proveedores["proveedores"]:
            print("No hay proveedores registrados.")
            input("Presione Enter para volver...")
            break

        for i, proveedor in enumerate(datos_proveedores["proveedores"]):
            print(f"{i + 1} - {proveedor['marca']}")
        proveedor_cual = input("\nIngrese la marca o número del proveedor (o 0 para volver): ")
        util.limpiar_pantalla()
        if proveedor_cual == "0":
            break
        encontrado = False
        if proveedor_cual.isdigit():
            indice = int(proveedor_cual) - 1
            if 0 <= indice < len(datos_proveedores["proveedores"]):
                proveedor1 = datos_proveedores["proveedores"][indice]
                encontrado = True
        else:
            for proveedor1 in datos_proveedores["proveedores"]:
                if proveedor_cual.lower() == proveedor1["marca"].lower():
                    encontrado = True
                    break
        if encontrado:
            print("\nDatos del proveedor:")
            for clave, valor in proveedor1.items():
                print(f"{clave}: {valor}")
            input("\nPresione Enter para continuar...")
        else:
            print("No se encontró ese proveedor.")
            input("Presione Enter para intentarlo de nuevo...")