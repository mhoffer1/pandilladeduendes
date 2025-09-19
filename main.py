## Importar modulos
from inventario import menu_inventario
from utilidades import limpiar_pantalla, guardar_datos_json, cargar_datos_json, incializar_datos, ARCHIVO_SUCURSALES
from reportes import *
from ventas import menu_ventas
from proveedores import menu_proveedores
from empleados import menu_empleados
from sucursales import menu_sucursales


# Menu principal
def elegir_kiosco():
    """En caso de no haber datos en sucursales.json, te obliga a generar una(primer inicio
    por cliente). Despues se muestra en pantalla las sucursales y por ultimo se selecciona
    una, la cual se retorna."""

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
    #ACA ARRANCA EL PROGRAMA A PARTIR DEL SEGUNDO USO!!!
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
        
        opcion = int(opcion) #casteo para comparar con ["id"]!

        sucursal_seleccionada = None
        for s in datos_sucursales["sucursales"]:
            if s["id"] == opcion:
                sucursal_seleccionada = s
                break
        
        if sucursal_seleccionada:
            print(f"Sucursal seleccionada: {sucursal_seleccionada['nombre']}")
            input("Presione Enter para continuar...")
            return sucursal_seleccionada
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
     #SI llega aca retorna None y no se ejecuta main_menu.

def main_menu():
    """Muestra el menu principal una vez que elegiste sucursal."""
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
    

def menu_reportes(sucursal):
    """Muestra el menu de reportes"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    REPORTES")
        print(f"usted esta trabajando en --{sucursal['nombre']}")
        print("=" * 50)
        print("1. Reporte de Inventario")
        print("2. Reporte de Ventas")
        print("3. Reporte de Empleados")
        print("0. Volver al menu principal")
        
        opcion = input("Seleccione una opcion: ").strip()
        
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
    while True:
        # Inicializa los .json(utilidades.py) 
        incializar_datos()
        sucursal = elegir_kiosco()
        if sucursal: #si no es false,osea no ingresan salir del programa.
        #se invoca el menu principal.
            main_menu() 
        else:
            break
            
