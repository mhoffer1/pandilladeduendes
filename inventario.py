from datetime import datetime

import utilidades as util


def menu_inventario(datos_inventario: dict, datos_ventas: dict):
    """Muestra el menu de inventario"""
    while True:
        util.limpiar_pantalla()
        opciones_inv = (
            "Agregar Producto",
            "Ver Todos los Productos",
            "Ver Detalles del Producto",
            "Actualizar Producto",
            "Cambiar Estado Producto",
            "Eliminar Producto",
            "Buscar Producto",
            "Mostrar Productos con Bajo Stock",
            "Volver al Menu Principal",
        )
        util.opciones("INVENTARIO", opciones_inv)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregar_producto(datos_inventario)
        elif opcion == "2":
            ver_todos_los_productos(datos_inventario)
        elif opcion == "3":
            detalles_producto(datos_inventario)
        elif opcion == "4":
            actualizar_producto(datos_inventario)
        elif opcion == "5":
            estado_producto(datos_inventario)
        elif opcion == "6":
            eliminar_producto(datos_inventario, datos_ventas)
        elif opcion == "7":
            buscar_producto(datos_inventario)
        elif opcion == "8":
            alerta_stock_bajo(datos_inventario)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def agregar_producto(datos_inventario: dict):
    datos_inventario.setdefault("productos", [])
    datos_inventario.setdefault("prox_id", 1)

    while True:
        util.limpiar_pantalla()
        opciones_prod = ("Agregar Producto", "Salir")
        util.opciones("Añadir productos", opciones_prod)

        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break

        if opcion == "1":
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip().lower()

                costo = util.pedir_float("costo")
                precio = util.pedir_float("precio de venta")
                stock = util.pedir_entero("stock")

                categoria = input("Ingrese la categoria del producto: ").strip().lower()

                if precio > costo and precio > 50 and stock > 0:
                    alta_rotacion = input(
                        "Es un producto de alta rotacion? (1 si, 0 u otra tecla no.)"
                    )
                    alta_rotacion = "si" if alta_rotacion == "1" else "no"

                    producto = {
                        "id": str(datos_inventario["prox_id"]),
                        "nombre": nombre,
                        "costo": costo,
                        "precio": precio,
                        "stock": stock,
                        "alta_rotacion": alta_rotacion,
                        "categoria": categoria,
                        "fecha_alta": str(datetime.now().date()),
                        "ultima_modificacion": str(datetime.now().date()),
                        "estado": "activo",
                    }
                    datos_inventario["productos"].append(producto)
                    datos_inventario["prox_id"] += 1
                    util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
                    print("Se agrego el producto correctamente.")
                    input("Presione Enter para continuar...")
                    break

                print("precio invalido.")
                input("Presione Enter para continuar...")
            continue

        print("Opcion invalida. Intente de nuevo.")
        input("Presione Enter para continuar...")


def ver_todos_los_productos(datos_inventario: dict):
    productos = datos_inventario.get("productos", [])
    if not productos:
        util.limpiar_pantalla()
        util.imprimir_titulo("Productos en inventario")
        print("No hay productos cargados.")
        input("Presione Enter para continuar...")
        return

    headers = [
        "ID",
        "Nombre",
        "Precio",
        "Costo",
        "Stock",
        "Categoria",
        "Alta Rotacion",
        "Fecha Alta",
        "Ultima Modificacion",
        "Estado",
    ]
    util.imprimir_tabla_x_paginas(headers, productos, "Productos en Inventario")


def detalles_producto(datos_inventario: dict):
    while True:
        indice, producto = util.seleccionar_item(
            datos_inventario.get("productos", []), "producto", "DETALLES DE PRODUCTO"
        )
        if producto is None:
            break

        util.limpiar_pantalla()
        util.imprimir_titulo("DETALLES DE PRODUCTO")
        util.listar_datos(producto)

        input("\nPresione Enter para continuar...")


