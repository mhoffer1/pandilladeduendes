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
    nombre = input("Nombre del Producto: ").strip().upper()
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
    
    encontrado = False
    print("=" * 50)
    print("   DETALLES DE PRODUCTOS")
    print("=" * 50)
    datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
    productos = datos_inventario.get("productos", [])

    producto_buscado = input("Ingrese el Nombre del producto que quiere 2buscar:")
    producto_buscado = producto_buscado.strip().upper()
    for producto in productos:
        if producto["nombre"] == producto_buscado:
            encontrado = True
            break
    if encontrado:
        print(f"ID: {producto["id"]}")
        print(f"Nombre: {producto["nombre"]}")
        print(f"Descripcion {producto["descripcion"]}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Costo: ${producto['costo']}")
        print(f"Stock: {producto['stock']}")
        print(f"Stock mínimo: {producto['min_stock']}")
        print(f"Proveedor: {producto['proveedor']}")
        print(f"Sucursal: {producto['sucursal']}")
        print(f"Fecha de creación: {producto['fecha_creacion']}")
        print(f"Última actualización: {producto['fecha_actualizacion']}")
    else:
        print("producto no encontrado")




def actualizar_producto():
    """Actualizar la informacion de un producto"""
    pass

def borrar_producto():
    """Borrar un producto del inventario"""
    pass

def buscar_producto():
    """Buscar productos por nombre o categoria"""
    pass

def alerta_stock_bajo():
    """Mostrar productos con stock por debajo del nivel minimo"""
    pass

