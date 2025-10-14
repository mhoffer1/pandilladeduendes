import utilidades as util
from datetime import datetime

datos_inventario = util.cargar_datos_json(util.ARCHIVO_INVENTARIO)

def menu_inventario():
    """Muestra el menu de inventario"""
    while True:
        util.limpiar_pantalla()
        opciones_inv = ("Agregar Producto", "Ver Todos los Productos", "Ver Detalles del Producto", "Actualizar Producto", "Borrar Producto", "Buscar Producto", "Mostrar Productos con Bajo Stock", "Volver al Menú Principal")
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
                                "ultima_modificacion": str(datetime.now().date())
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

    por_pagina = 10
    total = len(productos)
    total_paginas = (total + por_pagina - 1) // por_pagina
    pagina = 0

    while True:
        util.limpiar_pantalla()
        util.guiones()
        print(f"Productos en inventario (Pagina {pagina + 1} de {total_paginas})")
        util.guiones()

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
                "Si" if producto["alta_rotacion"] == "si" else "No",
                producto["fecha_alta"],
                producto["ultima_modificacion"],
            ]
            for producto in productos[inicio:fin]
        ]

        print(util.tabulate(data, headers, tablefmt="grid"))
        
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

def borrar_producto():
    """Borrar un producto del inventario"""
    while True:
        util.limpiar_pantalla()
        opciones_borrar = ("borrar un producto", "volver atrás")
        util.opciones("borrar producto", opciones_borrar)
        op = input("Ingrese una opción: ")
        
        if op == "0":
            break

        elif op == "1":
            util.limpiar_pantalla()
            util.guiones()
            print("BORRAR PRODUCTO")
            util.guiones()

            a_borrar = input("Ingrese el nombre del producto que desea eliminar: ").lower().strip()
            for producto in datos_inventario["productos"]:
                if producto["nombre"] == a_borrar:
                    confirmacion = input(f"\n¿Está usted seguro de querer borrar el producto '{producto["nombre"]}'? (1- Sí, 0 u otra cosa- No): ")
                    if confirmacion == "1":
                        datos_inventario["productos"].remove(producto)

                        util.guardar_datos_json(util.ARCHIVO_INVENTARIO, datos_inventario)
                        datos_inventario["prox_id"] -= 1
                        print("\nProducto eliminado con éxito.")
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
                
                por_pagina = 10
                total = len(coincidencias)
                total_paginas = (total + por_pagina - 1) // por_pagina
                pagina = 0

                while True:
                    util.limpiar_pantalla()
                    util.guiones()
                    print(f"Resultados de Búsqueda (Pagina {pagina + 1} de {total_paginas})")
                    util.guiones()

                    inicio = pagina * por_pagina
                    fin = min(inicio + por_pagina, total)

                    headers = ["ID", "Nombre", "Precio", "Costo", "Stock", "Categoria", "Alta Rotacion", "Fecha Alta", "Ultima Modificacion"]
                    data = [
                        [
                            coincide["id"],
                            coincide["nombre"].capitalize(),
                            coincide["precio"],
                            coincide["costo"],
                            coincide["stock"],
                            coincide["categoria"].capitalize(),
                            "Si" if coincide["alta_rotacion"] == "si" else "No",
                            coincide["fecha_alta"],
                            coincide["ultima_modificacion"],
                        ]
                        for coincide in coincidencias[inicio:fin]
                    ]

                    util.imprimir_tabla(headers, data)
                    
                    print("\nOpciones: [N] siguiente, [P] anterior, [0] volver")
                    opcion = input("Seleccione una opcion: ").strip().lower()

                    if opcion == "0":
                        break
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
                        continue
                         

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    while True:
        util.limpiar_pantalla()
        opciones_alertas = ["Ver alertas de Alta rotacion","Ver todas las alertas","salir"]
        util.opciones("buscar producto",opciones_alertas)
        opcion = input("Ingrese 0 para salir: ")
        if opcion == "0":
            break
        elif opcion == "1":
            encontrados = False
            contador = 1
            for producto in datos_inventario["productos"]:
                if producto["alta_rotacion"] == "si" and producto["stock"] <= 20:
                    
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
                if  producto["stock"] <= 20:
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