from datetime import datetime

import utilidades as util


def menu_ventas(
    datos_ventas: dict, datos_inventario: dict, datos_empleados: dict
) -> None:
    """
    Muestra el menu de Ventas

    Pre: Recibe tres diccionarios como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_ventas = ("Registrar Venta", "Promociones", "Volver al Menu Principal")
        util.opciones("VENTAS", opciones_ventas)

        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1":
            registrar_ventas(datos_ventas, datos_inventario, datos_empleados)
        elif opcion == "2":
            aplicar_promocion(datos_inventario)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def impr_factura_venta(datos_venta: dict) -> None:
    """
    Imprime la factura de la venta correspondiente con los datos recibidos.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    util.limpiar_pantalla()
    util.imprimir_titulo("factura de venta")
    print(f"ID DE VENTA: {util.formatear_id(datos_venta['id'])}")
    print(f"FECHA DE EMISIÓN: {datos_venta['fecha_venta']}")
    print(f"EMPLEADO: {datos_venta['empleado_nombre']} (ID {datos_venta['empleado_id']})")
    print()
    for venta_producto in datos_venta["info_venta"]:
        id_producto = util.formatear_id(venta_producto["id"])
        nombre_producto = venta_producto["nombre"]
        cant_producto = venta_producto["cantidad"]
        costo_producto = venta_producto["costo"]

        cant_nombre_id = f"x{cant_producto} {nombre_producto.title()} - ID:{id_producto}"
        ancho = 45 - len(cant_nombre_id)
        print(f"{cant_nombre_id}{costo_producto:.>{ancho}.2f} $")

    mensaje_descuento = (
        f"(DESCUENTO: {datos_venta['descuento']: .2f} %)"
        if datos_venta["descuento"]
        else ""
    )
    util.imprimir_titulo(
        f"COSTO TOTAL: {datos_venta['venta']: .2f} $ {mensaje_descuento}"
    )


def _obtener_productos_activos(datos_inventario: dict) -> list[dict]:
    """
    Devuelve los productos activos disponibles para la venta.

    Pre: Recibe un diccionario como parámetro.
    Post: Retorna una lista de diccionarios.
    """

    return [
        producto
        for producto in datos_inventario.get("productos", [])
        if producto.get("estado") == "activo"
        and not producto.get("eliminado", False)
    ]


def _buscar_producto_por_id(datos_inventario: dict, producto_id: str) -> dict | None:
    for producto in datos_inventario.get("productos", []):
        if (producto.get("id") == producto_id and not producto.get("eliminado", False)):
            return producto
    return None


def _calcular_totales(items_venta: dict[str, dict], descuento: float) -> tuple[float, float]:
    """
    Calcula los totales bruto y neto aplicando el descuento.

    Pre: Recibe un diccionario de strings y diccionarios y un flotante como parámetro.
    Post: Retorna una tupla de dos flotantes.
    """

    total_bruto = sum(item["subtotal"] for item in items_venta.values())
    if not total_bruto:
        return 0.0, 0.0

    total_neto = (
        aplicar_descuento(total_bruto, descuento) if descuento else total_bruto
    )
    return total_bruto, total_neto


def _mostrar_resumen_venta(items_venta: dict[str, dict], descuento: float) -> None:
    """Muestra el detalle de los productos cargados y el total.

    Pre: Recibe un diccionario de strings y diccionarios y un flotante.
    Post: No retorna nada.
    """

    if not items_venta:
        print("No hay productos cargados en la venta actual.")
        util.guiones()
        return

    headers = ["Producto", "Cantidad", "Precio Unitario ($)", "Subtotal ($)"]
    data = [
        [
            item["nombre"].title(),
            item["cantidad"],
            f"{item['precio_unitario']:.2f}",
            f"{item['subtotal']:.2f}",
        ]
        for item in items_venta.values()
    ]
    util.imprimir_tabla(headers, data)

    total_bruto, total_neto = _calcular_totales(items_venta, descuento)
    util.guiones()
    print(f"Subtotal: ${total_bruto:.2f}")
    if descuento:
        print(f"Descuento aplicado: {descuento:.2f}%")
        print(f"Total con descuento: ${total_neto:.2f}")
    else:
        print(f"Total: ${total_neto:.2f}")


