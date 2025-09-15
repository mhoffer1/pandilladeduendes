from utilidades import *

def menu_empleados():
    limpiar_pantalla()
    print("=" * 50)
    print(" Ventas")
    print("=" * 50)
    print("1.Registrar empleado")
    print("2.Editar datos de empleado.")
    print("3.Registrar asistencia.")
    print("4.Asignar roles a empleados.")
    print("5.Reportes por desempeño.")
    print("6.Dar de alta o baja un empleado.")
    print("0.Exit")
    while True:
        opcion = input("Ingrese una opcion:")
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
            dar_de_alta_o_baja()
        elif opcion == "0":
            break

def registrar_empleados():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Registrar un nuevo empleado.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def editar_datos_de_empleados():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Editar Datos de empleados.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def registrar_asistencia():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Registrar asistencia.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def generar_reportes_desempeño():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Reportes de Desempeño.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break

def asignar_roles():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Asignar roles")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break

def dar_de_alta_o_baja():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Registrar y dar de BajaEmpleados")
        print("=" * 50)
        opcion = input("Ingrese 1.para dar de alta, 2.Para dar de baja, 0.Para retroceder:")
        if opcion == "0":
            break
        elif opcion == "1":
            dar_de_alta()
        elif opcion == "2":
            dar_de_baja()
        
def dar_de_alta():
     limpiar_pantalla()
     while True:
        print("=" * 50)
        print("Dar de alta")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder.")
        if opcion == "0":
            break

def dar_de_baja():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Dar de baja")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder.")
        if opcion == "0":
           break
    