from collections import defaultdict
from datetime import datetime

import utilidades as util


def _productos_por_id(datos_inventario: dict) -> dict:
    """Genera un mapeo rapido de ID de producto a su informacion.
    Pre: Recibe un diccionario como parámetro.
    Post: Retorna un diccionario.
    """
    return {
        producto.get("id"): producto
        for producto in datos_inventario.get("productos", [])
        if producto.get("id") is not None
        and not producto.get("eliminado", False)
    }


def mostrar_reporte_inventario(datos_inventario: dict)->None:
    """
    Permite el reporte de inventario

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_alertas = (
            "ver productos inactivos",
            "Ver valor total del inventario",
            "Ver valor por categoria",
            "salir",
        )
        util.opciones("REPORTES INVENTARIO", opciones_alertas)
        opcion = input("Ingrese una opcion : ")
        if opcion == "0":
            break
        elif opcion == "1":
            ver_inactivos(datos_inventario)
        elif opcion == "2":
            ver_valor_del_inventario(datos_inventario)
        elif opcion == "3":
            valor_inventario_por_categoria(datos_inventario)
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def ver_valor_del_inventario(datos_inventario: dict)->None:
    """
    Permite ver valores generales del inventario.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    print(
        "NOTA: Para calcular el valor total de su inventario se considera el precio que usted pago, es decir, el COSTO de los productos."
    )
    total_AR, total_NOAR = 0, 0

    for producto in datos_inventario.get("productos", []):
        if producto.get("eliminado", False):
            continue
        if producto["alta_rotacion"] == "si":
            total_AR += producto["costo"] * producto["stock"]
        else:
            total_NOAR += producto["costo"] * producto["stock"]
    print(f"El valor total de su inventario es de: ${total_AR + total_NOAR}")
    print(f"${total_AR} son de productos de alta rotacion.")
    print(f"${total_NOAR} son de productos que NO son de alta rotacion.")
    input("Enter para continuar...")


def ver_inactivos(datos_inventario: dict)->None:
    """
    Permite ver inactivos

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    contador = 0
    for producto in datos_inventario.get("productos", []):
        if producto.get("eliminado", False):
            continue
        if producto.get("estado") != "activo":
            contador += 1
            print(f"{contador}.producto:{producto['nombre']}. ID:{producto['id']}")
    if contador == 0:
        print("No hay productos inactivos.")
    input("enter para continuar...")


def valor_inventario_por_categoria(datos_inventario: dict)->None:
    """
    Resume el valor y stock disponible agrupado por categoria.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    resumen = defaultdict(lambda: {"valor": 0.0, "stock": 0, "activos": 0, "inactivos": 0})
    for producto in datos_inventario.get("productos", []):
        if producto.get("eliminado", False):
            continue
        categoria = producto.get("categoria", "sin categoria")
        estado = producto.get("estado", "inactivo")
        stock = producto.get("stock", 0)
        valor = producto.get("costo", 0.0) * stock

        datos_categoria = resumen[categoria]
        datos_categoria["valor"] += valor
        datos_categoria["stock"] += stock
        if estado == "activo":
            datos_categoria["activos"] += 1
        else:
            datos_categoria["inactivos"] += 1

    if not resumen:
        print("No hay productos registrados.")
        input("Enter para continuar...")
        return

    datos_tabla = [
        {
            "categoria": categoria,
            "stock_total": valores["stock"],
            "valor": round(valores["valor"], 2),
            "activos": valores["activos"],
            "inactivos": valores["inactivos"],
        }
        for categoria, valores in sorted(
            resumen.items(), key=lambda item: item[1]["valor"], reverse=True
        )
    ]

    headers = [
        "Categoria",
        "Stock Total",
        "Valor Inventario ($)",
        "Productos Activos",
        "Productos Inactivos",
    ]
    util.imprimir_tabla_x_paginas(headers, datos_tabla, "VALOR POR CATEGORIA")

    valor_total = sum(valores["valor"] for valores in resumen.values())
    print(f"Valor total de inventario: ${valor_total:.2f}")
    input("Enter para continuar...")