def _seleccionar_producto_en_venta(items_venta: dict[str, dict]) -> str | None:
    """
    Permite elegir un producto que ya esta en la venta.

    Pre: Recibe un diccionario de string y diccioanrios.
    Post: Retorna un string o un None.
    """

    if not items_venta:
        print("Aun no se agregaron productos a la venta.")
        input("Presione Enter para continuar...")
        return None

    productos = [
        {
            "id": producto_id,
            "nombre": f"{item['nombre'].title()} (x{item['cantidad']} - ${item['subtotal']:.2f})",
        }
        for producto_id, item in items_venta.items()
    ]
    _, seleccionado = util.seleccionar_item(
        productos, "producto", "PRODUCTOS EN LA VENTA"
    )
    if seleccionado is None:
        return None
    return seleccionado["id"]


def _agregar_producto_a_venta(
    items_venta: dict[str, dict],
    datos_inventario: dict,
    descuento: float,
) -> None:
    """
    Agrega un producto a la venta actual.

    Pre: Recibe un diccionario, otro diccionario de string y diccionarios y un flotante como parámetro.
    Post: No retorna nada.
    """

    productos_activos = _obtener_productos_activos(datos_inventario)
    if not productos_activos:
        print("No hay productos activos disponibles para la venta.")
        input("Presione Enter para continuar...")
        return

    _, producto = util.seleccionar_item(
        productos_activos, "producto", "AGREGAR PRODUCTO"
    )
    if producto is None:
        return

    disponible = producto["stock"] - items_venta.get(producto["id"], {}).get(
        "cantidad", 0
    )
    if disponible <= 0:
        print("No hay stock disponible para este producto.")
        input("Presione Enter para continuar...")
        return

    cantidad = util.pedir_entero(
        f"la cantidad de {producto['nombre'].title()}",
        max=disponible,
    )

    precio_unitario = producto.get("promocion") or producto["precio"]
    subtotal = precio_unitario * cantidad

    if producto["id"] in items_venta:
        items_venta[producto["id"]]["cantidad"] += cantidad
        items_venta[producto["id"]]["subtotal"] += subtotal
    else:
        items_venta[producto["id"]] = {
            "id": producto["id"],
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "subtotal": subtotal,
        }

    total_bruto, total_neto = _calcular_totales(items_venta, descuento)
    print(
        f"Se agrego {cantidad} unidad(es) de {producto['nombre'].title()} a la venta."
    )
    if descuento:
        print(
            f"Total parcial con descuento: ${total_neto:.2f} (subtotal ${total_bruto:.2f})"
        )
    else:
        print(f"Total parcial: ${total_neto:.2f}")
    input("Presione Enter para continuar...")


def _modificar_producto_en_venta(
    items_venta: dict[str, dict],
    datos_inventario: dict,
    descuento: float,
) -> None:
    """
    Permite ajustar la cantidad de un producto en la venta.

    Pre: Recibe un diccionario de string y diccionarios, un diccionario y un flotante.
    Post: No retorna nada.
    """

    producto_id = _seleccionar_producto_en_venta(items_venta)
    if producto_id is None:
        return

    producto = _buscar_producto_por_id(datos_inventario, producto_id)
    if producto is None:
        print("El producto ya no existe en el inventario.")
        input("Presione Enter para continuar...")
        return

    nueva_cantidad = util.pedir_entero(
        f"la nueva cantidad para {items_venta[producto_id]['nombre'].title()}",
        max=producto["stock"],
        min=0,
    )

    if nueva_cantidad == 0:
        del items_venta[producto_id]
        print("Producto eliminado de la venta.")
    else:
        precio_unitario = producto.get("promocion") or producto["precio"]
        items_venta[producto_id]["cantidad"] = nueva_cantidad
        items_venta[producto_id]["precio_unitario"] = precio_unitario
        items_venta[producto_id]["subtotal"] = precio_unitario * nueva_cantidad
        print("Cantidad actualizada correctamente.")

    total_bruto, total_neto = _calcular_totales(items_venta, descuento)
    if descuento and total_bruto:
        print(
            f"Total parcial con descuento: ${total_neto:.2f} (subtotal ${total_bruto:.2f})"
        )
    elif total_bruto:
        print(f"Total parcial: ${total_neto:.2f}")
    input("Presione Enter para continuar...")


