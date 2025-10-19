import utilidades as util
from datetime import datetime

datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)

def menu_inventario():
    """Muestra el menu de inventario"""
    while True:
        util.limpiar_pantalla()
        opciones_inv = ("Agregar Producto", "Ver Todos los Productos", "Ver Detalles del Producto", "Actualizar Producto", "Cambiar Estado Producto", "Buscar Producto", "Mostrar Productos con Bajo Stock", "Volver al Menú Principal")
        util.opciones("INVENTARIO", opciones_inv)

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
            estado_producto()
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
    #SIRVE PARA EVITAR UN BUG_ CON EL PRIMER PRODUCTO CARGADO.
    if "productos" not in datos_inventario: 
        datos_inventario["productos"] = []
    if "prox_id" not in datos_inventario:
        datos_inventario["prox_id"] = 1

    while True:
        util.limpiar_pantalla()
        opciones_prod = ("Agregar Producto","Salir") #damos la oportunidad de salir por que es mucho quilombo si te metiste y no queres agregar nada.
        util.opciones("Añadir productos",opciones_prod)
        
        opcion = input("Ingrese una opcion: ")
        if opcion == "0":
            break
            
        if opcion == "1":
            while True: #hasta que ingresen toda la data bien.
                nombre = input("Ingrese el nombre del producto: ")
                
                costo = input("Ingrese el costo:$ ")
                try:
                    costo = float(costo)
                except:
                    print("Costo invalido.")
                    input("Enter para continuar...")
                    continue

                precio = input("Ingrese el precio de venta:$ ")
                try:
                    precio = float(precio)
                except:
                    print("Precio invalido.")
                    input("Enter para continuar...")
                    continue

                while True:
                    stock = input("Ingrese el stock:")
                    try:
                        stock = int(stock)
                        break
                    except:  
                        print("Ingrese un numero entero.")
                        
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
                                "ultima_modificacion": str(datetime.now().date()),
                                "activo": True
                                }
                    datos_inventario["productos"].append(producto) #al value del key productos apendea producto
                    datos_inventario["prox_id"] += 1
                    util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
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
        util.limpiar_pantalla()
        util.guiones()
        print("Productos en inventario")
        util.guiones()
        print("No hay productos cargados.")
        input("Presione Enter para continuar...")
        return

    headers = ["ID", "Nombre", "Precio", "Costo", "Stock", "Categoria", "Alta Rotacion", "Fecha Alta", "Ultima Modificacion"]
    util.imprimir_tabla_x_paginas(headers, productos, "Productos en Inventario")

def detalles_producto():
    while True:
        util.limpiar_pantalla()
        util.guiones()
        print("DETALLES DE PRODUCTO")
        util.guiones()

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
                if producto["activo"] == True:
                    print("El estado del producto es ACTIVO")
                else:
                    print("El estado del producto es INACTIVO.")
                encontrado = True
                break
        
        input("Presione Enter para continuar...")
        
        if not encontrado:
            print("Producto no encontrado.")
        

