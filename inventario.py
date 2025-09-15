from utilidades import *

def menu_inventario():
    """Muestra el menu de inventario"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("    INVENTARIO")
        print("=" * 50)
        print("1. Agregar Producto")
        print("2. Ver Todos los Productos")
        print("3. Ver Detalles del Producto")
        print("4. Actualizar Producto")
        print("5. Borrar Producto")
        print("6. Buscar Producto")
        print("7. Mostrar Productos con Bajo Stock")
        print("0. Volver al Menu Principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
             ver_todos_los_productos()
        elif opcion == "3":
            detalles_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            borrar_producto()
        elif opcion == "6":
            buscar_producto()
        elif opcion == "7":
            alerta_stock_bajo()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def agregar_producto():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Agregar Producto")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def ver_todos_los_productos():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Ver todos los productos")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def detalles_producto():
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Detalles de producto")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def actualizar_producto():
    """Actualizar la informacion de un producto"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("ACTUALIZAR LISTA PRODUCTOS")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def borrar_producto():
    """Borrar un producto del inventario"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("BORRAR PRODUCTO")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def buscar_producto():
    """Buscar productos por nombre o categoria"""
    while True:
        limpiar_pantalla()
        
        print("=" * 50)
        print("BUSCAR LISTA PRODUCTOS")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("ALERTA STOCK BAJO PRODUCTOS")
        print("=" * 50)
        opcion = input("Ingrese 0 para salir.")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
