import json
import os
from datetime import datetime
import sys

## Importar modulos
from inventario import *
from utilidades import *
from reportes import *
from ventas import *
from proveedores import *
from empleados import * 
#from ventas import *
#from empleados import *

def main_menu():
    """Muestra el menu principal y maneja la entrada del usuario"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    ERP - Pandilla de Duendes")
        print("=" * 50)
        print("1. Inventario")
        print("2. Ventas")
        print("3. Empleados")
        print("4. Reportes")
        print("0. Exit")
        print("=" * 50)
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            menu_ventas()
        elif opcion == "3":
            menu_empleados()
        elif opcion == "4":
             menu_proveedores()
        elif opcion == "5":
             menu_reportes()
        elif opcion == "0":
            print("Gracias por usar el ERP - Pandilla de Duendes!")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
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

def menu_proveedores():
    limpiar_pantalla()
    print("=" * 50)
    print(" Ventas")
    print("=" * 50)
    print("1.Registrar Proveedor")
    print("2.Solicitar productos a proveedor.")
    print("3.Ver pagos pendientes")
    print("4.Ver historial de Compra de Cada Proveedor.")
    print("5.Ver proveedor por Nombre.")
    print("0.Salir")
    opcion = input("Ingrese una opcion:")
    while True:
        if opcion == "1":
            registrar_provedores()
        elif opcion == "2":
            solicitar_productos_a_proveedor()
        elif opcion == "3":
            pagos_pendientes()
        elif opcion == "4":
            historial_de_compras_a_cada_proveedor()
        elif opcion == "5":
            buscar_proveedor_por_nombre()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida")

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
            print("Opcion invalida.")



def menu_reportes():
    """Muestra el menu de reportes"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTES")
        print("=" * 50)
        print("1. Reporte de Inventario")
        print("2. Reporte de Ventas")
        print("3. Reporte de Empleados")
        print("0. Volver al menu principal")
        
        opcion = input("Select an option: ").strip()
        
        if opcion == "1":
            mostrar_reporte_inventario()
        elif opcion == "2":
            mostrar_reporte_venta()
        elif opcion == "3":
            mostrar_reporte_empleados()
        elif opcion == "0":
            break
        else:
            print("opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    # Inicia los archivos de datos si no existen
    incializar_datos()
    # Muestra el menu principal
    main_menu()