def actualizar_producto():
    while True:
        util.limpiar_pantalla()
        producto_a_editar = input("Ingrese el ID / nombre del producto o 0 para salir: ")
        producto_a_editar = producto_a_editar.strip().lower()
        if producto_a_editar == "0":
            break
        
        producto_encontrado = next(
            (
                producto
                for producto in datos_inventario["productos"]
                if producto["id"] == producto_a_editar or producto["nombre"] == producto_a_editar
            ),
            None,
        )
        if not producto_encontrado:
            print("El producto no existe.")
            input("enter para continuar")
            continue

        util.limpiar_pantalla()
        
        # menu personalizado con valores actuales del producto
        util.guiones()
        print(f"    ACTUALIZANDO PRODUCTO ID:{producto_encontrado['id']} / {producto_encontrado['nombre'].upper()}")
        util.guiones()
        print(f"1- Precio: ${producto_encontrado['precio']}")
        print(f"2- Nombre: {producto_encontrado['nombre'].capitalize()}")
        print(f"3- Costo: ${producto_encontrado['costo']}")
        print(f"4- Stock: {producto_encontrado['stock']}")
        print(f"5- Categoria: {producto_encontrado['categoria'].capitalize()}")
        alta_rot_texto = "Si" if producto_encontrado['alta_rotacion'] == "si" else "No"
        print(f"6- Alta Rotacion: {alta_rot_texto}")
        print("0- Salir")
        util.guiones()

        opcion = input("Ingrese que desea actualizar: ")
        if opcion == "1":
            nuevo_precio = input("Ingrese un nuevo precio: ")
            try:
                nuevo_precio = int(nuevo_precio)
            except Exception as e:
                nuevo_precio = float(nuevo_precio)
            producto_encontrado["precio"] = nuevo_precio

        elif opcion == "2":
            nuevo_nombre = input("Ingrese el nombre que desea modificar: ") 
            producto_encontrado["nombre"] = nuevo_nombre.lower()

        elif opcion == "3":
            nuevo_costo = input("Ingrese el nuevo costo: ")
            try:
                nuevo_costo = int(nuevo_costo)
            except Exception as e:
                nuevo_costo = float(nuevo_costo)

            producto_encontrado["costo"] = nuevo_costo

        elif opcion == "4":
            nuevo_stock = input("Ingrese el nuevo stock: ")
            try:
                nuevo_stock = int(nuevo_stock)
            except Exception as e:
                print("Debe ingresar un numero entero.")
                break
            producto_encontrado["stock"] = nuevo_stock

        elif opcion == "5":
            nueva_categoria = input("Ingrese la nueva categoria: ")
            producto_encontrado["categoria"] = nueva_categoria.lower()

        elif opcion == "6":
            alta_rotacion = input("Ingrese 1 si es de alta rotacion, 0 u otra cosa sino.")
            if alta_rotacion == "1":
                producto_encontrado["alta_rotacion"] = "si"
            else:
                producto_encontrado["alta_rotacion"] = "no"

        elif opcion == "0":
            break
        else:  
            print("Opcion invalida.")
            break

        # actualiza la fecha de modificacion del producto
        producto_encontrado["ultima_modificacion"] = str(datetime.now().date())
        
        util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
        print("Producto actualizado y guardado correctamente.")
        input("Presione enter.")
        break

def estado_producto():
    """Cambia el estado del producto activo o no activo."""
    while True:
        util.limpiar_pantalla()
        opciones_borrar = ("Cambiar estado", "volver atrás")
        util.opciones("borrar producto", opciones_borrar)
        op = input("Ingrese una opción: ")
        
        if op == "0":
            break

        elif op == "1":
            util.limpiar_pantalla()
            util.guiones()
            print("CAMBIAR ESTADO")
            util.guiones()

            a_borrar = input("Ingrese el nombre del producto que desea habilitar o deshabilitar: ").lower().strip()
            for producto in datos_inventario["productos"]:
                if producto["nombre"] == a_borrar:
                    if producto["activo"]:
                        print("El estado actual del producto es ACTIVO")
                    else:
                        print("El estado actual del producto es INACTIVO.")
                    confirmacion = input(f"\n¿Está usted seguro de querer cambiar el estado de  '{producto["nombre"]}'? (1- Sí, 0 u otra cosa- No): ")
                    if confirmacion == "1":
                        if producto["activo"] == True:
                            producto["activo"] = False
                        else:
                            producto["activo"] = True
                    else:
                        input("enter para continuar...")

                        util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
                        print("\nEstado cambiado con exito.")
                        input("Presione Enter para continuar...")
                        break
                    break
            
            else:
                print("Producto no encontrado.")
                input("Presione Enter para continuar...")
                
                
