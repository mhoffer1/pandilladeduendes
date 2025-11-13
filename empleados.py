import utilidades as util
from datetime import datetime


def menu_empleados(datos_empleados: dict):
    """Muestra el menu de empleados"""
    while True:
        util.limpiar_pantalla()
        opciones_empl = (
            "Registrar Nuevo Empleado",
            "Editar Datos de Empleado",
            "Registrar Asistencia",
            "Asignar Roles a Empleados",
            "Dar de Baja o Alta a un Empleado",
            "Mostrar empleados",
            "Volver al Menú Principal",
        )
        util.opciones("EMPLEADOS", opciones_empl)

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_empleados(datos_empleados)
        elif opcion == "2":
            editar_datos_de_empleados(datos_empleados)
        elif opcion == "3":
            registrar_asistencia(datos_empleados)
        elif opcion == "4":
            asignar_roles(datos_empleados)
        elif opcion == "5":
            dar_de_baja_alta(datos_empleados)
        elif opcion == "6":
            mostrar_empleados(datos_empleados)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_empleados(datos_empleados: dict):
    """
    Permite registrar empleados al usuario.

    Pre: No recibe nada como parámetro
    Post: No retorna nada, agrega un diccionario al JSON
    """
    datos_empleados.setdefault("empleados", []) 
    datos_empleados.setdefault("prox_id", 1)
    #si no existe, se asigna un valor por defecto, soluciona bugs fatales de primera
    #ejecucion.
    while True:
        opcion = util.ingresar("registrar empleados")
        if opcion == "0":
            break
        if opcion == "1":
            sueldo_invalido = True
            while True:
                if sueldo_invalido == False:
                    break
                nombre = input("Nombre completo: ")
                puesto = input("Puesto: ")
                while sueldo_invalido:
                    try:
                        sueldo = util.pedir_entero("Sueldo")
                    except ValueError:
                        print("El sueldo debe ser un numero entero.")
                        input("Presione enter para continuar...")
                        continue
                    if sueldo > 50000:
                        sueldo_invalido = False
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
                        util.guardar_datos_json(util.ARCHIVO_EMPLEADOS, datos_empleados)
                        print("Empleado agregado correctamente.")
                        input("Presione Enter para continuar...")
                        break
                    print("El sueldo debe ser mayor a $50000.")
        else:
            util.limpiar_pantalla()
            util.imprimir_titulo("registrar empleados")
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def editar_datos_de_empleados(datos_empleados: dict):
    """
    Permite editar un atributo de un empleado al usuario.
    Pre: No recibe nada como parámetro.
    Post: No retorna nada, modifica un atributo del JSON.
    """
    while True:
        op = util.ingresar("editar empleados")
        if op == "1":
            indice, empleado = util.seleccionar_item(
                datos_empleados.get("empleados", []),
                "empleado",
                "EDITAR EMPLEADO",
            )
            if empleado is None:
                continue

            print("Que dato desea cambiar: ")
            claves = list(empleado.keys())
            for i, clave in enumerate(claves, start=1): #indice y key.
                print(f"{i}- {clave.capitalize().replace('_', ' ')}") #reemplaza _ por espacio.
            dato = input("Ingrese el dato que desea cambiar: ")
            
            for i, clave in enumerate(claves, start=1):
                if dato.lower() == clave.lower() or (dato.isdigit() and int(dato) == i): #osea si es igual a clave o a la opcion.
                    if clave in ("fecha_de_alta", "id"): #TESTEAR SI FUNCIONA BIEN
                        print("Ese dato no se puede cambiar.")
                        input("Ingrese enter para salir.")
                        return
                    if clave == "asistencias":
                        #print("Para eso entrar al modulo registrar asistencias.")
                        registrar_asistencia(datos_empleados)
                        return
                    if clave == "estado":
                        print(f"El estado actual es {empleado[clave]}")
                        op_estado = input(
                            "Ingrese 1 para cambiar, 0 u otro para retroceder:"
                        )
                        if op_estado == "1":
                            empleado[clave] = (
                                "Inactivo" if empleado[clave] == "Activo" else "Activo"
                            )
                            util.guardar_datos_json(
                                util.ARCHIVO_EMPLEADOS, datos_empleados
                            )
                            print("Cambio realizado con exito.")
                        input("enter para continuar...")
                        return

                    nuevo_dato = input(
                        f"Ingrese el nuevo valor para '{clave}': "
                    )
                    empleado[clave] = nuevo_dato
                    util.guardar_datos_json(
                        util.ARCHIVO_EMPLEADOS, datos_empleados
                    )
                    print(f"{clave} modificado correctamente.")
                    input("Ingrese enter para salir.")
                    return

            print("No existe ese dato.")
            input("Enter")
        elif op == "0":
            input("Ingrese enter para salir.")
            break
        else:
            print("Opcion incorrecta.")