def _quitar_producto_de_venta(
    items_venta: dict[str, dict], descuento: float
) -> None:
    """
    Elimina un producto de la venta actual.

    Pre: Recibe un diccionario de string y diccionarios y un flotante.
    Post: No retorna nada.
    """

    producto_id = _seleccionar_producto_en_venta(items_venta)
    if producto_id is None:
        return

    eliminado = items_venta.pop(producto_id, None)
    if eliminado is None:
        print("El producto seleccionado no forma parte de la venta.")
    else:
        print(
            f"Se quito {eliminado['nombre'].title()} de la venta (cantidad: {eliminado['cantidad']})."
        )

    total_bruto, total_neto = _calcular_totales(items_venta, descuento)
    if descuento and total_bruto:
        print(
            f"Total parcial con descuento: ${total_neto:.2f} (subtotal ${total_bruto:.2f})"
        )
    elif total_bruto:
        print(f"Total parcial: ${total_neto:.2f}")
    else:
        print("La venta ya no tiene productos cargados.")
    input("Presione Enter para continuar...")


def _gestionar_descuento(descuento_actual: float) -> float:
    """
    Permite aplicar o quitar un descuento a la venta.

    Pre: Recibe un flotante.
    Post: Retorna un flotante.
    """

    util.limpiar_pantalla()
    util.imprimir_titulo("DESCUENTO DE LA VENTA")
    print(f"Descuento actual: {descuento_actual:.2f}%")
    print("Ingrese 0 para quitar el descuento.")
    nuevo_descuento = util.pedir_float(
        "el porcentaje de descuento", max=98.0, min=0.0
    )
    return nuevo_descuento


def _confirmar_venta(
    items_venta: dict[str, dict],
    descuento: float,
    datos_ventas: dict,
    datos_inventario: dict,
    empleado: dict,
) -> bool:
    """
    Confirma la venta, actualiza inventario y guarda la informacion.

    Pre: Recibe cuatro diccionarios y un flotante como parámetro.
    Post: Retorna un booleano.
    """

    if not items_venta:
        print("Debe agregar al menos un producto para registrar la venta.")
        input("Presione Enter para continuar...")
        return False

    util.limpiar_pantalla()
    util.imprimir_titulo("CONFIRMAR VENTA")
    print(
        f"Empleado responsable: {empleado['nombre']} (ID {empleado['id']})"
    )
    util.guiones()
    _mostrar_resumen_venta(items_venta, descuento)
    util.guiones()

    if input("¿Desea confirmar la venta? (s/n): ").strip().lower() != "s":
        print("Venta cancelada antes de confirmar.")
        input("Presione Enter para continuar...")
        return False

    for item in items_venta.values():
        producto = _buscar_producto_por_id(datos_inventario, item["id"])
        if producto is None or producto.get("estado") != "activo":
            print(
                f"El producto {item['nombre'].title()} ya no esta disponible en el inventario."
            )
            input("Presione Enter para continuar...")
            return False
        if producto.get("eliminado", False):
            print(
                f"El producto {item['nombre'].title()} esta marcado como eliminado en el inventario."
            )
            input("Presione Enter para continuar...")
            return False
        if producto["stock"] < item["cantidad"]:
            print(
                f"Stock insuficiente para {item['nombre'].title()}. Disponible: {producto['stock']}"
            )
            input("Presione Enter para continuar...")
            return False

    for item in items_venta.values():
        producto = _buscar_producto_por_id(datos_inventario, item["id"])
        producto["stock"] -= item["cantidad"]

    total_bruto, total_neto = _calcular_totales(items_venta, descuento)
    info_venta = [
        {
            "id": item["id"],
            "nombre": item["nombre"],
            "cantidad": item["cantidad"],
            "costo": item["subtotal"],
        }
        for item in items_venta.values()
    ]

    informacion_venta = {
        "id": str(datos_ventas.get("prox_id", 1)),
        "venta": total_neto,
        "fecha_venta": str(datetime.now().date()),
        "info_venta": info_venta,
        "descuento": descuento,
        "empleado_id": empleado["id"],
        "empleado_nombre": empleado["nombre"],
    }

    datos_ventas.setdefault("ventas", []).append(informacion_venta)
    datos_ventas["prox_id"] = datos_ventas.get("prox_id", 1) + 1
    util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
    util.guardar_datos_json(util.ARCHIVO_VENTAS, datos_ventas)

    impr_factura_venta(informacion_venta)
    input("Presione Enter para continuar...")
    return True