def mostrar_reporte_venta(
    datos_ventas: dict, datos_inventario: dict, datos_empleados: dict
)->None:
    """
    Permite ver el reporte de venta.

    Pre: Recibe tres diccionarios como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_venta = (
            "mostrar ventas por periodo de tiempo",
            "Ventas por empleado",
            "Top productos vendidos",
            "Margen por producto",
            "Ventas por categoria",
            "salir",
        )

        util.opciones("REPORTES VENTA", opciones_venta)
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        elif opcion == "1":
            mostrar_reporte_por_periodo(datos_ventas)
        elif opcion == "2":
            reporte_ventas_por_empleado(datos_ventas, datos_empleados)
        elif opcion == "3":
            reporte_top_productos(datos_ventas, datos_inventario)
        elif opcion == "4":
            reporte_margen_por_producto(datos_ventas, datos_inventario)
        elif opcion == "5":
            reporte_ventas_por_categoria(datos_ventas, datos_inventario)
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def mostrar_reporte_por_periodo(datos_ventas: dict)->None:
    """
    Muestra reportes por período.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_venta = (
            "reporte diario",
            "reporte mensual",
            "reporte del año",
            "salir",
        )
        util.opciones("REPORTES VENTA", opciones_venta)
        opcion = input("Ingrese  una opcion: ")

        if opcion == "1":
            _generar_reporte_ventas(datos_ventas, "%Y-%m-%d", "VENTAS DIARIAS")
        elif opcion == "2":
            _generar_reporte_ventas(datos_ventas, "%Y-%m", "VENTAS MENSUALES")
        elif opcion == "3":
            _generar_reporte_ventas(datos_ventas, "%Y", "VENTAS ANUALES")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("enter para continuar.")


def _generar_reporte_ventas(datos_ventas: dict, formato_fecha: str, titulo: str)->None:
    """
    Permite generar reportes de ventas.

    Pre: Recibe un diccionario y dos strings como parámetro.
    Post: No retorna nada.
    """
    datos_para_la_tabla = []
    headers = ["id", "monto", "fecha_venta"]
    periodo_actual = datetime.now().strftime(formato_fecha)
    monto_total = 0

    for venta in reversed(datos_ventas.get("ventas", [])):
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")
        if periodo_actual == fecha_en_str.strftime(formato_fecha):
            datos_para_la_tabla.append(
                {
                    "id": venta["id"],
                    "monto": venta["venta"],
                    "fecha_venta": venta["fecha_venta"],
                }
            )
            monto_total += venta["venta"]
        else:
            break

    if datos_para_la_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, titulo)
        print(f"El monto total es de ${monto_total}")
    else:
        print("No se registraron ventas en el periodo seleccionado.")
    input("Enter para continuar...")


def reporte_ventas_por_empleado(datos_ventas: dict, datos_empleados: dict)->None:
    """
    Muestra reportes de ventas por empleado.

    Pre: Recibe dos diccionarios como parámetro.
    Post: No retorna nada.
    """
    resumen = defaultdict(lambda: {"total": 0.0, "cantidad": 0})
    for venta in datos_ventas.get("ventas", []):
        nombre = venta.get("empleado_nombre", "Sin asignar")
        resumen[nombre]["total"] += venta.get("venta", 0)
        resumen[nombre]["cantidad"] += 1

    if not resumen:
        print("No hay ventas registradas.")
        input("Enter para continuar...")
        return

    datos_para_tabla = [
        {
            "nombre": nombre,
            "total": valores["total"],
            "cantidad": valores["cantidad"],
        }
        for nombre, valores in resumen.items()
    ]

    headers = ["Empleado", "Total Ventas ($)", "Cantidad de Ventas"]
    util.imprimir_tabla_x_paginas(headers, datos_para_tabla, "VENTAS POR EMPLEADO")
    input("Enter para continuar...")


