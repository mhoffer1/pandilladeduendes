from utilidades import *
datos_ventas = cargar_datos_json(ARCHIVO_VENTAS)
datos_inventario = cargar_datos_json(ARCHIVO_INVENTARIO)
from datetime import datetime
def menu_ventas():
    "Muestra el menu de Ventas"
    while True:
        limpiar_pantalla()
        opciones_ventas = ("Registrar Venta", "Aplicar Descuento/Promoción", "Mostrar Historial de Ventas", "Volver al Menú Principal")
        opciones("VENTAS", opciones_ventas)

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            elegir_descuento_o_promocion()
        elif opcion == "3":
            elegir_historial_ventas()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")


def registrar_ventas():  
      
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
                prod = input("Ingrese el nombre o ID del producto que quiere vender(0 para terminar venta):")
                if prod == "0":
                    print(f"Debe abonar: {costo}") #cuando se termina de registar la venta.
                    guardar_datos_json(ARCHIVO_INVENTARIO, datos_inventario)
                    ventas = {
                                "id"   : str(datos_ventas["prox_id"]),
                                "venta": costo,
                                "fecha_venta": str(datetime.now().date())
                                
                                }
                    datos_inventario["prox_id"] += 1
                    datos_ventas["ventas"].append(ventas)
                    guardar_datos_json(ARCHIVO_VENTAS,datos_ventas)
                    datos_ventas["prox_id"] += 1
                    input("Enter para continuar...")

                    break
                
                for producto in datos_inventario["productos"]:
                    if producto["nombre"] == prod or producto["id"] == prod:
                        
                        while True:
                            cantidad = input("Ingrese cuantas unidades desea vender:")
                            try:
                                cantidad = int(cantidad)
                            except Exception as e:
                                input("Debe ingresar un numero entero.")
                    
                            
                            else:
                                if cantidad > 0:
                                        costo += producto["costo"] * cantidad
                                        producto["stock"] -= cantidad
                                        break
                                else:
                                    print("Ingresar un numero positivo.")
                        break
                    else:
                        print("Producto no encontrado.")
                        input("Enter para continuar.")
                        break

      
    
def elegir_descuento_o_promocion(): 
    
    while True:
        limpiar_pantalla()
        opciones_desc_o_prom = ("Aplicar Descuento", "Aplicar Promoción", "Volver Atrás")
        opciones("APLICAR DESCUENTO O PROMOCIÓN", opciones_desc_o_prom)
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            aplicar_descuento()
        elif opcion == "2":
            aplicar_promocion()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def aplicar_descuento():
    while True:
        limpiar_pantalla()
        guiones()
        print("APLICAR DESCUENTO")
        guiones()
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def aplicar_promocion():
    while True:
        limpiar_pantalla()
        guiones()
        print("APLICAR PROMOCIÓN")
        guiones()
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def elegir_historial_ventas():
    "podes ver el historial de ventas y filtrar por dia,mes y año."

    while True:
        limpiar_pantalla()
        opciones_hist = ("Ver Historial del Día", "Ver Historial de la Semana", "Ver Historial del Mes", "Volver Atrás")
        opciones("ELEGIR HISTORIAL DE VENTAS", opciones_hist)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            historial_por_dia()
        elif opcion == "2":
            historial_por_semana()
        elif opcion == "3":
            historial_por_mes()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def historial_por_dia():
    "ves el historial de ventas diario."
    while True:
        limpiar_pantalla()
        guiones()
        print("HISTORIAL DE VENTAS POR DIA")
        guiones()
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")

def historial_por_semana():
    "ves el historial de ventas semanal."
    while True:
        limpiar_pantalla()
        guiones()
        print("HISTORIAL DE VENTAS POR SEMANA")
        guiones()
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
                print("Opcion invalida. Intente de nuevo.")
                input("Presione Enter para continuar...")
        
        
def historial_por_mes():
    "ves el historial de ventas mensual."
    while True:
        limpiar_pantalla()
        guiones()
        print("HISTORIAL DE VENTAS POR MES")
        guiones()
        opcion =  input("Presiona 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            