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


def registrar_ventas()->None:
    """
    Regista ventas y las almacena en el .json de ventas. El precio de promocion
    tiene prioridad ante el precio comun.
    """  
      
    while True:
        limpiar_pantalla()
        costo = 0
        opcion_ventas = ("registar venta","salir")
        opciones("Registrar Venta",opcion_ventas)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        elif opcion == "1":
            while True:
                prod = input("Ingrese el nombre o ID del producto que quiere vender(0 para terminar venta): ")
                if prod == "0":
                    descuento = input("Desea aplicar descuento? (1.si 0.no): ")
                    if descuento == "0":
                        print(f"Debe abonar: {costo}") #cuando se termina de registar la venta.
                        guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                        ventas = {
                                    "id"   : str(datos_ventas["prox_id"]),
                                    "venta": costo,
                                    "fecha_venta": str(datetime.now().date())
                                    }
                        datos_ventas["ventas"].append(ventas)
                        guardar_datos_json(ARCHIVO_VENTAS,datos_ventas)
                        datos_ventas["prox_id"] += 1
                        input("Enter para continuar...")
                        return
                    elif descuento == "1":
                        descuento_a_realizar = input("Ingrese el descuento que desea realizar: ")
                        try:#USAR FLOAT.
                            descuento_a_realizar = int(descuento_a_realizar)
                        except Exception as e:
                            descuento_a_realizar = float(descuento_a_realizar)
                        costo = aplicar_descuento(costo,descuento_a_realizar)
                        print(f"Debe abonar: {costo}") #cuando se termina de registar la venta.
                        guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                        ventas = {
                                    "id"   : str(datos_ventas["prox_id"]),
                                    "venta": costo,
                                    "fecha_venta": str(datetime.now().date())
                                    }
                        datos_ventas["ventas"].append(ventas)
                        guardar_datos_json(ARCHIVO_VENTAS,datos_ventas)
                        datos_ventas["prox_id"] += 1
                        input("Enter para continuar...")
                        return

                
                for producto in datos_inventario["productos"]:
                    if producto["nombre"] == prod or producto["id"] == prod and producto["estado"] == "activo":
                        while True:
                                cantidad = input("Ingrese cuantas unidades desea vender: ")
                                try:
                                    cantidad = int(cantidad)
                                except:
                                    input("Debe ingresar un numero entero.")
                                else:
                                    if cantidad > 0:
                                        if producto["stock"] >= cantidad:
                                            # SI existe usa el precio de promocion y tiene valor, sino el normal
                                            if "promocion" in producto and producto["promocion"]:
                                                precio_unitario = producto["promocion"] 
                                            else: 
                                                precio_unitario = producto["precio"]
                                            
                                            costo += precio_unitario * cantidad
                                            producto["stock"] -= cantidad
                                            print(f"{cantidad} unidad(es) de {producto['nombre']} vendidas.")
                                          
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
    while True:
        limpiar_pantalla()
        if descuento > 98 or descuento <= 0:
            print("Descuento invalido.")
            
            descuento = input("Ingrese un descuento valido:")
            try:
                int(descuento)
            except Exception as e:
                float(descuento)
        else:
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