def actualizar_producto(datos_inventario: dict):
    while True:
        indice, producto = util.seleccionar_item(
            datos_inventario.get("productos", []),
            "producto",
            "ACTUALIZAR PRODUCTO",
        )
        if producto is None:
            break

        util.limpiar_pantalla()
        util.imprimir_titulo(
            f"ACTUALIZANDO PRODUCTO ID:{producto['id']} / {producto['nombre']}"
        )
        datos = (producto['precio'], producto['nombre'].title(), producto['costo'], producto['stock'], producto['categoria'].title(), producto['alta_rotacion'].title())
        titulos = ("Precio", "Nombre", "Costo", "Stock", "Categoría", "Alta Rotación")

        for dato, titulo in zip(datos, titulos):
            simbolo = "$" if isinstance(dato, float) else ""
            print(f"{titulo}: {simbolo}{dato}")

        opcion = input("Ingrese que desea actualizar: ").strip()
        if opcion == "1":
            producto["precio"] = util.pedir_float("un nuevo precio")
        elif opcion == "2":
            nuevo_nombre = input("Ingrese el nombre que desea modificar: ").strip().lower()
            producto["nombre"] = nuevo_nombre
        elif opcion == "3":
            producto["costo"] = util.pedir_float("el nuevo costo")
        elif opcion == "4":
            producto["stock"] = util.pedir_entero("el nuevo stock")
        elif opcion == "5":
            nueva_categoria = input("Ingrese la nueva categoria: ").strip().lower()
            producto["categoria"] = nueva_categoria
        elif opcion == "6":
            alta_rotacion = input(
                "Ingrese 1 si es de alta rotacion, 0 u otra cosa sino."
            )
            producto["alta_rotacion"] = "si" if alta_rotacion == "1" else "no"
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("Presione enter.")
            continue

        producto["ultima_modificacion"] = str(datetime.now().date())
        util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
        print("Producto actualizado y guardado correctamente.")
        input("Presione enter.")


def estado_producto(datos_inventario: dict):
    while True:
        indice, producto = util.seleccionar_item(
            datos_inventario.get("productos", []),
            "producto",
            "CAMBIAR ESTADO",
        )
        if producto is None:
            break

        estado_actual = producto.get("estado", "inactivo")
        print(f"El estado actual del producto es {estado_actual}.")
        confirmacion = input(
            f"\n¿Esta usted seguro de querer cambiar el estado de '{producto['nombre']}'? (1- Si, 0 u otra cosa- No): "
        )
        if confirmacion == "1":
            producto["estado"] = "inactivo" if estado_actual == "activo" else "activo"
            util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
            print("\nEstado cambiado con exito.")
        else:
            print("Operacion cancelada.")
        input("Presione Enter para continuar...")


def eliminar_producto(datos_inventario: dict, datos_ventas: dict):
    while True:
        indice, producto = util.seleccionar_item(
            datos_inventario.get("productos", []),
            "producto",
            "ELIMINAR PRODUCTO",
        )
        if producto is None:
            break

        vendido = any(
            producto["id"] == venta_producto.get("id")
            for venta in datos_ventas.get("ventas", [])
            for venta_producto in venta.get("info_venta", [])
        )

        if vendido:
            print(
                "No se puede eliminar un producto con historial de ventas. Use 'Cambiar Estado Producto' para desactivarlo."
            )
            input("Presione Enter para continuar...")
            continue

        confirmacion = input(
            f"¿Esta seguro de eliminar el producto '{producto['nombre']}'? (1- Si, 0 u otra cosa- No): "
        )
        if confirmacion == "1":
            del datos_inventario["productos"][indice]
            util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
            print("Producto eliminado correctamente.")
        else:
            print("Operacion cancelada.")
        input("Presione Enter para continuar...")


def buscar_por_nombre(productos: list[dict]) -> list[dict]:
    """
    Busca el nombre ingresado en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR NOMBRE")
    a_buscar = input("Ingrese el nombre a buscar: ").lower().strip()
    coincidencias = [
        producto
        for producto in productos
        if a_buscar in producto["nombre"]
    ]

    return coincidencias


def buscar_por_categ(productos: list[dict]) -> list[dict]:
    """
    Busca la categoría ingresada en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR CATEGORÍA")
    a_buscar = input("Ingrese la categoria a buscar: ").lower().strip()
    coincidencias = [
        producto
        for producto in productos
        if a_buscar in producto["categoria"]
    ]

    return coincidencias


def buscar_por_precios(productos: list[dict]) -> list[dict]:
    """
    Busca el rango de precios ingresado en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR PRECIO")
    print("A continuacion ingrese el rango de precios que desea buscar...\n")

    precio_min = util.pedir_float("precio minimo")
    precio_max = util.pedir_float("precio maximo", min=precio_min)
    coincidencias = [
        producto
        for producto in productos
        if producto["precio"] >= precio_min
        and producto["precio"] <= precio_max
    ]

    return coincidencias

def buscar_por_stock(productos: list[dict]) -> list[dict]:
    """
    Busca el rango de stock ingresado en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR STOCK")
    print("A continuacion ingrese el rango de valores de stock que desea buscar...\n")

    stock_min = util.pedir_entero("stock minimo")
    stock_max = util.pedir_entero("stock maximo", min=stock_min)
    coincidencias = [
        producto
        for producto in productos
        if producto["stock"] >= stock_min
        and producto["stock"] <= stock_max
    ]

    return coincidencias


