from utilidades import *
def registrar_ventas():
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Reporte De Ventas")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder: ")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Por favor, ingrese 0 para salir.")
         
    
def aplicar_descuento(): 
    limpiar_pantalla()
    while True:
        print("=" * 50)
        print("Aplicar descuento.")
        print("=" * 50)
        opcion = input("Ingrese 0 para retroceder:")
        if opcion == "0":
            break
        else:
            print("Opcion invalida. Por favor, ingrese 0 para salir.")

def mostrar_historial_ventas():
    limpiar_pantalla()
    print("=" * 50)
    print("Mostrar historial de Ventas")
    
    print("=" * 50)
    while True:
        opcion = input("Seleccione 1.si quiere ver el historial del dia, 2. si quiere ver el semanal, 3.si quiere ver el mensual,0.Para salir.")
        if opcion == "1":
            historial_por_dia()
            break
        elif opcion == "2":
            historial_por_semana()
            break
        elif opcion == "3":
            historial_por_mes()
            break
        elif opcion == "0":
            break
def historial_por_dia():
    limpiar_pantalla()
    print("=" * 50)
    print("Mostrar historial de Ventas Por Dias")
    print("=" * 50)
    opcion =  input("Presiona 0 para retroceder.")
    if opcion == "0":
        mostrar_historial_ventas()
    else:
        print("Opcion invalida.")

def historial_por_semana():
    limpiar_pantalla()
    print("=" * 50)
    print("Mostrar historial de Ventas Por Semana")
    print("=" * 50)
    opcion =  input("Presiona 0 para retroceder.")
    if opcion == "0":
        mostrar_historial_ventas()
    else:
        print("Opcion invalida.")
        
def historial_por_mes():
    limpiar_pantalla()
    print("=" * 50)
    print("Mostrar historial de Ventas Por Mes.")
    print("=" * 50)
    opcion =  input("Presiona 0 para retroceder.")
    if opcion == "0":
        mostrar_historial_ventas()
    else:
        print("Opcion invalida.")

        

    

