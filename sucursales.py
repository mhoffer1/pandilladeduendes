from utilidades import *

datos_sucursales = cargar_datos_json(ARCHIVO_SUCURSALES)

def menu_sucursales():
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
            agregar_sucursales()
        elif opcion == "2":
            editar_sucursales()
        elif opcion == "3":
            eliminar_sucursales()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def editar_sucursales():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Editar Sucursales.")
        print("=" * 50)
        mostrar_sucursales()
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def eliminar_sucursales():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Eliminar sucursales.")
        print("=" * 50)
        mostrar_sucursales()
        print()
        nombre = input("Nombre de la sucursal: ").strip()
        input("Presione Enter para continuar...")
        break
        
def agregar_sucursales():
     while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Agregar sucursales")
        print("=" * 50)
        mostrar_sucursales()
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
        input("Presione Enter para continuar...")
        break

def mostrar_sucursales():
    
        print("=" * 50)
        print("Sucursales disponibles")
        print("=" * 50)
        for sucursal in datos_sucursales["sucursales"]:
            print(f"ID: {sucursal['id']}, Nombre: {sucursal['nombre']}, Direccion: {sucursal['direccion']}")
        print("=" * 50)
       