def reporte_top_productos(datos_ventas: dict, datos_inventario: dict)->None:
    """
    Muestra los productos en orden.

    Pre: Recibe dos diccionario como parámetro.
    Post: No retorna nada.
    """
    acumulado = defaultdict(int)
    for venta in datos_ventas.get("ventas", []):
        for producto in venta.get("info_venta", []):
            acumulado[producto["id"]] += producto.get("cantidad", 0)

    if not acumulado:
        print("No hay ventas registradas.")
        input("Enter para continuar...")
        return

    productos_por_id = _productos_por_id(datos_inventario)

    top_productos = sorted(
        (
            {
                "producto": productos_por_id.get(id_producto, {}).get(
                    "nombre", f"ID {id_producto}"
                ),
                "cantidad": cantidad,
            }
            for id_producto, cantidad in acumulado.items()
        ),
        key=lambda item: item["cantidad"],
        reverse=True,
    )[:5]

    headers = ["Producto", "Total Vendido"]
    util.imprimir_tabla_x_paginas(headers, top_productos, "TOP PRODUCTOS")
    input("Enter para continuar...")


def reporte_margen_por_producto(
    datos_ventas: dict, datos_inventario: dict
) -> None:
    """
    Calcula ingresos, costos estimados y margen por producto vendido.

    Pre: Recibe dos diccionarios como parámetro.
    Post: No retorna nada.
    """
    productos_por_id = _productos_por_id(datos_inventario)
    resumen = defaultdict(
        lambda: {"nombre": "", "cantidad": 0, "ingreso": 0.0, "costo": 0.0}
    )

    for venta in datos_ventas.get("ventas", []):
        for item in venta.get("info_venta", []):
            prod_id = item.get("id")
            cantidad = int(item.get("cantidad", 0) or 0)
            ingreso = float(item.get("costo", 0.0) or 0.0)

            producto = productos_por_id.get(prod_id, {})
            nombre = producto.get("nombre", item.get("nombre", f"ID {prod_id}"))
            costo_unitario = float(producto.get("costo", 0.0) or 0.0)

            datos_producto = resumen[prod_id]
            datos_producto["nombre"] = nombre
            datos_producto["cantidad"] += cantidad
            datos_producto["ingreso"] += ingreso
            datos_producto["costo"] += costo_unitario * cantidad

    if not resumen:
        print("No hay ventas registradas.")
        input("Enter para continuar...")
        return

    datos_tabla = []
    for valores in resumen.values():
        ingreso = valores["ingreso"]
        costo = valores["costo"]
        margen = ingreso - costo
        margen_pct = (margen / ingreso * 100) if ingreso else 0.0
        datos_tabla.append(
            {
                "producto": valores["nombre"],
                "cantidad": valores["cantidad"],
                "ingreso": round(ingreso, 2),
                "costo": round(costo, 2),
                "margen": round(margen, 2),
                "margen_%": round(margen_pct, 2),
            }
        )

    datos_tabla.sort(key=lambda item: item["margen"], reverse=True)

    headers = [
        "Producto",
        "Cantidad Vendida",
        "Ingresos ($)",
        "Costos ($)",
        "Margen ($)",
        "Margen (%)",
    ]
    util.imprimir_tabla_x_paginas(headers, datos_tabla, "MARGEN POR PRODUCTO")

    total_ingresos = sum(item["ingreso"] for item in datos_tabla)
    total_costos = sum(item["costo"] for item in datos_tabla)
    total_margen = total_ingresos - total_costos
    print(f"Ingresos totales: ${total_ingresos:.2f}")
    print(f"Costos estimados: ${total_costos:.2f}")
    print(f"Margen estimado: ${total_margen:.2f}")
    input("Enter para continuar...")


