from utilidades import *

datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)

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
    validar_precio = lambda x: x > 50 #el producto mas barato puede costar 100.
    while True:
        limpiar_pantalla()
        opciones_prod = ["Agregar Producto","Salir"] #damos la oportunidad de salir por que es mucho quilombo si te metiste y no queres agregar nada.
        opciones("Añadir productos",opciones_prod)
        
        opcion = input("Ingrese 1 opcion: ")
        if opcion == "0":
            break
        if opcion == "1":
            while True: #hasta que ingresen toda la data bien.
                nombre = input("Ingrese el nombre del producto:")
                precio = int(input("Ingrese el precio:$"))
                if validar_precio :
                    alta_rotacion = input("Es un producto de alta rotacion?(1 si,0 u otra tecla no.)")
                    if alta_rotacion == 1:
                        producto = {
                                   "id"   : datos_inventario["prox_id"],
                                  "nombre": nombre,
                                  "precio": precio,
                                  "alta_rotacion": "si"
                                  }
                    else:
                         producto = {
                                  "nombre": nombre,
                                  "precio": precio,
                                  "alta_rotacion": "no"
                                  }
                    datos_inventario["prox_id"] += 1
                    datos_inventario["productos"].append(producto)
                    guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                    print("Se agrego la sucursal correctamente.")
                    input("Presione Enter para continuar...")
                    break
                print("precio invalido.")

        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
def ver_todos_los_productos():
    while True:
        limpiar_pantalla()
        guiones()
        print("ver productos")
        guiones()
        for producto in datos_inventario["productos"]:
            print(f"{producto['nombre']}, ${producto['precio']}")


        input("Presione espacio para continuar.")
        break
        
    
        
      

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
