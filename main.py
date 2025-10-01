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
        print("=" * 50)
        print(f"  ERP - Pandilla de Duendes")
        print("=" * 50)
        print("1. Inventario")
        print("2. Ventas")
        print("3. Empleados")
        print("4. Proveedores")
        print("5. Reportes")
        print("0. Atras")
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
            return False
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
        print("Gracias por usar ERP---Pandilla de Duendes!")
        
            