def asignar_roles(datos_empleados: dict):
    """
    Permite al usuario asignarle un rol a un empleado.

    Pre: No recibe nada como parámetro.
    Post: No retorna nada, agrega un rol de atributo.
    """
    while True:
        opcion = util.ingresar("asignar roles")
        if opcion == "0":
            break
        elif opcion == "1":
            indice, empleado = util.seleccionar_item(
                datos_empleados.get("empleados", []), #si no existe empleados, se pasa lista vacia para evitar errores.
                "empleado",
                "asignar roles",
            )
            if empleado:
                rol = input(
                    f"Ingrese el rol para el empleado {empleado['nombre']}: " #seleccionas empleado en seleccionar item
                )
                empleado["rol"] = rol
                util.guardar_datos_json(util.ARCHIVO_EMPLEADOS, datos_empleados)
                print("Rol actualizado correctamente.")
            else:
                print("No se encontro ese empleado.")
            input("Ingrese enter para salir.")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_asistencia(datos_empleados: dict):
    """
    Permite al usuario registrar asistencias de los empleados.

    Pre: No recibe nada como parámetro.
    Post: No retorna nada, registra una fecha con horario en una lista.
    """
    while True:
        opcion = util.ingresar("registrar asistencia")
        if opcion == "0":
            break
        elif opcion == "1":
            indice, empleado = util.seleccionar_item(
                datos_empleados.get("empleados", []),
                "empleado",
                "registrar asistencia",
            )
            if empleado:
                if validar_estado(datos_empleados, indice):
                    empleado["asistencias"].append(
                        datetime.now().strftime("%Y-%m-%d %H:%M")
                    )
                    util.guardar_datos_json(
                        util.ARCHIVO_EMPLEADOS, datos_empleados
                    )
                    print("Asistencia registrada correctamente")
                else:
                    print("Este empleado esta inactivo.")
            else:
                print("No se encontro ese empleado.")
            input("Presione Enter para salir.")
            return
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")


def dar_de_baja_alta(datos_empleados: dict):
    """
    Permite al usuario dar de baja o de alta a un empleado.

    Pre: No recibe nada como parámetro.
    Post: No retorna nada, cambia el estado de un empleado.
    """
    while True:
        opcion = util.ingresar("dar de baja o de alta")
        if opcion == "0":
            break
        elif opcion == "1":
            indice, empleado = util.seleccionar_item(
                datos_empleados.get("empleados", []),
                "empleado",
                "dar de baja o de alta",
            )
            if empleado:
                while True:
                    op = input("Ingrese 1 para dar de baja, 2 para dar de alta: ")
                    if op == "1":
                        if validar_estado(datos_empleados, indice):
                            datos_empleados["empleados"][indice]["estado"] = "Inactivo"
                            break
                        else:
                            print(
                                f"El empleado {datos_empleados['empleados'][indice]['nombre']} ya está inactivo"
                            )
                    elif op == "2":
                        if not validar_estado(datos_empleados, indice):
                            datos_empleados["empleados"][indice]["estado"] = "Activo"
                            break
                        else:
                            print(
                                f"El empleado {datos_empleados['empleados'][indice]['nombre']} ya está activo"
                            )
                    else:
                        print("Opcion incorrecta.")
                        input("Ingrese enter para continuar...")
            if empleado:
                util.guardar_datos_json(util.ARCHIVO_EMPLEADOS, datos_empleados)
                print("Estado de empleado modificado correctamente.")
            else:
                print("No se encontro ese empleado.")
            input("Presione Enter para salir.")
            return
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")


def mostrar_empleados(datos_empleados: dict):
    """
    Permite al usuario visualizar los empleados.

    Pre: No recibe nada como parámetro.
    Post: No retorna nada, imprime una tabla con lo empleados.
    """
    while True:
        util.limpiar_pantalla()
        util.imprimir_titulo("mostrar empleados")
        if not datos_empleados.get("empleados"):
            print("No hay empleados registrados.")
            input("Presione Enter para volver...")
            break
        else:
            empleado_cual = input(
                "\nIngrese 1 para continuar (o 0 para volver): "
            )
            util.limpiar_pantalla()
            if empleado_cual == "0":
                break
            headers = list(datos_empleados["empleados"][0].keys()) #usamos los keys de empleados sub0 por que siempre son iguales, no hace falta recorrer otros.
            util.imprimir_tabla_x_paginas(
                [header.capitalize() for header in headers],
                datos_empleados["empleados"],
                "Datos del empleado",
            )
            input("\nPresione Enter para continuar...")


def validar_estado(data: dict, indice: int) -> bool:
    """
    Valida el estado. No es opcion del menu, se utiliza en otras funciones.

    Pre: Recibe un diccionario y un entero.
    Post: Retorna un booleano.
    """
    return data["empleados"][indice]["estado"] == "Activo"