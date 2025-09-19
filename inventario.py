from utilidades import limpiar_pantalla

def menu_inventario(sucursal):
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
            agregar_producto(sucursal)
        elif opcion == "2":
             ver_todos_los_productos(sucursal)
        elif opcion == "3":
            detalles_producto(sucursal)
        elif opcion == "4":
            actualizar_producto(sucursal)
        elif opcion == "5":
            borrar_producto(sucursal)
        elif opcion == "6":
            buscar_producto(sucursal)
        elif opcion == "7":
            alerta_stock_bajo(sucursal)
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def agregar_producto(sucursal):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Agregar Producto")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def ver_todos_los_productos(sucursal):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Ver todos los productos")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def detalles_producto(sucursal):
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("Detalles de producto")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def actualizar_producto(sucursal):
    """Actualizar la informacion de un producto"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("ACTUALIZAR LISTA PRODUCTOS")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def borrar_producto(sucursal):
    """Borrar un producto del inventario"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("BORRAR PRODUCTO")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def buscar_producto(sucursal):
    """Buscar productos por nombre o categoria"""
    while True:
        limpiar_pantalla()
        
        print("=" * 50)
        print("BUSCAR LISTA PRODUCTOS")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def alerta_stock_bajo(sucursal):
    """Mostrar productos con stock por debajo del nivel minimo"""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("ALERTA STOCK BAJO PRODUCTOS")
 
        print("=" * 50)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
