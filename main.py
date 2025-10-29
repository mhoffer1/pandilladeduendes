# Importar modulos
from inventario import menu_inventario
import utilidades as util
from reportes import (
    mostrar_reporte_empleados,
    mostrar_reporte_inventario,
    mostrar_reporte_venta,
)
from ventas import menu_ventas
from proveedores import menu_proveedores
from empleados import menu_empleados


def main_menu(
    datos_inventario,
    datos_ventas,
    datos_empleados,
    datos_proveedores,
):
    """Muestra el menu principal una vez que elegiste sucursal."""
    while True:
        util.limpiar_pantalla()
        opciones_main = (
            "Ventas",
            "Inventario",
            "Empleados",
            "Proveedores",
            "Reportes",
            "Salir del programa",
        )
        util.opciones("ERP - Pandilla de Duendes", opciones_main)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            menu_ventas(datos_ventas, datos_inventario, datos_empleados)
        elif opcion == "2":
            menu_inventario(datos_inventario, datos_ventas)
        elif opcion == "3":
            menu_empleados(datos_empleados)
        elif opcion == "4":
            menu_proveedores(datos_proveedores)
        elif opcion == "5":
            menu_reportes(datos_inventario, datos_ventas, datos_empleados)
        elif opcion == "0":
            return False
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def menu_reportes(datos_inventario, datos_ventas, datos_empleados):
    """Muestra el menu de reportes"""
    while True:
        util.limpiar_pantalla()
        opciones_report = (
            "Reporte de Inventario",
            "Reporte de Ventas",
            "Reporte de Empleados",
            "Volver al menu principal",
        )
        util.opciones("REPORTES", opciones_report)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_reporte_inventario(datos_inventario)
        elif opcion == "2":
            mostrar_reporte_venta(datos_ventas, datos_inventario, datos_empleados)
        elif opcion == "3":
            mostrar_reporte_empleados(datos_empleados)
        elif opcion == "0":
            break
        else:
            print("opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":

    # Inicializa los .json(utilidades.py)
    util.incializar_datos()  # primer uso, sino main_menu

    datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)
    datos_ventas = util.cargar_datos_json(util.ARCHIVO_VENTAS)
    datos_empleados = util.cargar_datos_json(util.ARCHIVO_EMPLEADOS)
    datos_proveedores = util.cargar_datos_json(util.ARCHIVO_PROVEEDORES)

    main_menu(datos_inventario, datos_ventas, datos_empleados, datos_proveedores)

    util.limpiar_pantalla()
    util.guiones()
    print("Saliendo del programa...\nGracias por usar ERP - Pandilla de Duendes!")
    util.guiones()
