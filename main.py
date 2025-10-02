## Importar modulos
from inventario import menu_inventario
from utilidades import *
from reportes import *
from ventas import menu_ventas
from proveedores import menu_proveedores
from empleados import menu_empleados

def main_menu():
    """Muestra el menu principal una vez que elegiste sucursal."""
    while True:
        limpiar_pantalla()
        opciones_main = ("Inventario", "Ventas", "Empleados", "Proveedores", "Reportes", "Salir del programa")
        opciones("ERP - Pandilla de Duendes", opciones_main)
        
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
            return False
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
    

def menu_reportes():
    """Muestra el menu de reportes"""
    while True:
        limpiar_pantalla()
        opciones_report = ("Reporte de Inventario", "Reporte de Ventas", "Reporte de Empleados", "Volver al menú principal")
        opciones("REPORTES", opciones_report)
        
        opcion = input("Seleccione una opcion: ").strip()
        
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
    
        # Inicializa los .json(utilidades.py) 
        incializar_datos() #primer uso, sino main_menu
        
        main_menu()
        print("\nGracias por usar ERP - Pandilla de Duendes!")