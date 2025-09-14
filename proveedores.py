from utilidades import *

def registrar_provedores():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Registrar proveedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def solicitar_productos_a_proveedor():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Solicitar productos A Provedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def pagos_pendientes():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Pagos pendientes a proveedores")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder:")
        if opcion == "0":
            break

def historial_de_compras_a_cada_proveedor():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Historial de compras de cada proveedor")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
def buscar_proveedor_por_nombre():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Buscar proveedor por nombre.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break