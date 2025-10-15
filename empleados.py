from utilidades import limpiar_pantalla, guiones, opciones
from utilidades import *
from datetime import datetime

datos_empleados = cargar_datos_json(ARCHIVO_EMPLEADOS)

def menu_empleados():
    while True:
        limpiar_pantalla()
        opciones_empl = ("Registrar Nuevo Empleado", "Editar Datos de Empleado", "Registrar Asistencia", "Asignar Roles a Empleados", "Reportes por Desempeño", "Dar de Baja a un Empleado", "Mostrar empleados", "Volver al Menú Principal")
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
                generar_reportes_desempeño()
        elif opcion == "6":
                dar_de_baja()
        elif opcion == "7":
                mostrar_empleados()
        elif opcion == "0":
                break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")

def registrar_empleados():
    while True:
        limpiar_pantalla()
        guiones()
        print("REGISTRAR EMPLEADO")
        guiones()
        opcion = input("Ingrese 0 para retroceder y 1 para registrar: ")
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
                        "fecha_alta": str(datetime.now().date()),
                        "asistencias": []
                    }
                    datos_empleados["prox_id"] += 1
                    datos_empleados["empleados"].append(empleado)
                    guardar_datos_json(ARCHIVO_EMPLEADOS, datos_empleados)
                    print("Empleado agregado correctamente.")
                    input("Presione Enter para continuar...")
                    break
                print("El sueldo debe ser mayor a 0.")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def editar_datos_de_empleados():
    while True:
        limpiar_pantalla()
        guiones()
        print("EDITAR EMPLEADO")
        guiones()
        print("Desea cambiar:")
        op = input("Ingrese 1 para entrar 0 para salir: ")
        if op == "1":
            limpiar_pantalla()
            if datos_empleados["empleados"]:
                for i, empleado in enumerate(datos_empleados["empleados"]):
                    print(f"{i+1}- {empleado['nombre']}")
                cual = input("Ingrese el empleado que desea modificar: ")
                limpiar_pantalla()
                encontrado = False 
                for j, empleado1 in enumerate(datos_empleados["empleados"]):
                    if cual.lower() == empleado1["nombre"].lower() or cual.isdigit() and int(cual)-1 == j:
                        encontrado = True
                        print("Qué dato desea cambiar:")
                        for i, clave in enumerate(empleado1):
                            print(f"{i+1}- {clave}")
                        dato = input("Ingrese el dato que desea cambiar: ")
                        encontrado2 = False
                        limpiar_pantalla()
                        for i, clave in enumerate(empleado1):
                            if dato.lower() == clave.lower() or (dato.isdigit() and int(dato)-1 == i):
                                encontrado2 = True
                                if clave == "fecha_alta":
                                    print("Ese dato no se puede cambiar.")
                                    input("Ingrese enter para salir.")
                                    return
                                elif clave == "asistencias":
                                    print("Para eso entrar al módulo registrar asistencias.")
                                    input("Ingrese enter para salir.")
                                    return
                                else:
                                    nuevo_dato = input(f"Ingrese el nuevo valor para '{clave}': ")
                                    empleado1[clave] = nuevo_dato 
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
        limpiar_pantalla()
        guiones()
        print("ASIGNAR ROLES")
        
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            
def generar_reportes_desempeño():
    while True:
        limpiar_pantalla()
        guiones()
        print("REPORTES DE DESEMPEÑO")
      
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def registrar_asistencia():
    while True:
        limpiar_pantalla()
        guiones()
        print("REGISTRAR ASISTENCIA")
        guiones()
        opcion = input("Ingrese 0 para retroceder, 1 para continuar: ")
        if opcion == "0":
            break
        elif opcion == "1":
            if not datos_empleados["empleados"]:
                print("No hay empleados registrados.")
                input("Presione Enter para volver...")
                break
            else:
                for i, empleado in enumerate(datos_empleados["empleados"]):
                    print(f"{i + 1} - {empleado['nombre']}")
                asiste = input("\nIngrese el nombre o número del empleado (o 0 para volver): ")
                encontrado = False
                limpiar_pantalla()
                for j, empleado1 in enumerate(datos_empleados["empleados"]):
                    if asiste.lower() == empleado1["nombre"].lower() or asiste.isdigit() and int(asiste)-1 == j:
                        encontrado = True
                    if encontrado:
                        empleado1["asistencias"].append(str(datetime.now().date()))
                if encontrado:
                    print("Asistencia registrada correctamente")
                if not encontrado:
                    print("No se encontro ese empleado.")
                input("Presione Enter para salir.")
                return
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")

def dar_de_baja():
    while True:
        limpiar_pantalla()
        guiones()
        print("DAR DE BAJA")
        guiones()
        opcion = input("Ingrese 0 para retroceder, 1 para continuar: ")
        limpiar_pantalla()
        if opcion == "0":
            break
        elif opcion == "1":
            if not datos_empleados["empleados"]:
                print("No hay empleados registrados.")
                input("Presione Enter para volver...")
                break
            else:
                for i, empleado in enumerate(datos_empleados["empleados"]):
                    print(f"{i + 1} - {empleado['nombre']}")
                de_baja = input("\nIngrese el nombre o número del empleado (o 0 para volver): ")
                encontrado = False
                limpiar_pantalla()
                for j, empleado1 in enumerate(datos_empleados["empleados"]):
                    if de_baja.lower() == empleado1["nombre"].lower() or de_baja.isdigit() and int(de_baja)-1 == j:
                        encontrado = True
                    if encontrado:
                        del datos_empleados["empleados"][j]
                        print("Empleado dado de baja correctamente.")
                if not encontrado:
                    print("No se encontro ese empleado.")
                input("Presione Enter para salir.")
                return
                    
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para salir...")

def mostrar_empleados():
    while True:
        limpiar_pantalla()
        guiones()
        print("Los empleados son los siguientes.")
        guiones()

        if not datos_empleados["empleados"]:
            print("No hay empleados registrados.")
            input("Presione Enter para volver...")
            break

        for i, empleado in enumerate(datos_empleados["empleados"]):
            print(f"{i + 1} - {empleado['nombre']}")
        empleado_cual = input("\nIngrese el nombre o número del empleado (o 0 para volver): ")
        limpiar_pantalla()
        if empleado_cual == "0":
            break
        encontrado = False
        if empleado_cual.isdigit():
            indice = int(empleado_cual) - 1
            if 0 <= indice < len(datos_empleados["empleados"]):
                empleado1 = datos_empleados["empleados"][indice]
                encontrado = True
        else:
            for empleado1 in datos_empleados["empleados"]:
                if empleado_cual.lower() == empleado1["nombre"].lower():
                    encontrado = True
                    break
        if encontrado:
            print("\nDatos del empleado:")
            for clave, valor in empleado1.items():
                print(f"{clave}: {valor}")
            input("\nPresione Enter para continuar...")
        else:
            print("No se encontró ese empleado.")
            input("Presione Enter para intentarlo de nuevo...")