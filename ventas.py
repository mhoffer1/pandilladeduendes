from utilidades import *

def menu_ventas():
    "Muestra el menu de Ventas"
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" Ventas")
        print("=" * 50)
        print("1.Registrar venta")
        print("2.Aplicar Descuento/Promocion")
        print("3.Mostrar historial de ventas")
        print("0.Salir")
        opcion = input("Ingrese una opcion:")
        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            aplicar_descuento()
        elif opcion == "3":
            mostrar_historial_ventas()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_ventas():
    
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Reporte De Ventas")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
         
    
def aplicar_descuento(): 
    
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Aplicar descuento.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_historial_ventas():
    

    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas")
        print("=" * 50)
        print("1. Ver historial de ventas del dia")
        print("2. Ver historial de ventas de la semana")
        print("3. Ver historial de ventas del mes")
        print("0. Salir")
        opcion = input("Ingrese una opcion:")
        if opcion == "1":
            historial_por_dia()
        elif opcion == "2":
            historial_por_semana()
        elif opcion == "3":
            historial_por_mes()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def historial_por_dia():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Dias")
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder.")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")

def historial_por_semana():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Semana")
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder.")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")
        
        
def historial_por_mes():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Mes.")
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            