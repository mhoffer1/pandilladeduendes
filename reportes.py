import utilidades as util
from datetime import datetime

datos_ventas = util.cargar_datos_json(util.ARCHIVO_VENTAS)
datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)
datos_empleados = util.cargar_datos_json(util.ARCHIVO_EMPLEADOS)


# ---------------------------------REPORTE INVENTARIO--------------------------
def mostrar_reporte_inventario():
    """
    Podes ver el reporte de inventario.
    """
    while True:
        util.limpiar_pantalla()
        opciones_alertas = (
            "ver productos inactivos",
            "Ver valor total del inventario",
            "salir",
        )
        util.opciones("buscar producto", opciones_alertas)
        opcion = input("Ingrese una opcion : ")
        if opcion == "0":
            break
        elif opcion == "1":
            ver_inactivos()
        elif opcion == "2":
            ver_valor_del_inventario()
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def ver_valor_del_inventario():
    print(
        "NOTA: Para calcular el valor total de su inventario se considera el precio que usted pago, es decir, el COSTO de los productos."
    )
    total_AR, total_NOAR = 0, 0  # totales de alta rotacion y de no alta rotacion.

    for producto in datos_inventario["productos"]:
        if producto["alta_rotacion"] == "si":
            total_AR += producto["costo"] * producto["stock"]
        else:
            total_NOAR += producto["costo"] * producto["stock"]
    print(f"El valor total de su inventario es de: ${total_AR + total_NOAR}")
    print(f"${total_AR} son de productos de alta rotacion.")
    print(f"${total_NOAR} son de productos que NO son de alta rotacion.")
    input("Enter para continuar...")


def ver_inactivos():
    """
    parte de reportes de inventario, se ven los productos inactivos.
    """
    contador = 0
    for producto in datos_inventario["productos"]:
        if producto["activo"] == False:
            contador += 1
            print(f"{contador}.producto:{producto["nombre"]}. ID:{producto["id"]}")
    input("enter para continuar...")


# ------------------------------REPORTE VENTAS----------------------------------
def mostrar_reporte_venta():
    """
    Ver el reporte de ventas.
    """
    while True:
        util.limpiar_pantalla()
        opciones_venta = ("mostrar ventas por periodo de tiempo", "salir")

        util.opciones("REPORTES VENTA", opciones_venta)
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        elif opcion == "1":
            mostrar_reporte_por_periodo()
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def mostrar_reporte_por_periodo():
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
            venta_diario()
        elif opcion == "2":
            ventas_mes()
        elif opcion == "3":
            ventas_anio()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
            input("enter para continuar.")


def venta_diario():
    datos_para_la_tabla = []
    contador = 0
    hoy = datetime.now().date()
    headers = ["id","venta","fecha_venta"]
    monto_total = 0
    for venta in reversed(
        datos_ventas["ventas"]
    ):  # se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")
        if hoy == fecha_en_str.date():
            datos_para_la_tabla.append(
            {
                "id": venta["id"],
                "monto": venta["venta"],
                "fecha_venta": venta["fecha_venta"]
            }
            )
        else:
            break
    if datos_para_la_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, "VENTAS DIARIAS")
        print(f"El monto total es de ${monto_total}")
    else:
        print("No se registraron ventas hoy.")
    input("Enter para continuar...")


def ventas_mes():
    
    
    monto_total = 0
    datos_para_la_tabla = []
    headers = ["id","venta","fecha_venta"]
    mes_y_ano_actual = datetime.now().strftime("%Y-%m")
    for venta in reversed(
        datos_ventas["ventas"]
    ):  # se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")

        if mes_y_ano_actual == fecha_en_str.strftime("%Y-%m"):  # de la fecha del json, no se evalua el dia.
            datos_para_la_tabla.append(
            {
                "id": venta["id"],
                "monto": venta["venta"],
                "fecha_venta": venta["fecha_venta"]
            }
            )
        else:
            break
    if datos_para_la_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, "VENTAS MENSUALES")
        print(f"El monto total es de : ${monto_total}")
    else:
        print("No se registraron ventas este mes.")
    input("Enter para continuar...")


def ventas_anio():
    datos_para_la_tabla = []
    monto_total = 0
    headers = ["id","venta","fecha_venta"]
    mes_y_anio_actual = datetime.now().strftime("%Y")
    for venta in reversed(
        datos_ventas["ventas"]
    ):  # se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")

        if mes_y_anio_actual == fecha_en_str.strftime("%Y"):  # de la fecha del json, no se evalua el dia.
            datos_para_la_tabla.append(
            {
                "id": venta["id"],
                "monto": venta["venta"],
                "fecha_venta": venta["fecha_venta"]
            }
            )
        else:
            break
    if datos_para_la_tabla:
        util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, "VENTAS ANUALES")
        print(f"El monto total es de ${monto_total}")

    else:
        print("No se registraron ventas este año.")
    input("Enter para continuar...")


# -----------------------------------REPORTES EMPLEADOS-------------------------
def mostrar_reporte_empleados() -> None:
    """
    Ver el reporte de los empleados.
    """
    while True:
        
        util.limpiar_pantalla()
        opciones_empleados = ("reporte asistencias", "reporte sueldos.", "salir")

        util.opciones("REPORTES VENTA", opciones_empleados)
        opcion = input("Ingrese  una opcion: ")

        if opcion == "0":
            break
        elif opcion == "1":
            reporte_asistencias()
        elif opcion == "2":
            reporte_sueldos()


def reporte_asistencias() -> None:
    """
    Se genera una tabla con las asistencias historicas de los empleados.
    """

    datos_para_la_tabla = []
    headers = ["id", "nombre", "fecha de alta", "total de asistencias"]
    for empleado in datos_empleados["empleados"]:
        datos_para_la_tabla.append(
            {
                "id": empleado["id"],
                "nombre": empleado["nombre"],
                "fecha_alta": empleado["fecha_de_alta"],
                "asistencias": len(empleado["asistencias"])
            }
        )
    util.imprimir_tabla_x_paginas(headers, datos_para_la_tabla, "ASISTENCIAS")


def reporte_sueldos():
    "Se visualizan todos los sueldos. Se hace enfasis en el mas bajo, mas alto y en el promedio"
    mas_bajo = (float("inf"), "sin nombre")  # tupla con sueldo y nombre.
    mas_alto = (0, "sin nombre")  # tupla con sueldo y nombre
    total = 0  # total de sueldos
    cant = 0  # cant empelados
    datos_para_tabla = []
    headers = ["id", "nombre", "sueldo"]
    for empleado in datos_empleados["empleados"]:
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
    util.imprimir_tabla_x_paginas(headers, datos_para_tabla, "SUELDOS")
    promedio = (
        total // cant
    )  # division entera para hacer un aprox, no es relevante los decimales.
    print(f"El sueldo mas alto es: ${mas_alto[0]} y corresponde a {mas_alto[1]}.")
    print(f"El sueldo mas bajo es: ${mas_bajo[0]} y corresponde a {mas_bajo[1]}")
    print(f"El sueldo promedio es de: ${promedio}")
    input("Enter para continuar...")
