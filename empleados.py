from utilidades import *
from datetime import datetime

datos_empleados = cargar_datos_json(ARCHIVO_EMPLEADOS)


def menu_empleados():
    """Muestra el menu de empleados"""
    while True:
        limpiar_pantalla()
        opciones_empl = (
            "Registrar Nuevo Empleado",
            "Editar Datos de Empleado",
            "Registrar Asistencia",
            "Asignar Roles a Empleados",
            "Dar de Baja o Alta a un Empleado",
            "Mostrar empleados",
            "Volver al Menú Principal",
        )
        opciones("EMPLEADOS", opciones_empl)

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_empleados()
        elif opcion == "2":
            editar_datos_de_empleados()
        elif opcion == "3":
            registrar_asistencia()
        elif opcion == "4":
            asignar_roles()
        elif opcion == "5":
            dar_de_baja_alta()
        elif opcion == "6":
            mostrar_empleados()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_empleados():
    while True:
        opcion = ingresar("registrar empleados")
        if opcion == "0":
            break
        if opcion == "1":
            while True:
                nombre = input("Nombre completo: ")
                puesto = input("Puesto: ")
                try:
                    sueldo = int(input("Sueldo: "))
                except ValueError:
                    print("El sueldo debe ser un numero entero.")
                    input("Presione enter para continuar...")
                    continue
                if sueldo > 0:
                    empleado = {
                        "id": str(datos_empleados["prox_id"]),
                        "nombre": nombre.title(),
                        "puesto": puesto.title(),
                        "sueldo": sueldo,
                        "fecha_de_alta": str(datetime.now().date()),
                        "asistencias": [],
                        "estado": "Activo",
                    }
                    datos_empleados["prox_id"] += 1
                    datos_empleados["empleados"].append(empleado)
                    guardar_datos_json(ARCHIVO_EMPLEADOS, datos_empleados)
                    print("Empleado agregado correctamente.")
                    input("Presione Enter para continuar...")
                    break
                print("El sueldo debe ser mayor a 0.")
        else:
            limpiar_pantalla()
            imprimir_titulo("registrar empleados")
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def editar_datos_de_empleados():
    while True:
        op = ingresar("editar empleados")
        if op == "1":
            if datos_empleados["empleados"]:
                listar_empleados()
                cual = input("Ingrese el empleado que desea modificar: ")
                limpiar_pantalla()
                imprimir_titulo("EDITAR EMPLEADO")
                encontrado = False
                for j, empleado1 in enumerate(datos_empleados["empleados"]):
                    if (
                        cual.lower() == empleado1["nombre"].lower()
                        or cual.isdigit()
                        and int(cual) - 1 == j
                    ):
                        encontrado = True
                        print("Qué dato desea cambiar:")
                        for i, clave in enumerate(empleado1):
                            print(f"{i+1}- {clave}")
                        dato = input("Ingrese el dato que desea cambiar: ")
                        encontrado2 = False
                        limpiar_pantalla()
                        imprimir_titulo("EDITAR EMPLEADO")
                        for i, clave in enumerate(empleado1):
                            if dato.lower() == clave.lower() or (
                                dato.isdigit() and int(dato) - 1 == i
                            ):
                                encontrado2 = True
                                if clave == "fecha_alta" or clave == "id":
                                    print("Ese dato no se puede cambiar.")
                                    input("Ingrese enter para salir.")
                                elif clave == "asistencias":
                                    print(
                                        "Para eso entrar al módulo registrar asistencias."
                                    )
                                    input("Ingrese enter para salir.")
                                    return
                                elif clave == "estado":
                                    print(f"El estado actual es {empleado1[clave]}")
                                    op = input("Ingrese 1 para cambiar,0 u otro para retroceder:")
                                    if op == "1":
                                        if empleado1[clave] == "activo":
                                            empleado1[clave] = "inactivo"
                                        else:
                                            empleado1[clave] = "activo"
                                        guardar_datos_json(
                                        ARCHIVO_EMPLEADOS, datos_empleados
                                    )
                                        print("cambio realizado con exito.")
                                        input("enter para continuar...")
                                    else:
                                        input("Enter para continuar...")
                                        break
                                else:
                                    nuevo_dato = input(
                                        f"Ingrese el nuevo valor para '{clave}': "
                                    )
                                    empleado1[clave] = nuevo_dato
                                    guardar_datos_json(
                                        ARCHIVO_EMPLEADOS, datos_empleados
                                    )
                                    print(f"{clave} modificado correctamente.")
                                    input("Ingrese enter para salir.")
                                    return
                        if not encontrado2:
                            print("No existe ese dato.")
                            input("Enter")
                        break

                if not encontrado:
                    print("No existe esa persona en los datos.")
            else:
                print("Los datos están vacíos.")
                break
        elif op == "0":
            input("Ingrese enter para salir.")
            break
        else:
            print("Opcion incorrecta.")


