from utilidades import *

datos_sucursales = cargar_datos_json(ARCHIVO_SUCURSALES) #archivos de las sucursales.

def menu_sucursales(sucursal):
     """
     Podes acceder a todas las funciones de las sucursales!
     """
     while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    SUCURSALES")
        print("=" * 50)
        print("1. Agregar Sucursales.")
        print("2. Editar Sucursales.")
        print("3. Eliminar Sucursales.")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "0":
            break
        elif opcion == "1":
            agregar_sucursales(sucursal)
        elif opcion == "2":
            editar_sucursales(sucursal)
        elif opcion == "3":
            eliminar_sucursales(sucursal)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def editar_sucursales(sucursal):
    """
    Permite editar informacion de sucursales ya creadas.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Editar Sucursales.")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        mostrar_sucursales(sucursal)
        print("0. Retroceder")
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def eliminar_sucursales(sucursal):
    """
    Te muestra las sucursales y te dice cual queres eliminar.
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Eliminar sucursales.")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        mostrar_sucursales(sucursal)
        print()
        nombre = input("Nombre de la sucursal: ").strip()
        input("Presione Enter para continuar...")
        break
        
def agregar_sucursales(sucursal):
     """
     Sirve para agregar sucursales, tambien se ven las ya creadas.
     """
     while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Agregar sucursales")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        mostrar_sucursales(sucursal)
        nombre = input("Nombre de la sucursal: ").strip()
        direccion = input("Direccion de la sucursal: ").strip()
        sucursal = {
                "id": datos_sucursales["prox_id"],
                "nombre": nombre,
                "direccion": direccion
            }
        datos_sucursales["prox_id"] += 1
        datos_sucursales["sucursales"].append(sucursal)
            
        guardar_datos_json(ARCHIVO_SUCURSALES, datos_sucursales) #el archivo y lo que queres almacenar.
        print("Se agrego la sucursal correctamente.")
        input("Presione Enter para continuar...")
        break

def mostrar_sucursales(sucursal):
        """
        Sirve para ver las sucursales, en el resto de funciones de este menu tambien se
        puede visualizar por una cuestion practica a la hora de editar y agregar y evitar
        repeticiones accidentales.
        """
    
        print("=" * 50)
        print("Sucursales disponibles")
        print(f"usted esta trabajando en {sucursal['nombre']}")
        print("=" * 50)
        for sucursal in datos_sucursales["sucursales"]:
            print(f"ID: {sucursal['id']}, Nombre: {sucursal['nombre']}, Direccion: {sucursal['direccion']}")
        print("=" * 50)
       