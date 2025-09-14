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
            mostrar_productos()
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
    """Agregar un nuevo producto al inventario"""
    limpiar_pantalla()
    print("=" * 50)
    print("    Agregar Nuevo Producto")
    print("=" * 50)
    
    # Cargar datos actuales
    datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
    
    # Solicitar detalles del producto
    nombre = input("Nombre del Producto: ").strip().lower()
    if not nombre:
        print("El nombre del producto no puede estar vacio.")
        input("Presione Enter para continuar...")
        return
    
    descripcion = input("Descripcion: ").strip()
    categoria = input("Categoria: ").strip()
    
    precio = validar_numero("Precio: $", valor_min=0)
    costo = validar_numero("Costo: $", valor_min=0)
    stock = validar_entero("Stock Inicial: ", valor_min=0)
    min_stock = validar_entero("Stock Minimo: ", valor_min=0)
    
    proveedor = input("Proveedor: ").strip()
    sucursal = input("Sucursal: ").strip()
    
    # Crear diccionario del producto
    producto = {
        "id": datos_inventario["prox_id"],
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "precio": precio,
        "costo": costo,
        "stock": stock,
        "min_stock": min_stock,
        "proveedor": proveedor,
        "sucursal": sucursal,
        "fecha_creacion": timestamp_actual(),
        "fecha_actualizacion": timestamp_actual()
    }
    
    # Agregar producto al inventario
    datos_inventario["productos"].append(producto)
    datos_inventario["prox_id"] += 1
    
    # guardar cambios
    if guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario):
        print(f"\nProducto '{nombre}' agregado exitosamente. Con ID: {producto['id']}")
    else:
        print("\nError al guardar el producto.")
    
    input("presione Enter para continuar...")

def mostrar_productos():
    """Mostrar todos los productos en el inventario"""
    limpiar_pantalla()
    print("=" * 50)
    print("    PRODUCTOS")
    print("=" * 50)

    datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
    productos = datos_inventario.get("productos", [])
    
    if not productos:
        print("No se encontraron productos en el inventario.")
        input("Presione Enter para continuar...")
        return

    # definicion de como formatear cada campo    
    mapeo_campos = {
        'id': {'max_largo': 5},
        'nombre': {'max_largo': 25},
        'categoria': {'max_largo': 15},
        'precio': {'formato': 'moneda', 'max_largo': 12},
        'stock': {'max_largo': 8},
        'min_stock': {'max_largo': 10},
        'fecha_creacion': {'formato': 'fecha', 'max_largo': 10}
    }
    
    headers = ['ID', 'Nombre', 'Categoria', 'Precio', 'Stock', 'Min Stock', 'Creacion']
    tabla_datos = formatear_tabla(productos, mapeo_campos)
    
    mostrar_tabla_pag(tabla_datos, headers, "productos", tamanio_pag=15)

def detalles_producto():
    """Mostrar detalles de un producto especifico"""
    limpiar_pantalla()
    
    print("=" * 50)
    print("   DETALLES DE PRODUCTOS")
    print("=" * 50)
    datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
    productos = datos_inventario.get("productos", [])

    producto_buscado = input("Ingrese el Nombre del producto que quiere buscar: ").strip().lower()
    
    if not producto_buscado:
        print("El nombre del producto no puede estar vacio.")
        input("Presione Enter para continuar...")
        return

    productos_filtrados = [p for p in productos if producto_buscado in p['nombre'].lower()]
    
    if not productos_filtrados:
        print(f"No se encontraron productos con el nombre '{producto_buscado}'.")
        input("Presione Enter para continuar...")
        return

    mapeo_campos = {
        'id': {'max_largo': 5},
        'nombre': {'max_largo': 25},
        'descripcion': {'max_largo': 40},
        'categoria': {'max_largo': 15},
        'precio': {'formato': 'moneda', 'max_largo': 12},
        'costo': {'formato': 'moneda', 'max_largo': 12},
        'stock': {'max_largo': 8},
        'min_stock': {'max_largo': 10},
        'proveedor': {'max_largo': 20},
        'sucursal': {'max_largo': 20},
        'fecha_creacion': {'formato': 'fecha', 'max_largo': 10},
        'fecha_actualizacion': {'formato': 'fecha', 'max_largo': 10}
    }

    headers = ['ID', 'Nombre', 'Descripcion', 'Categoria', 'Precio', 'Costo', 'Stock', 'Min Stock', 'Proveedor', 'Sucursal', 'Creacion', 'Actualizacion']
    tabla_datos = formatear_tabla(productos_filtrados, mapeo_campos)

    mostrar_tabla_pag(tabla_datos, headers, "Detalles del Producto", tamanio_pag=10)

def actualizar_producto():
    """Actualizar la informacion de un producto"""
    limpiar_pantalla()
    
    print("=" * 50)
    print("ACTUALIZAR LISTA PRODUCTOS")
    print("=" * 50)

def borrar_producto():
    """Borrar un producto del inventario"""
    limpiar_pantalla()
    print("=" * 50)
    print("BORRAR PRODUCTO")
    print("=" * 50)

def buscar_producto():
    """Buscar productos por nombre o categoria"""
    limpiar_pantalla()
    
    print("=" * 50)
    print("BUSCAR LISTA PRODUCTOS")
    print("=" * 50)

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    limpiar_pantalla()
    print("=" * 50)
    print("ALERTA STOCK BAJO PRODUCTOS")
    print("=" * 50)