def asignar_roles():
    while True:
        opcion = ingresar("asignar roles")
        if opcion == "0":
            break
        elif opcion == "1":
            j, empleado = seleccionar_empleado("dar de baja o de alta")
            if empleado:
                rol = input(f"Ingrese el rol para el empleado {empleado["nombre"]}")
                empleado["rol"] = rol
                guardar_datos_json(ARCHIVO_EMPLEADOS, datos_empleados)
                print("Rol actualizado correctamente.")
            else:
                print("No se encontro ese empleado.")
            input("Ingrese enter para salir.")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_asistencia():
    while True:
        opcion = ingresar("registrar asistencia")
        if opcion == "0":
            break
        elif opcion == "1":
            j, empleado = seleccionar_empleado("registrar_asistencia")
            if empleado:
                if validar_estado(datos_empleados,j):
                    empleado["asistencias"].append(datetime.now().strftime("%Y-%m-%d %H:%M"))
                else:
                    print("Este empleado esta inactivo.")
                    input("Ingrese enter para salir.")
                    return
            if empleado:
                guardar_datos_json(ARCHIVO_EMPLEADOS, datos_empleados)
                print("Asistencia registrada correctamente")
            if not empleado:
                print("No se encontro ese empleado.")
            input("Presione Enter para salir.")
            return
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")


def dar_de_baja_alta():
    while True:
        opcion = ingresar("dar de baja o de alta")
        if opcion == "0":
            break
        elif opcion == "1":
            j, empleado = seleccionar_empleado("dar de baja o de alta")
            if empleado:
                while True:
                    op = input("Ingrese 1 para dar de baja, 2 para dar de alta: ")
                    if op == "1":
                        if validar_estado(datos_empleados,j):
                            datos_empleados["empleados"][j]["estado"] = "Inactivo"
                            break
                        else:
                            print(f"El empleado {datos_empleados["empleados"][j]["nombre"]} ya está inactivo")
                    elif op == "2":
                        if not validar_estado(datos_empleados,j):
                            datos_empleados["empleados"][j]["estado"] = "Activo"
                            break
                        else:
                            print(f"El empleado {datos_empleados["empleados"][j]["nombre"]} ya está activo")
                    else:
                        print("Opcion incorrecta.")
                        input("Ingrese enter para continuar...")
            if empleado:
                guardar_datos_json(ARCHIVO_EMPLEADOS, datos_empleados)
                print("Estado de empleado modificado correctamente.")
            if not empleado:
                print("No se encontro ese empleado.")
            input("Presione Enter para salir.")
            return

        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")


def mostrar_empleados():
    while True:
        limpiar_pantalla()
        imprimir_titulo("mostrar empleados")
        if not datos_empleados["empleados"]:
            print("No hay empleados registrados.")
            input("Presione Enter para volver...")
            break
        else:
            empleado_cual = input(
                "\nIngrese 1 para continuar (o 0 para volver): "
            )
            limpiar_pantalla()
            if empleado_cual == "0":
                break
            headers = []
            for clave, valor in datos_empleados["empleados"][0].items():
                headers.append(clave.capitalize())
            imprimir_tabla_x_paginas(headers, datos_empleados["empleados"], "Datos del empleado")
            input("\nPresione Enter para continuar...")

def listar_empleados():
    for i, empleado in enumerate(datos_empleados["empleados"]):
        if empleado["estado"] == "activo":
            print(f"{i+1} - {empleado['nombre']}")

def validar_estado(data,i):
    return data["empleados"][i]["estado"] == "Activo"

def seleccionar_empleado(tarea:str):
    if not datos_empleados["empleados"]:
        print("No hay empleados registrados.")
        input("Presione Enter para volver...")
        return None, None
    listar_empleados()
    asiste = input(
                    "\nIngrese el nombre o número del empleado (o 0 para volver): "
                )
    if asiste == "0":
        return None, None
    limpiar_pantalla()
    imprimir_titulo(tarea)
    for j, empleado1 in enumerate(datos_empleados["empleados"]):
        if (
            asiste.lower() == empleado1["nombre"].lower()
            or asiste.isdigit()
            and int(asiste) - 1 == j
        ):
            return j,empleado1
    print("No existe ese empleado.")
    input("Ingrese enter para salir.")
    return None, None