def reporte_ventas_por_categoria(
    datos_ventas: dict, datos_inventario: dict
) -> None:
    """
    Agrupa ventas por categoria de producto.

    Pre: Recibe dos diccionarios como parámetro.
    Post: No retorna nada.
    """

    productos_por_id = _productos_por_id(datos_inventario)
    resumen = defaultdict(lambda: {"cantidad": 0, "ingreso": 0.0})

    for venta in datos_ventas.get("ventas", []):
        for item in venta.get("info_venta", []):
            prod_id = item.get("id")
            producto = productos_por_id.get(prod_id, {})
            categoria = producto.get("categoria", "sin categoria")

            cantidad = int(item.get("cantidad", 0) or 0)
            ingreso = float(item.get("costo", 0.0) or 0.0)

            resumen[categoria]["cantidad"] += cantidad
            resumen[categoria]["ingreso"] += ingreso

    if not resumen:
        print("No hay ventas registradas.")
        input("Enter para continuar...")
        return

    total_ingresos = sum(valores["ingreso"] for valores in resumen.values())

    datos_tabla = []
    for categoria, valores in resumen.items():
        ingreso = valores["ingreso"]
        participacion = (ingreso / total_ingresos * 100) if total_ingresos else 0.0
        datos_tabla.append(
            {
                "categoria": categoria,
                "cantidad": valores["cantidad"],
                "ingreso": round(ingreso, 2),
                "participacion_%": round(participacion, 2),
            }
        )

    datos_tabla.sort(key=lambda item: item["ingreso"], reverse=True)

    headers = [
        "Categoria",
        "Cantidad Vendida",
        "Ingresos ($)",
        "Participacion (%)",
    ]
    util.imprimir_tabla_x_paginas(headers, datos_tabla, "VENTAS POR CATEGORIA")
    print(f"Ingresos totales: ${total_ingresos:.2f}")
    input("Enter para continuar...")


def mostrar_reporte_empleados(datos_empleados: dict) -> None:
    """
    Ver el reporte de los empleados.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    while True:
        util.limpiar_pantalla()
        opciones_empleados = ("reporte asistencias", "reporte sueldos.", "salir")

        util.opciones("REPORTES EMPLEADOS", opciones_empleados)
        opcion = input("Ingrese  una opcion: ")

        if opcion == "0":
            break
        elif opcion == "1":
            reporte_asistencias(datos_empleados)
        elif opcion == "2":
            reporte_sueldos(datos_empleados)


def reporte_asistencias(datos_empleados: dict) -> None:
    """
    Se genera una tabla con las asistencias historicas de los empleados.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """

    datos_para_la_tabla = []
    headers = ["id", "nombre", "fecha de alta", "total de asistencias"]
    for empleado in datos_empleados.get("empleados", []):
        datos_para_la_tabla.append(
            {
                "id": empleado["id"],
                "nombre": empleado["nombre"],
                "fecha_alta": empleado["fecha_de_alta"],
                "asistencias": len(empleado["asistencias"]),
            }
        )
    if datos_para_la_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, "ASISTENCIAS")
    else:
        print("No hay empleados registrados.")
    input("Enter para continuar...")


def reporte_sueldos(datos_empleados: dict)->None:
    """
    Se visualizan todos los sueldos.

    Pre: Recibe un diccionario como parámetro.
    Post: No retorna nada.
    """
    mas_bajo = (float("inf"), "sin nombre")
    mas_alto = (0, "sin nombre")
    total = 0
    cant = 0
    datos_para_tabla = []
    headers = ["id", "nombre", "sueldo"]
    for empleado in datos_empleados.get("empleados", []):
        datos_para_tabla.append(
            {
                "id": empleado["id"],
                "nombre": empleado["nombre"],
                "sueldo": empleado["sueldo"],
            }
        )
        total += empleado["sueldo"]
        cant += 1
        if empleado["sueldo"] < mas_bajo[0]:
            mas_bajo = (empleado["sueldo"], empleado["nombre"])
        if empleado["sueldo"] > mas_alto[0]:
            mas_alto = (empleado["sueldo"], empleado["nombre"])
    if datos_para_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_tabla, "SUELDOS")
        promedio = total // cant if cant else 0
        print(f"El sueldo mas alto es: ${mas_alto[0]} y corresponde a {mas_alto[1]}.")
        print(f"El sueldo mas bajo es: ${mas_bajo[0]} y corresponde a {mas_bajo[1]}")
        print(f"El sueldo promedio es de: ${promedio}")
    else:
        print("No hay empleados registrados.")
    input("Enter para continuar...")