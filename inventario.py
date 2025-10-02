from utilidades import limpiar_pantalla, guiones, opciones

def menu_inventario():
    """Muestra el menu de inventario"""
    while True:
        limpiar_pantalla()
        opciones_inv = ("Agregar Producto", "Ver Todos los Productos", "Ver Detalles del Producto", "Actualizar Producto", "Borrar Producto", "Buscar Producto", "Mostrar Productos con Bajo Stock", "Volver al Menú Principal")
        opciones("INVENTARIO", opciones_inv)
        
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
        guiones()
        print("AGREGAR PRODUCTO")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def ver_todos_los_productos():
    while True:
        limpiar_pantalla()
        guiones()
        print("VER TODOS LOS PRODUCTOS")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def detalles_producto():
    while True:
        limpiar_pantalla()
        guiones()
        print("DETALLES DE PRODUCTO")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def actualizar_producto():
    """Actualizar la informacion de un producto"""
    while True:
        limpiar_pantalla()
        guiones()
        print("ACTUALIZAR LISTA PRODUCTOS")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def borrar_producto():
    """Borrar un producto del inventario"""
    while True:
        limpiar_pantalla()
        guiones()
        print("BORRAR PRODUCTO")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def buscar_producto():
    """Buscar productos por nombre o categoria"""
    while True:
        limpiar_pantalla()
        guiones()
        print("BUSCAR LISTA PRODUCTOS")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    while True:
        limpiar_pantalla()
        guiones()
        print("ALERTA STOCK BAJO PRODUCTOS")
        guiones()
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
