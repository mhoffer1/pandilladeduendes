from utilidades import limpiar_pantalla, guiones, opciones

def menu_empleados():
    while True:
        limpiar_pantalla()
        opciones_empl = ("Registrar Nuevo Empleado", "Editar Datos de Empleado", "Registrar Asistencia", "Asignar Roles a Empleados", "Reportes por Desempeño", "Dar de Baja a un Empleado", "Volver al Menú Principal")
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
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def editar_datos_de_empleados():
    while True:
        limpiar_pantalla()
        guiones()
        print("EDITAR EMPLEADO")
        
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
    