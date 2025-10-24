from utilidades import *
datos_ventas = cargar_datos_json(ARCHIVO_VENTAS)
datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
from datetime import datetime

def menu_ventas()->None:
    "Muestra el menu de Ventas"
    while True:
        limpiar_pantalla()
        opciones_ventas = ("Registrar Venta","Promociones" ,"Volver al Menú Principal")
        opciones("VENTAS", opciones_ventas)

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            aplicar_promocion()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def impr_factura_venta(datos_venta: dict) -> None:
    """
    Imprime la factura de la venta correspondientes con los datos recibidos.

    Pre: Recibe como parámetro el diccionario con cada elemento de la venta (id, costo, etc.).
    Post: No retorna nada, imprime en formato apropiado la factura de la venta.
    """
    imprimir_titulo("factura de venta")
    print(f"ID DE VENTA: {formatear_id(datos_venta["id"])}")
    print(f"FECHA DE EMISIÓN: {datos_venta["fecha_venta"]}")
    print()
    for venta_producto in datos_venta["info_venta"]:
        id_producto = formatear_id(venta_producto["id"])
        nombre_producto = venta_producto["nombre"]
        cant_producto = venta_producto["cantidad"]
        costo_producto = venta_producto["costo"]

        cant_nombre_id = f"x{cant_producto} {nombre_producto.title()} - ID:{id_producto}"
        ancho = 45-len(cant_nombre_id)
        print(f"{cant_nombre_id}{costo_producto:.>{ancho}.2f} $")
    
    mensaje_descuento = f"(DESCUENTO: {datos_venta["descuento"]: .2f} %)" if datos_venta["descuento"] else ""
    imprimir_titulo(f"COSTO TOTAL: {datos_venta["venta"]: .2f} $ {mensaje_descuento}")


def registrar_ventas()->None:
    """
    Regista ventas y las almacena en el .json de ventas. El precio de promocion
    tiene prioridad ante el precio comun.
    """  
      
    while True:
        limpiar_pantalla()
        costo_total = 0
        opcion_ventas = ("registrar venta","salir")
        opciones("Registrar Venta",opcion_ventas)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        elif opcion == "1":
            info_venta = [] # Se va llenando a medida que se ingresan los productos y cantidades a vender

            while True:
                prod = input("Ingrese el nombre o ID del producto que quiere vender(0 para terminar venta): ").lower().strip()
                if prod == "0":
                    descuento_a_realizar = 0.0
                    hay_descuento = input("Desea aplicar descuento? (1.si 0.no): ")
                    if hay_descuento == "1":
                        descuento_a_realizar = pedir_float("el descuento que desea realizar", 98.0) # Máximo 98 % de descuento
                        costo_total = aplicar_descuento(costo_total,descuento_a_realizar)
                    
                    guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                    informacion_venta = {
                                "id"   : str(datos_ventas["prox_id"]),
                                "venta": costo_total,
                                "fecha_venta": str(datetime.now().date()),
                                "info_venta": info_venta,
                                "descuento": descuento_a_realizar
                                }
                    datos_ventas["ventas"].append(informacion_venta)
                    datos_ventas["prox_id"] += 1
                    guardar_datos_json(ARCHIVO_VENTAS,datos_ventas)

                    impr_factura_venta(informacion_venta)
                    input("Enter para continuar...")
                    return

                
                for producto in datos_inventario["productos"]:
                    if producto["nombre"] == prod or producto["id"] == prod and producto["estado"] == "activo":
                        while True:
                            cantidad = pedir_entero(f"cuántas unidades de {producto["nombre"].title()} desea vender")
                            if cantidad > 0:
                                if producto["stock"] >= cantidad:
                                    # SI existe usa el precio de promocion y tiene valor, sino el normal
                                    if "promocion" in producto and producto["promocion"]:
                                        precio_unitario = producto["promocion"] 
                                    else: 
                                        precio_unitario = producto["precio"]
                                    
                                    costo_producto = precio_unitario * cantidad
                                    costo_total += costo_producto
                                    producto["stock"] -= cantidad
                                    print(f"{cantidad} unidad(es) de {producto['nombre'].title()} vendidas.")
                                    
                                    coincidencias = [venta["id"] for venta in info_venta]
                            
                                    if producto["id"] not in coincidencias: # Si es la primera vez que se carga una venta de este producto, se hace un diccionario nuevo con la info
                                        venta_producto = {"id": producto["id"],
                                                        "nombre": producto["nombre"],
                                                        "cantidad": cantidad,
                                                        "costo": costo_producto}
                                        
                                        info_venta.append(venta_producto)
                                    else: # Si ya está cargado en info_ventas, no se hace un nuevo diccionario. Se suma más cantidad y más costo al producto ya registrado
                                        i_coincidencia = coincidencias.index(producto["id"])
                                        info_venta[i_coincidencia]["cantidad"] += cantidad
                                        info_venta[i_coincidencia]["costo"] += costo_producto
                                    
                                    input("Enter para continuar...")
                                    break
                                else:
                                    print("No hay suficiente stock.")
                                    input("Enter para continuar...")
                            else:
                                print("Ingresar un numero positivo.")
                                input("Enter para continuar...")
                        break  

                else:
                    print("Producto no encontrado.")
                    input("Enter para continuar...")

