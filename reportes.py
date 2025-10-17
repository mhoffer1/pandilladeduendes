import utilidades as util
from datetime import datetime
datos_ventas = util.cargar_datos_json(util.ARCHIVO_VENTAS)
datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)
def mostrar_reporte_inventario():
    """
    Podes ver el reporte de inventario.
    """
    while True:
        util.limpiar_pantalla()
        opciones_alertas = ("ver alertas","Ver todas las alertas","salir")
        util.opciones("buscar producto",opciones_alertas)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
def mostrar_reporte_venta():
    """
    Ver el reporte de ventas.
    """
    while True:
        util.limpiar_pantalla()
        opciones_venta = ("mostrar ventas por periodo de tiempo","salir")
        
        util.opciones("REPORTES VENTA",opciones_venta)
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        if opcion == "1":
            mostrar_reporte_por_periodo()
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_reporte_por_periodo():
    while True:
        util.limpiar_pantalla()
        opciones_venta = ("reporte diario","reporte semanal","reporte del año","salir")
        util.opciones("REPORTES VENTA",opciones_venta)
        opcion = input("Ingrese  una opcion: ")
        
        if opcion == "1":
            venta_diario()
        elif opcion == "2":
            ventas_mes()
        elif opcion == "3":
            ventas_anio()
        else:
            print("Opcion invalida.")
            input("enter para continuar.")

def venta_diario():
    contador = 0
    hoy = datetime.now().date()
    for venta in datos_ventas["ventas"]:
        fecha_en_str = datetime.strptime(venta["fecha_venta"],"%Y-%m-%d")
        if hoy == fecha_en_str.date():
            contador += 1
            print(f"{contador}- id: {venta["id"]} monto: ${venta["venta"]}")
    if contador == 0:
        print("No se registraron ventas hoy.")
    input("Enter para continuar...")
    

def ventas_mes():
    pass
def ventas_anio():
    pass
def mostrar_reporte_empleados():
    pass
    """
    Ver el reporte de los empleados.
    """
    while True:
        limpiar_pantalla()
        guiones()
        print("    REPORTE DE EMPLEADOS")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
