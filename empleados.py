from utilidades import *

def menu_empleados(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    EMPLEADOS")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        print("1. Registrar empleado")
        print("2. Editar datos de empleado.")
        print("3. Registrar asistencia.")
        print("4. Asignar roles a empleados.")
        print("5. Reportes por desempeño.")
        print("6. Dar de alta o baja un empleado.")
        print("0. Volver al Menu Principal")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
                registrar_empleados(sucursales)
        elif opcion == "2":
                editar_datos_de_empleados(sucursales)
        elif opcion == "3":
                registrar_asistencia(sucursales)
        elif opcion == "4":
                asignar_roles(sucursales)
        elif opcion == "5":
                generar_reportes_desempeño(sucursales)
        elif opcion == "6":
                dar_de_alta_o_baja(sucursales)
        elif opcion == "0":
                break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")

def registrar_empleados(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Registrar un nuevo empleado.")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def editar_datos_de_empleados(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Editar Datos de empleados.")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def registrar_asistencia(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Registrar asistencia.")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            
def generar_reportes_desempeño(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Reportes de Desempeño.")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def asignar_roles(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Asignar roles")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def dar_de_alta_o_baja(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Registrar y dar de Baja Empleados")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 1. Para dar de alta, 2. Para dar de baja, 0. Para retroceder: ")
        if opcion == "0":
            break
        elif opcion == "1":
            dar_de_alta(sucursales)
        elif opcion == "2":
            dar_de_baja(sucursales)
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
        
def dar_de_alta(sucursales):
     while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Dar de alta")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def dar_de_baja(sucursales):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Dar de baja")
        print(f"usted esta trabajando en {sucursales['nombre']}")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
           break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
    