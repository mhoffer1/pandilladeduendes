## Importar modulos
from inventario import *
from utilidades import *
from reportes import *
from ventas import *
from proveedores import *
from empleados import * 
from sucursales import *


# Menu principal
def elegir_kiosco():

    datos_sucursales = cargar_datos_json(ARCHIVO_SUCURSALES)
    
    if not datos_sucursales.get("sucursales"):
        print("No se encontraron sucursales. Ingrese una a continuacion...")
        nombre = input("Nombre de la sucursal: ").strip()
        direccion = input("Direccion de la sucursal: ").strip()
        sucursal = {
            "id": datos_sucursales["prox_id"],
            "nombre": nombre,
            "direccion": direccion
        }
        datos_sucursales["prox_id"] += 1
        datos_sucursales["sucursales"].append(sucursal)
        
        guardar_datos_json(ARCHIVO_SUCURSALES, datos_sucursales)
        print("Se agrego la sucursal correctamente.")

    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(" Seleccionar sucursal")
        print("=" * 50)
        for sucursal in datos_sucursales["sucursales"]:
            print(f"{sucursal['id']}. {sucursal['nombre']}")
        print("0. Salir")

        opcion = input("Seleccione una sucursal: ").strip()
        
        if opcion == "0":
            print("Saliendo del sistema...")
            break
        
        if not opcion.isdigit():
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue
        
        opcion = int(opcion)

        sucursal_seleccionada = None
        for s in datos_sucursales["sucursales"]:
            if s["id"] == opcion:
                sucursal_seleccionada = s
                break
        
        if sucursal_seleccionada:
            print(f"Sucursal seleccionada: {sucursal_seleccionada['nombre']}")
            input("Presione Enter para continuar...")
            return sucursal
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def main_menu():
    """Muestra el menu principal y maneja la entrada del usuario"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(f"  ERP - Pandilla de Duendes - Sucursal: {sucursal['id']}/{sucursal['nombre']}")
        print("=" * 50)
        print("1. Inventario")
        print("2. Ventas")
        print("3. Empleados")
        print("4. Proveedores")
        print("5. Reportes")
        print("6. Sucursales")
        print("0. Atras")
        print("=" * 50)
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            menu_inventario(sucursal)
        elif opcion == "2":
            menu_ventas(sucursal)
        elif opcion == "3":
            menu_empleados(sucursal)
        elif opcion == "4":
            menu_proveedores(sucursal)
        elif opcion == "5":
            menu_reportes(sucursal)
        elif opcion == "6":
            menu_sucursales(sucursal)
        elif opcion == "0":
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
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        print("1. Reporte de Inventario")
        print("2. Reporte de Ventas")
        print("3. Reporte de Empleados")
        print("0. Volver al menu principal")
        
        opcion = input("Select an option: ").strip()
        
        if opcion == "1":
            mostrar_reporte_inventario(sucursal)
        elif opcion == "2":
            mostrar_reporte_venta(sucursal)
        elif opcion == "3":
            mostrar_reporte_empleados(sucursal)
        elif opcion == "0":
            break
        else:
            print("opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

   
if __name__ == "__main__":
    # Inicializa los .json e invoca elegir kiosco
    incializar_datos()
    
    sucursal = elegir_kiosco() #se almacena kiosco en una variable global.
    #se invoca el menu principal.
    main_menu() 
