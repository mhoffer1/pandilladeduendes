import json
import os
from datetime import datetime
import sys

## Importar modulos
from inventario import *
from utilidades import *
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
        #print("3. Empleados")
        #print("4. Reportes")
        print("0. Exit")
        print("=" * 50)
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            menu_inventario()
        # elif opcion == "2":
        #     menu_ventas()
        # elif opcion == "4":
        #     menu_empleados()
        # elif opcion == "5":
        #     menu_reportes()
        elif opcion == "0":
            print("Gracias por usar el ERP - Pandilla de Duendes!")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

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
        print("=" * 50)
        
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
