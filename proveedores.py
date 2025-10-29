from datetime import datetime

import utilidades as util


def menu_proveedores(datos_proveedores: dict):
    """Menu principal de proveedores."""
    while True:
        util.limpiar_pantalla()
        opciones_prov = (
            "Registrar Proveedor",
            "Pedidos",
            "Buscar Proveedores",
            "Mostrar proveedores",
            "Volver al Menu Principal",
        )
        util.opciones("PROVEEDORES", opciones_prov)
        opcion = input("Ingrese una opcion: ").strip()

        if opcion == "1":
            registrar_provedores(datos_proveedores)
        elif opcion == "2":
            pedidos(datos_proveedores)
        elif opcion == "3":
            buscar_proveedor(datos_proveedores)
        elif opcion == "4":
            mostrar_proveedores(datos_proveedores)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_provedores(datos_proveedores: dict):
    """Registra nuevos proveedores."""
    datos_proveedores.setdefault("proveedores", [])
    datos_proveedores.setdefault("prox_id", 1)

    while True:
        validacion = lambda x, y: x != "" or y != ""
        util.limpiar_pantalla()
        opciones_prov = ("Registrar Proveedor", "Salir")
        util.opciones("REGISTAR PROVEEDORES", opciones_prov)
        opcion = input("Ingrese 0 para retroceder: ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            nombre = input("Ingrese el nombre del proveedor.").strip().lower()
            marca = input(
                "Ingrese la marca con la que trabaja el proveedor (De no haber presionar Enter): "
            ).lower().strip()
            tipo_de_productos = input(
                "Ingrese el tipo de productos con la que trabaja el proveedor (De no haber presionar Enter): "
            ).lower().strip()
            if validacion(marca, tipo_de_productos):
                proveedor = {
                        "nombre": nombre,
                        "marca": marca if marca else "NO INFO",
                        "tipo_de_producto": tipo_de_productos if tipo_de_productos else "NO INFO",
                        "fecha_alta": str(datetime.now().date()),
                        "pedido": [],
                    }
                datos_proveedores["proveedores"].append(proveedor)
                datos_proveedores["prox_id"] += 1
                util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
                print("Se Registro el proveedor correctamente.")
                input("Presione Enter para continuar...")
                break
            else:
                print(
                    "Debe cargar por lo menos una marca o tipo de productos especifico."
                )
                input("Enter para continuar.")


def pedidos(datos_proveedores: dict):
    """Gestiona los pedidos a proveedores."""
    while True:
        util.limpiar_pantalla()
        opciones_ = ("Registrar pedido", "ver pedidos", "eliminar pedidos", "salir")
        util.opciones("PEDIDOS A PROVEEDORES", opciones_)
        opcion = input("Ingrese una opcion (0 para retroceder): ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_pedidos(datos_proveedores)
        elif opcion == "2":
            ver_pedidos(datos_proveedores)
        elif opcion == "3":
            eliminar_pedidos(datos_proveedores)
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_pedidos(datos_proveedores: dict) -> None:
    """Registra pedidos para un proveedor."""
    indice, proveedor = util.seleccionar_item(
        datos_proveedores.get("proveedores", []),
        "proveedor",
        "registrar pedidos",
    )
    if proveedor is None:
        return

    pedido = []
    pedido_hecho = False
    print(
        "nota: Se le enviara un whatsapp automaticamente, tambien podras ver el pedido en el sistema."
    )
    while True:
        prod = input("Ingrese el producto que quiere pedir(0 para salir):").strip()
        if prod == "0":
            break
        while True:
            cantidad = util.pedir_entero("la cantidad de productos")
            if cantidad > 0:
                break
        pedido_hecho = True
        pedido.append((prod, cantidad))

    if pedido_hecho:
        proveedor["pedido"] = pedido
        util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
        print("Pedido realizado con exito.")
        input("Enter para continuar...")


def ver_pedidos(datos_proveedores: dict) -> None:
    """Muestra los pedidos registrados."""
    listado = 1
    for proveedor in datos_proveedores.get("proveedores", []):
        if len(proveedor.get("pedido", [])) > 0:
            print(f"{listado}.{proveedor['nombre']}")
            listado += 1
            for producto, cantidad in proveedor["pedido"]:
                print(f"-{producto}:{cantidad}")
    input("enter para continuar...")


def eliminar_pedidos(datos_proveedores: dict) -> None:
    """Elimina los pedidos de un proveedor."""
    while True:
        util.limpiar_pantalla()
        opciones_ = ("eliminar pedido", "salir")
        util.opciones("PEDIDOS A PROVEEDORES", opciones_)
        opcion = input("Ingrese una opcion: ").lower().strip()

        if opcion == "0":
            break
        elif opcion == "1":
            indice, proveedor = util.seleccionar_item(
                datos_proveedores.get("proveedores", []),
                "proveedor",
                "eliminar pedidos",
            )
            if proveedor is None:
                continue
            if len(proveedor.get("pedido", [])) > 0:
                proveedor["pedido"] = []
                print("Pedido eliminado correctamente!")
                util.guardar_datos_json(util.ARCHIVO_PROVEEDORES, datos_proveedores)
                input("Ingrese enter para continuar...")
            else:
                print(
                    f"el proveedor {proveedor['nombre']} no tiene pedidos registrados."
                )
                input("Enter para continuar...")
        else:
            print("Opcion invalida.")
            input("Enter para continuar...")


def buscar_proveedor(datos_proveedores: dict):
    """Permite buscar proveedores por diferentes criterios."""
    while True:
        util.limpiar_pantalla()
        opcion = input(
            "Ingrese 1 para buscar proveedores o 0 para salir: "
        ).strip()
        if opcion == "0":
            break
        elif opcion == "1":
            enumerador = 1
            busqueda = input(
                "Ingrese un nombre,marca o producto para buscar proveedor:"
            ).strip().lower()
            encontrado = False
            for proveedor in datos_proveedores.get("proveedores", []):
                if (
                    proveedor["nombre"] == busqueda
                    or proveedor["marca"] == busqueda
                    or proveedor["tipo_de_producto"] == busqueda
                ):
                    encontrado = True
                    print(
                        f"{enumerador}.{proveedor['nombre'].capitalize()}     -{proveedor['marca'].capitalize()}        -{proveedor['tipo_de_producto'].capitalize()}"
                    )
                    enumerador += 1
            if not encontrado:
                print("No hay informacion.")
            input("enter para continuar...")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def mostrar_proveedores(datos_proveedores: dict):
    """Muestra los proveedores y sus datos."""
    while True:
        util.limpiar_pantalla()
        util.guiones()
        print("Los proveedores son los siguientes.")
        util.guiones()

        if not datos_proveedores.get("proveedores"):
            print("No hay proveedores registrados.")
            input("Presione Enter para volver...")
            break

        for i, proveedor in enumerate(datos_proveedores["proveedores"]):
            print(f"{i + 1} - {proveedor['marca']}")
        proveedor_cual = input(
            "\nIngrese la marca o numero del proveedor (o 0 para volver): "
        )
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
            print("No se encontro ese proveedor.")
            input("Presione Enter para intentarlo de nuevo...")