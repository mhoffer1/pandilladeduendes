from utilidades import *
from datetime import datetime

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
    #validar_precio = lambda x: x > 50 # el producto mas barato puede costar 100.
    while True:
        limpiar_pantalla()
        opciones_prod = ["Agregar Producto","Salir"] #damos la oportunidad de salir por que es mucho quilombo si te metiste y no queres agregar nada.
        opciones("Añadir productos",opciones_prod)
        
        opcion = input("Ingrese 1 opcion: ")
        if opcion == "0":
            break

        if opcion == "1":
            while True: #hasta que ingresen toda la data bien.
                nombre = input("Ingrese el nombre del producto: ")
                costo = int(input("Ingrese el costo:$ "))
                precio = int(input("Ingrese el precio de venta:$ "))
                stock = int(input("Ingrese el stock inicial: "))
                categoria = input("Ingrese la categoria del producto: ")

                if precio > costo and precio > 50 and stock > 0: #el precio tiene que ser mayor al costo y mayor a 50
                    alta_rotacion = input("Es un producto de alta rotacion? (1 si, 0 u otra tecla no.)")
                    if alta_rotacion == "1":
                        alta_rotacion = "si"
                    else:
                        alta_rotacion = "no"

                    producto = {
                                "id"   : str(datos_inventario["prox_id"]),
                                "nombre": nombre.lower(),
                                "costo" : costo,
                                "precio": precio,
                                "stock": stock,
                                "alta_rotacion": alta_rotacion,
                                "categoria": categoria.lower(),
                                "fecha_alta": str(datetime.now().date()),
                                "ultima_modificacion": str(datetime.now().date())
                                }
                    datos_inventario["prox_id"] += 1
                    datos_inventario["productos"].append(producto)
                    guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                    print("Se agrego el producto correctamente.")
                    input("Presione Enter para continuar...")
                    break
                print("precio invalido.")

        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def ver_todos_los_productos():
    productos = datos_inventario["productos"]
    if not productos:
        limpiar_pantalla()
        guiones()
        print("Productos en inventario")
        guiones()
        print("No hay productos cargados.")
        input("Presione Enter para continuar...")
        return

    por_pagina = 10
    total = len(productos)
    total_paginas = (total + por_pagina - 1) // por_pagina
    pagina = 0

    while True:
        limpiar_pantalla()
        guiones()
        print(f"Productos en inventario (Pagina {pagina + 1} de {total_paginas})")
        guiones()

        inicio = pagina * por_pagina
        fin = min(inicio + por_pagina, total)

        headers = ["ID", "Nombre", "Precio", "Costo", "Stock", "Categoria", "Alta Rotacion", "Fecha Alta", "Ultima Modificacion"]
        data = [
            [
                producto["id"],
                producto["nombre"].capitalize(),
                producto["precio"],
                producto["costo"],
                producto["stock"],
                producto["categoria"].capitalize(),
                "Si" if producto["alta_rotacion"] == "1" else "No",
                producto["fecha_alta"],
                producto["ultima_modificacion"],
            ]
            for producto in productos[inicio:fin]
        ]

        print(tabulate(data, headers, tablefmt="grid"))
        
        print("\nOpciones: [N] siguiente, [P] anterior, [0] volver")
        opcion = input("Seleccione una opcion: ").strip().lower()

        if opcion == "0":
            return
        if opcion == "n":
            if pagina < total_paginas - 1:
                pagina += 1
            else:
                input("Es la ultima pagina. Presione Enter para continuar...")
        elif opcion == "p":
            if pagina > 0:
                pagina -= 1
            else:
                input("Es la primera pagina. Presione Enter para continuar...")
        else:
            input("Opcion invalida. Presione Enter para continuar...")
        break

def detalles_producto():
    while True:
        limpiar_pantalla()
        guiones()
        print("DETALLES DE PRODUCTO")
        guiones()
        
        #buscar por id o nombre
        opcion = input("Ingrese el ID / nombre del producto o 0 para salir: ")
        opcion = opcion.strip().lower()
        if opcion == "0":
            break
        
        encontrado = False
        for producto in datos_inventario["productos"]:
            if producto["id"] == opcion or producto["nombre"] == opcion:
                print("Detalles del producto:")
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre'].capitalize()}")
                print(f"Precio: {producto['precio']}")
                print(f"Costo: {producto['costo']}")
                print(f"Stock: {producto['stock']}")
                print(f"Categoria: {producto['categoria'].capitalize()}")
                print(f"Alta Rotacion: {'Si' if producto['alta_rotacion'] == '1' else 'No'}")
                print(f"Fecha Alta: {producto['fecha_alta']}")
                print(f"Ultima Modificacion: {producto['ultima_modificacion']}")
                encontrado = True
                break
        
        if not encontrado:
            print("Producto no encontrado.")
        
        input("Presione Enter para continuar...")