def registrar_ventas(
    datos_ventas: dict, datos_inventario: dict, datos_empleados: dict
) -> None:
    """
    Registra ventas con un flujo interactivo mas cercano a un ERP real.

    Pre: Recibe tres diccionarios como parámetro.
    Post: No retorna nada.
    """

    if not datos_empleados.get("empleados"):
        print("No hay empleados registrados. Registre un empleado antes de continuar.")
        input("Presione Enter para continuar...")
        return

    if not _obtener_productos_activos(datos_inventario):
        print("No hay productos activos disponibles para vender.")
        input("Presione Enter para continuar...")
        return

    _, empleado = util.seleccionar_item(
        datos_empleados.get("empleados", []),
        "empleado",
        "NUEVA VENTA",
    )
    if empleado is None:
        return

    items_venta: dict[str, dict] = {}
    descuento = 0.0

    while True:
        util.limpiar_pantalla()
        util.imprimir_titulo("NUEVA VENTA")
        print(f"Empleado responsable: {empleado['nombre']} (ID {empleado['id']})")
        util.guiones()
        _mostrar_resumen_venta(items_venta, descuento)
        util.guiones()
        opciones_venta = (
    " Agregar producto",
    " Modificar cantidad",
    " Quitar producto",
    " Aplicar/Quitar descuento",
    " Confirmar venta",
    " Cancelar venta"
)
        util.opciones("PROMOCIONES", opciones_venta)
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            _agregar_producto_a_venta(items_venta, datos_inventario, descuento)
        elif opcion == "2":
            _modificar_producto_en_venta(items_venta, datos_inventario, descuento)
        elif opcion == "3":
            _quitar_producto_de_venta(items_venta, descuento)
        elif opcion == "4":
            descuento = _gestionar_descuento(descuento)
        elif opcion == "5":
            if _confirmar_venta(
                items_venta, descuento, datos_ventas, datos_inventario, empleado
            ):
                return
        elif opcion == "0":
            if not items_venta:
                return
            if input("¿Desea cancelar la venta actual? (s/n): ").strip().lower() == "s":
                print("Venta cancelada.")
                input("Presione Enter para continuar...")

                return
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def aplicar_descuento(valor: float, descuento: float) -> float:
    """
    Realiza un descuento y retorna el valor neto.

    Pre: Recibe dos flotantes como parámetros.
    Post: Retorna un flotante.
    """
    return valor * (1 - descuento / 100)


def aplicar_promocion(datos_inventario: dict) -> None:
    """
    Gestiona promociones para productos.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_prod = (
            "agregar promocion",
            "ver promocion",
            "eliminar promocion",
            "salir",
        )
        
        util.opciones("PROMOCIONES", opciones_prod)
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            clase = input("Ingrese a que categoria desea hacerle una promocion:")
            encontrado = False
            for producto in datos_inventario.get("productos", []):
                if producto.get("eliminado", False):
                    continue
                if producto["categoria"].strip().lower() == clase.strip().lower():
                    encontrado = True
                    descuento_a_aplicar = util.pedir_entero(
                        "el descuento que desea realizar (en %)", max=98
                    )
                    precio_descuento = aplicar_descuento(
                        producto["precio"], descuento_a_aplicar
                    )
                    producto["promocion"] = precio_descuento
                    print("Promocion registrada con exito.")
                    util.guardar_datos_json(
                        util.ARCHIVO_INVENTARIO, datos_inventario
                    )
                    input("Enter para continuar...")
                    break
            if not encontrado:
                print("Producto no encontrado.")
                input("Enter para continuar...")
        elif opcion == "2":
            hay_promociones = False
            for producto in datos_inventario.get("productos", []):
                if producto.get("eliminado", False):
                    continue
                if producto.get("promocion"):
                    hay_promociones = True
                    print(
                        f"Hay una promocion en el producto {producto['nombre']} esta a un valor {producto['promocion']} que pertenece a la categoria  {producto['categoria']}"
                    )
            if not hay_promociones:
                print("No hay promociones activas.")
            input("Enter para continuar...")
        elif opcion == "3":
            a_eliminar = input(
                "Ingrese a que categoria quiere eliminarle su promocion:"
            ).strip().lower()
            eliminado = False
            for producto in datos_inventario.get("productos", []):
                if producto.get("eliminado", False):
                    continue
                if producto["categoria"].strip().lower() == a_eliminar:
                    producto["promocion"] = None
                    eliminado = True
            if eliminado:
                util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
                print("Promocion eliminada con exito.")
            else:
                print("No se encontraron promociones para esa categoria.")
            input("Ingrese enter para continuar.")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")