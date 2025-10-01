from utilidades import *

def menu_ventas():
    "Muestra el menu de Ventas"
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    VENTAS")
 
        print("=" * 50)
        print("1. Registrar venta")
        print("2. Aplicar Descuento/Promocion")
        print("3. Mostrar historial de ventas")
        print("0. Volver al Menu Principal")
        opcion = input("Ingrese una opcion: ")
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


def registrar_ventas(sucursal):
    
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
         
    
def aplicar_descuento(sucursal): 
    
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Aplicar descuento.")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def mostrar_historial_ventas(sucursal):
    "podes ver el historial de ventas y filtrar por dia,mes y año."

    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas")
 
        print("=" * 50)
        print("1. Ver historial de ventas del dia")
        print("2. Ver historial de ventas de la semana")
        print("3. Ver historial de ventas del mes")
        print("0. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            historial_por_dia(sucursal)
        elif opcion == "2":
            historial_por_semana(sucursal)
        elif opcion == "3":
            historial_por_mes(sucursal)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def historial_por_dia(sucursal):
    "ves el historial de ventas diario."
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Dias")
 
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")

def historial_por_semana(sucursal):
    "ves el historial de ventas semanal."
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Semana")
 
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")
        
        
def historial_por_mes(sucursal):
    "ves el historial de ventas mensual."
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Mostrar historial de Ventas Por Mes.")
 
        print("=" * 50)
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            