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
        if datos_empleados["empleados"]:
            for empleado in datos_empleados["empleados"]:
                print(f"-{empleado['nombre']}")
            cual = input("Ingrese el empleado que desea modificar: ")
            encontrado = False
            for empleado1 in datos_empleados["empleados"]:
                if cual == empleado1["nombre"]:
                    encontrado = True
                    print("Qué dato desea cambiar:")
                    for clave, valor in empleado1.items():
                        print(f"El {clave} por ahora es {valor}")
                    dato = input("Ingrese el dato que desea cambiar: ")
                    if dato in empleado1:
                        nuevo_dato = input(f"Ingrese el nuevo {dato}: ")
                        if dato == "sueldo":
                            empleado1[dato] = int(nuevo_dato)
                        else:
                            empleado1[dato] = nuevo_dato
                        print(f"{dato} modificado correctamente.")
                    else:
                        print("No se pudo modificar. No existe ese dato.")
                    break
            
            if not encontrado:
                print("No existe ese nombre en los datos.")
        else:
            print("Los datos están vacíos.")
            break
        # for empleado in datos_empleados["empleados"]:
        #     print(f"El ID: {empleado['id']}")
        #     print(f"El nombre: {empleado['nombre']}")
        #     print(f"El puesto: {empleado['puesto']}")
        #     print(f"El sueldo: {empleado['sueldo']}")
        # opcion = input("Elija una de las opciones. Ingrese 0 para retroceder. ")
        # if opcion == "0":
        #     break
        # if opcion == "1":
        #     if datos_empleados["empleados"]:
        #         for elem in datos_empleados["empleados"]:
        #             print(f"-{elem["nombre"]}")
        #         cual = input("Ingrese el empleado que desea modificar.")
        #         datos_empleados["empleados"][0]["id"] = ("Ingrese el nuevo ID: ")
        # else:
        #     print("Opcion invalida. Intente de nuevo.")
        #     input("Presione Enter para continuar...")

def registrar_asistencia():
    while True:
        limpiar_pantalla()
        guiones()
        print("REGISTRAR ASISTENCIA")
        
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

def dar_de_baja():
    while True:
        limpiar_pantalla()
        guiones()
        print("DAR DE BAJA")
        guiones()
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
           break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_empleados():
    while True:
        limpiar_pantalla()
        guiones()
        print("Los empleados son los siguientes.")
        guiones()
        
        for i, empleado in enumerate(datos_empleados["empleados"]):
            print(f"{i+1}-{empleado['nombre']}")
        
        empleado_cual = input("Ingrese el nombre del empleado del cual desea ver los datos: ")
        encontrado = False
        
        for empleado1 in datos_empleados["empleados"]:
            if empleado_cual.lower() == empleado1["nombre"].lower():
                encontrado = True
                print("\nDatos del empleado:")
                for clave, valor in empleado1.items():
                    print(f"{clave} tiene un valor de {valor}")
                break
        
        if not encontrado:
            print("No se encontró ese empleado.")
        
        opcion = input("\nIngrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")