def buscar_por_rotacion(productos: list[dict]) -> list[dict]:
    """
    Busca el tipo de rotación ingresado en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR ROTACIÓN")
    a_buscar = input(
        "Ingrese el valor de rotacion del producto (1- Alta Rotacion, 0 u otra cosa- Baja Rotacion): "
    ).strip()

    a_buscar = "si" if a_buscar == "1" else "no"
    coincidencias = [
        producto
        for producto in productos
        if producto["alta_rotacion"] == a_buscar
    ]

    return coincidencias


def buscar_por_estado(productos: list[dict]) -> list[dict]:
    """
    Busca el estado (activo o inactivo) ingresado en la base de datos de productos.

    Pre: Recibe como parametro la lista de diccionarios correspondientes a los productos almacenados.
    Post: Retorna una lista con los diccionarios correspondientes a los productos que coinciden con la búsqueda.
    """
    util.imprimir_titulo("BUSQUEDA POR ESTADO")
    a_buscar = input(
        "Ingrese el estado del producto (1- Activo, 0 u otra cosa- Inactivo): "
    ).strip()

    a_buscar = "activo" if a_buscar == "1" else "inactivo" #si a buscar es 1 se filtran los activos, caso contrario los inactivos.
    coincidencias = [
        producto
        for producto in productos
        if producto["estado"] == a_buscar
    ]

    return coincidencias


def buscar_producto(datos_inventario: dict):
    opciones_prod = ("buscar producto", "salir")
    while True:
        util.limpiar_pantalla()
        util.opciones("buscar producto", opciones_prod)
        opcion = input("Ingrese una opcion:")
        if opcion == "0":
            break
        elif opcion == "1":
            util.limpiar_pantalla()
            if not datos_inventario.get("productos"):
                print("No se encontraron productos cargados.")
                input("Presione Enter para continuar...")
                break

            while True:
                util.limpiar_pantalla()
                opciones_de_busqueda = (
                    "Nombre",
                    "Categoria",
                    "Precio",
                    "Stock",
                    "Alta Rotacion",
                    "Estado",
                    "Volver Atras",
                )
                util.opciones("buscar producto", opciones_de_busqueda)

                op = input("Ingrese por cual caracteristica desea buscar: ")
                if op == "0":
                    break

                util.limpiar_pantalla()
                lista_productos = datos_inventario.get("productos", [])

                if op == "1":
                    coincidencias = buscar_por_nombre(lista_productos)
                elif op == "2":
                    coincidencias = buscar_por_categ(lista_productos)
                elif op == "3":
                    coincidencias = buscar_por_precios(lista_productos)
                elif op == "4":
                    coincidencias = buscar_por_stock(lista_productos)
                elif op == "5":
                    coincidencias = buscar_por_rotacion(lista_productos)
                elif op == "6":
                    coincidencias = buscar_por_estado(lista_productos)
                else:
                    print("Opción inválida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    continue

                if not coincidencias:
                    print("No se encontraron productos con esas caracteristicas.")
                    input("Presione Enter para continuar...")
                    continue

                headers = [
                    "ID",
                    "Nombre",
                    "Precio",
                    "Costo",
                    "Stock",
                    "Categoria",
                    "Alta Rotacion",
                    "Fecha Alta",
                    "Ultima Modificacion",
                    "Estado"
                ]
                util.imprimir_tabla_x_paginas(
                    headers, coincidencias, "Resultados de Busqueda"
                )
        else:
            print("Opcion invalida. Intente nuevamente.")
            input("Presione Enter para continuar...")


def alerta_stock_bajo(datos_inventario: dict):
    while True:
        util.limpiar_pantalla()
        opciones_alertas = ("Ver alertas de Alta rotacion", "Ver todas las alertas", "salir")
        util.opciones("buscar producto", opciones_alertas)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        elif opcion == "1":
            encontrados = False
            contador = 1
            for producto in datos_inventario.get("productos", []):
                if (
                    producto["alta_rotacion"] == "si"
                    and producto["stock"] <= 20
                    and producto.get("estado") == "activo"
                ):
                    print(f"{contador}.{producto['nombre'].title()}")
                    contador += 1
                    encontrados = True
            if encontrados:
                input("enter para continuar...")
            else:
                print("No se encontraron productos.")
                input("enter para continuar...")

        elif opcion == "2":
            encontrados = False
            enumerador = 1
            for producto in datos_inventario.get("productos", []):
                if producto["stock"] <= 20 and producto.get("estado") == "activo":
                    print(f"{enumerador}.{producto['nombre'].title()}")
                    enumerador += 1
                    encontrados = True
            if encontrados:
                input("enter para continuar...")
            else:
                print("No se encontraron productos.")
                input("enter para continuar...")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