def actualizar_producto():
    opciones_prod = ["precio","nombre","costo","stock","categoria","alta rotacion","salir"]
    while True:
        limpiar_pantalla()
        producto_a_editar = input("Ingrese el nombre del producto:").lower()
        opciones("Actualizar producto",opciones_prod)
    
        for producto in datos_inventario["productos"]:
            if producto["nombre"] == producto_a_editar:
                producto_a_editar = producto
                break
        else:
            print("El producto no existe.")
            input("enter para continuar")
            break

        opcion = input("Ingrese que desea actualizar:")
        if opcion == "1":
            nuevo_precio = input("Ingrese un nuevo precio:")
            try:
                nuevo_precio = int(nuevo_precio)
            except Exception as e:
                nuevo_precio = float(nuevo_precio)
            producto_a_editar["precio"] = nuevo_precio #se modifica la linea, en caso de no existir python crearia este key y value.

        elif opcion == "2":
            nuevo_nombre = input("Ingrese el nombre que desea modificar:") 
            producto_a_editar["nombre"] = nuevo_nombre

        elif opcion == "3":
            nuevo_costo = input("Ingrese el nuevo costo:")
            try:
                nuevo_costo = int(nuevo_costo)
            except Exception as e:
                nuevo_costo = float(nuevo_costo)

            producto_a_editar["costo"] = nuevo_costo

        elif opcion == "4":
            nuevo_stock = input("Ingrese el nuevo stock:")
            try:
                nuevo_stock = int(nuevo_stock)
            except Exception as e:
                print("Debe ingresar un numero entero.")
            producto_a_editar["stock"] = nuevo_stock

        elif opcion == "5":
            nueva_categoria = input("Ingrese la nueva categoria:")
            producto_a_editar["categoria"] = nueva_categoria

        elif opcion == "6":
            alta_rotacion = input("Ingrese 1 si es de alta rotacion, 0 u otra cosa sino.")
            if alta_rotacion == "1":
                producto_a_editar["alta_rotacion"] = "si"
            else:
                producto_a_editar["alta rotacion"] = "no"

        elif opcion == "0":
            break
        else:  
            print("Opcion invalida.")
            break

        guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario) #modificamos datos inventario!
        print("Precio actualizado y guardado correctamente.")
        input("Presione enter.")
        break




        

def borrar_producto():
    pass
    """Borrar un producto del inventario"""
   # while True:
        #limpiar_pantalla()
        #guiones()
        #print("BORRAR PRODUCTO")
        #guiones()
       # prod = input("Ingrese el nombre del producto que desea eliminar:")
        #for producto in datos_inventario["productos"]:
            #if producto["nombre"] == prod:
               # datos_inventario.pop(producto["nombre"])
                
                
        


def buscar_producto():
    """Buscar productos por nombre o categoria"""
    opciones_prod = ["buscar producto","salir"]
    while True:
        limpiar_pantalla()
        opciones("Actualizar producto",opciones_prod)
        opcion = input("Ingrese una opcion:")
        if opcion == "0":
            break
        elif opcion == "1":
            producto_buscar = input("Ingrese el nombre del producto a buscar:").lower()
            for producto in datos_inventario["productos"]:
                if producto["nombre"] == producto_buscar:
                    producto_buscar = producto 
                    break
                else:
                    print("Producto no encontrado.")
                    input("ingrese enter para continuar")
                    return #para cortar la funcion.
            print(
                f"""
                Producto encontrado:
                - Id: {producto_buscar["id"]}
                - Stock: {producto_buscar["stock"]}
                - Costo: {producto_buscar["costo"]}
                - Precio de venta: {producto_buscar["precio"]}
                -Categoria: {producto_buscar["categoria"]}
                - Ultima modificacion: {producto_buscar["ultima_modificacion"]}
                - Fecha de alta: {producto_buscar["fecha_alta"]}
                        """)

            input("enter para continuar.")

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
