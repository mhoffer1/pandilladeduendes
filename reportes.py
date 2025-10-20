import utilidades as util
from datetime import datetime

datos_ventas = util.cargar_datos_json(util.ARCHIVO_VENTAS)
datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)
datos_empleados = util.cargar_datos_json(util.ARCHIVO_EMPLEADOS)

def mostrar_reporte_inventario():
    """
    Podes ver el reporte de inventario.
    """
    while True:
        util.limpiar_pantalla()
        opciones_alertas = ("ver productos inactivos ","salir")
        util.opciones("buscar producto", opciones_alertas)
        opcion = input("Ingrese una opcion : ")
        if opcion == "0":
            break
        elif opcion == "1":
            ver_inactivos()
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

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
        if opcion == "1":
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
        else:
            print("Opcion invalida.")
            input("enter para continuar.")


def venta_diario():
    contador = 0
    hoy = datetime.now().date()
    monto_total = 0
    for venta in reversed(datos_ventas["ventas"]): #se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")
        if hoy == fecha_en_str.date():
            contador += 1
            print(f"{contador}- id: {venta["id"]} monto: ${venta["venta"]}")
            monto_total += venta["venta"]
        else:
            break
    if contador > 0:
        print(f"El monto total es de ${monto_total}")
    else:
        print("No se registraron ventas hoy.")
    input("Enter para continuar...")


def ventas_mes():
    contador = 0
    monto_total = 0
    mes_y_ano_actual = datetime.now().strftime('%Y-%m')
    for venta in reversed(datos_ventas["ventas"]): #se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")

        if mes_y_ano_actual == fecha_en_str.strftime("%Y-%m"): #de la fecha del json, no se evalua el dia.
            contador += 1
            print(f"{contador}- id: {venta["id"]} monto: ${venta["venta"]}")
            monto_total += venta["venta"]
        else:
            break
    if contador > 0:
        print(f"El monto total es de : ${monto_total}")
    else:
        print("No se registraron ventas hoy.")
    input("Enter para continuar...")


def ventas_anio():
    monto_total = 0
    contador = 0
    mes_y_ano_actual = datetime.now().strftime('%Y')
    for venta in reversed(datos_ventas["ventas"]): #se recorre al reves por que las ventas diarias estan al final.
        fecha_en_str = datetime.strptime(venta["fecha_venta"], "%Y-%m-%d")

        if mes_y_ano_actual == fecha_en_str.strftime("%Y"): #de la fecha del json, no se evalua el dia.
            contador += 1
            print(f"{contador}- id: {venta["id"]} monto: ${venta["venta"]}")
            monto_total += venta["venta"]
        else:
            break
    if contador > 0:
        print(f"El monto total es de ${monto_total}")
    else:
        print("No se registraron ventas hoy.")
    input("Enter para continuar...")



def mostrar_reporte_empleados():
    pass
    """
    Ver el reporte de los empleados.
    """
    while True:
        util.limpiar_pantalla()
        opciones_empleados = ("reporte asistencias","reporte sueldos.","salir")
           
        util.opciones("REPORTES VENTA", opciones_empleados)
        opcion = input("Ingrese  una opcion: ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            reporte_asistencias()
        elif opcion == "2":
            reporte_sueldos()

def reporte_asistencias():
            buscar = input("Ingrese un nombre o id de empleado para buscar:")
            encontrado = False
            for empleado in datos_empleados["empleados"]:
                if buscar == empleado["nombre"] or buscar == empleado["id"]:
                    encontrado = True
                    break
            if encontrado:
                print(f"El empleado {empleado["nombre"]} fue registado el {empleado["fecha_alta"]} y registra un total de {len(empleado["asistencias"])} asistencia/s.")
            else:
                print("No encontrado.")
            input("Enter para contiunar...")
def reporte_sueldos():
    "Se visualizan todos los sueldos. Se hace enfasis en el mas bajo, mas alto y en el promedio"
    mas_bajo = (float("inf"),"sin nombre") #tupla con sueldo y nombre.
    mas_alto = (0,"sin nombre") #tupla con sueldo y nombre
    total = 0 #total de sueldos
    cant = 0 #cant empelados
    for empleado in datos_empleados["empleados"]:
        print(f"El empleado {empleado["nombre"]} ID: {empleado["id"]} cobra: ${empleado["sueldo"]}")
        total += empleado["sueldo"]
        cant += 1
        if empleado["sueldo"] < mas_bajo[0]:
            mas_bajo = (empleado["sueldo"], empleado["nombre"])
        if empleado["sueldo"] > mas_alto[0]:
            mas_alto = (empleado["sueldo"],empleado["nombre"])
    promedio = total // cant #division entera para hacer un aprox, no es relevante los decimales.
    print(f"El sueldo mas alto es: ${mas_alto[0]} y corresponde a {mas_alto[1]}.")
    print(f"El sueldo mas bajo es: ${mas_bajo[0]} y corresponde a {mas_bajo[1]}")
    print(f"El sueldo promedio es de: ${promedio}")
    input("Enter para continuar...")

        