def buscar_producto():
    """Buscar productos por nombre, categoría, precio, stock o alta rotación"""
    opciones_prod = ["buscar producto","salir"]
    while True:
        util.limpiar_pantalla()
        util.opciones("buscar producto",opciones_prod)
        opcion = input("Ingrese una opcion:")
        if opcion == "0":
            break
        elif opcion == "1":
            util.limpiar_pantalla()
            if not datos_inventario["productos"]:
                print("No se encontraron productos cargados.")
                input("Presione Enter para continuar...")
                break

            while True:
                util.limpiar_pantalla()
                opciones_de_busqueda = ("Nombre", "Categoría", "Precio", "Stock", "Alta Rotación", "Volver Atrás")
                util.opciones("buscar producto", opciones_de_busqueda)

                op = input("Ingrese por cuál característica desea buscar: ")
                if op == "0":
                    break

                util.limpiar_pantalla()
                if op == "1":
                    util.guiones()
                    print("BÚSQUEDA POR NOMBRE")
                    util.guiones()
                    a_buscar = input("Ingrese el nombre a buscar: ").lower().strip()
                    coincidencias = [producto for producto in datos_inventario["productos"] if a_buscar in producto["nombre"]]
                
                elif op == "2":
                    util.guiones()
                    print("BÚSQUEDA POR CATEGORÍA")
                    util.guiones()
                    a_buscar = input("Ingrese la categoría a buscar: ").lower().strip()
                    coincidencias = [producto for producto in datos_inventario["productos"] if a_buscar in producto["categoria"]]
                
                elif op == "3":
                    util.guiones()
                    print("BÚSQUEDA POR PRECIO")
                    util.guiones()
                    print("A continuación ingrese el rango de precios que desea buscar...\n")

                    precio_min = util.pedir_float("precio mínimo")
                    precio_max = util.pedir_float("precio máximo", precio_min)
                    coincidencias = [producto for producto in datos_inventario["productos"] if producto["precio"] >= precio_min and producto["precio"] <= precio_max]
                
                elif op == "4":
                    util.guiones()
                    print("BÚSQUEDA POR STOCK")
                    util.guiones()
                    print("A continuación ingrese el rango de valores de stock que desea buscar...\n")

                    stock_min = util.pedir_entero("stock mínimo")
                    stock_max = util.pedir_entero("stock máximo", stock_min)
                    coincidencias = [producto for producto in datos_inventario["productos"] if producto["stock"] >= stock_min and producto["stock"] <= stock_max]
                
                elif op == "5":
                    util.guiones()
                    print("BÚSQUEDA POR ROTACIÓN")
                    util.guiones()
                    a_buscar = input("Ingrese el valor de rotación del producto (1- Alta Rotación, 0 u otra cosa- Baja Rotación): ").strip()
                    a_buscar = "si" if a_buscar == "1" else "no"
                    coincidencias = [producto for producto in datos_inventario["productos"] if producto["alta_rotacion"] == a_buscar]
                
                if not coincidencias:
                        print("No se encontraron productos con esas características.")
                        input("Presione Enter para continuar...")
                        continue
                
                headers = ["ID", "Nombre", "Precio", "Costo", "Stock", "Categoria", "Alta Rotacion", "Fecha Alta", "Ultima Modificacion"]
                util.imprimir_tabla_x_paginas(headers, coincidencias, "Resultados de Búsqueda")
                         

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    while True:
        util.limpiar_pantalla()
        opciones_alertas = ("Ver alertas de Alta rotacion","Ver todas las alertas","salir")
        util.opciones("buscar producto",opciones_alertas)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        elif opcion == "1":
            encontrados = False
            contador = 1
            for producto in datos_inventario["productos"]:
                if producto["alta_rotacion"] == "si" and producto["stock"] <= 20 and producto["activo"] == True:
                    
                    print(f"{contador}.{producto['nombre'].capitalize()}")
                    contador += 1
                    encontrados = True
            if encontrados :
                input("enter para continuar...")
            else:
                print("No se encontraron productos.")
                input("enter para continuar...")
        
        elif opcion == "2":
            encontrados = False
            enumerador = 1
            for producto in datos_inventario["productos"]:
                if  producto["stock"] <= 20 and producto["activo"] == True:
                    print(f"{enumerador}.{producto['nombre'].capitalize()}")
                    enumerador += 1
                    encontrados = True
            if encontrados :
                input("enter para continuar...")
            else:
                print("No se encontraron productos.")
                input("enter para continuar...")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")