def aplicar_descuento(valor:int,descuento:int)->int:
    """
    se invoca desde "registrar_ventas", realiza un descuento y se valida que sea valido.
    pre:Recibe el valor de la venta y el descuento a realizar.
    post: Retorna el valor neto a cobrar.
    """
    valor_neto = valor * (1 - descuento / 100)
    return valor_neto
            
       
def aplicar_promocion()->None:
    """
    Se aplica una promocion a ciertos productos, tiene prioridad en las ventas ante 
    el precio de lista.
    """
    while True:
        limpiar_pantalla()
        opciones_prod = ("agregar promocion", "ver promocion", "eliminar promocion", "salir")
        opciones("PROMOCIONES",opciones_prod)
        opcion =  input("Ingrese una opcion: ")
        if opcion == "0":
            break
        elif opcion == "1":
            clase = input("Ingrese a que categoria desea hacerle una promocion:")
            encontrado = False
            for producto in datos_inventario["productos"]:
                    if producto["categoria"].strip().lower() == clase.strip().lower():
                        encontrado = True
                        descuento_a_aplicar = input("Ingrese el descuento que desea realizar(en %): ")
                        try:    
                            descuento_a_aplicar = int(descuento_a_aplicar)
                        except Exception as e:
                            print("descuento invalido.") 
                            break
                        else:             
                            descuento = aplicar_descuento(producto["precio"],descuento_a_aplicar)
                            producto["promocion"] = descuento
                            print("Promocion registrada con exito.")
                            guardar_datos_json(ARCHIVO_INVENTARIO,datos_inventario)
                            input("Enter para continuar...")
                            break
            if encontrado == False:
                    print("Producto no encontrado.")
                    input("Enter para continuar...")
        elif opcion == "2":
           
            for producto in datos_inventario["productos"]:
                #for clave, valor in producto.items():
                    if "promocion" in producto and producto["promocion"]: #para que no tome los Null
                        print(f"Hay una promocion en el producto {producto['nombre']} esta a un valor {producto['promocion']} que pertenece a la categoria  {producto['categoria']}")
            input("Enter para continuar...")
            break
        elif opcion == "3":
            a_eliminar = input("Ingrese a que categoria quiere eliminarle su promocion:").strip().lower()
            for producto in datos_inventario["productos"]:
                    if producto["categoria"].strip().lower() == a_eliminar.strip().lower():
                        producto["promocion"] = None
                        guardar_datos_json(ARCHIVO_INVENTARIO,datos_inventario)
                        print("Promocion eliminada con exito.")
                        input("Ingrese enter para continuar.")
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

