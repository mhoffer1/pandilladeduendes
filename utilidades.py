import json
import os
from tabulate import tabulate

# from datetime import datetime

# Rutas de los archivos de datos, si existen se devuelven y si no se crea mas abajo!!!
DATA_DIR = "data" #carpeta
ARCHIVO_INVENTARIO = f"{DATA_DIR}/inventario.json" #carpeta, archivo.
ARCHIVO_VENTAS = f"{DATA_DIR}/ventas.json"
ARCHIVO_EMPLEADOS = f"{DATA_DIR}/empleados.json"
ARCHIVO_PROVEEDORES= f"{DATA_DIR}/proveedores.json"


def cargar_datos_json(file_path:str) -> dict: #para mostrar SOLO sucursales(por ahora.).
    """Cargar datos desde un archivo JSON, se almacena en una variable
       Al principio de cada .py 
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file) #retorna un dict. load = lee
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error leyendo {file_path}. El archivo puede estar corrupto.")
        return {}

def guardar_datos_json(file_path:str, data:dict): #para guardar las sucursales(por ahora.)
    """Guardar datos en un archivo JSON"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False) #dump= escribee
        return True
    except Exception as e:
        print(f"Error guardando en {file_path}: {e}")
        return False


def incializar_datos()->None:
    """Incializa todos los archivos de datos con estructuras vacias"""
    # Crea el directorio de datos si no existe
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Incializa el archivo de inventario
    if not os.path.exists(ARCHIVO_INVENTARIO): #si no esta en el path, se crea 
        guardar_datos_json(ARCHIVO_INVENTARIO, {"productos": [], "prox_id": 1,}) #crea un diccionario, que adentro tiene una lista que va a estar compuesta por diccionarios.

    # Inicializa el archivo de ventas
    if not os.path.exists(ARCHIVO_VENTAS): #se usa como file path.
        guardar_datos_json(ARCHIVO_VENTAS, {"ventas": [], "prox_id": 1})

    # Inicializa el archivo de empleados
    if not os.path.exists(ARCHIVO_EMPLEADOS): #se usa como file path
        guardar_datos_json(ARCHIVO_EMPLEADOS, {"empleados": [], "prox_id": 1})
    #Inicializa el archivo de proveedores
    if not os.path.exists(ARCHIVO_PROVEEDORES): #se usa como file path
        guardar_datos_json(ARCHIVO_PROVEEDORES, {"proveedores": [], "prox_id": 1})
    
def limpiar_pantalla()-> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    """limpiar la pantalla de la consola"""

def guiones(n=50) -> None:
    """
    Imprime una línea de "=", cuya cantidad es la cantidad que indique el usuario, o 50 si no se especifica.

    Pre: No recibe parámetros.
    Post: Imprime la línea de "=". No retorna nada
    """
    print("="*n)

def opciones(titulos: str, tupla_opciones: tuple[str]) -> None:
    """
    Lista y enumera las opciones recibidas como parámetro, imprimiendo el título del módulo por encima.

    Pre: Recibe el título del módulo y la tupla con las opciones a listar. La última opción debe ser la de Volver atrás o Salir del programa.
    Post: No retorna nada, imprime el título y el listado de opciones.
    """
    titulo(titulos)
    for i, op in enumerate(tupla_opciones):
        if i == len(tupla_opciones)-1: # Si es la última opción va a ser la de salir del programa y lo imprime con un 0
            i = -1
        print(f"{i+1}- {op.title()}")
    guiones()

def imprimir_tabla(headers: list[str], data: list[list[str]]) -> None:
    """
    Imprime una tabla con los datos y encabezados proporcionados.

    Pre: Recibe una lista de encabezados y una lista de listas con los datos.
    Post: No retorna nada, imprime la tabla en la consola.
    """
    try:
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except ImportError:
        print("La librería 'tabulate' no está instalada. Instálala para ver tablas formateadas.")
        # Imprime de forma básica si tabulate no está disponible
        print(" | ".join(headers))
        print("-" * (len(headers) * 10))
        for row in data:
            print(" | ".join(map(str, row)))

def imprimir_tabla_x_paginas(headers: list[str], lista_datos: list[dict], titulo: str):
    """
    Imprime una tabla de máximo 10 datos, con un sistema de avanzar o retroceder en páginas.
    la lista de diccionarios tiene un diccionario por empleado.
    Pre: Recibe como parámetro una lista de encabezados y una lista de diccionarios correspondientes a cada elemento cuyos datos deben mostrarse en la tabla
    Post: No retorna nada, imprime la tabla con el sistema de páginas.
    """
    por_pagina = 10
    total = len(lista_datos)
    total_paginas = (total + por_pagina - 1) // por_pagina
    pagina = 0

    while True:
        limpiar_pantalla()
        guiones()
        print(f"{titulo.title()} (Página {pagina + 1} de {total_paginas})")
        guiones()

        inicio = pagina * por_pagina
        fin = min(inicio + por_pagina, total)

        data = [
            [x if not isinstance(x, str) and not isinstance(x, list) else x.title() if isinstance(x, str) else len(x) for x in dato.values()]
            for dato in lista_datos[inicio:fin]
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
        continue

def pedir_entero(nombre: str, min: int=1, max: int=1_000_000):
    """
    Pide un número entero, maneja posibles errores de casteo y valida que esté en el rango ingresado.

    Pre: Recibe como parámetros el nombre del objeto, el mínimo y el máximo posible a ingresar.
    Post: Retorna el entero ingresado por el usuario, validado previamente.
    """
    while True:
        entero = input(f"Ingrese el valor de {nombre.lower()}: ")
        try: # Valida que lo ingresado sea un número y que se pueda castear a int
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {nombre.capitalize()} debe ser un número.")
            continue

        if entero < min or entero > max: # Valida que se encuentre en el rango establecido
            print("ERROR - Rango inválido")
            continue
        else:
            return entero

def pedir_float(nombre: str, min: float=1.0, max: float=1000000.0):
    """
    Pide un número flotante, maneja posibles errores de casteo y valida que esté en el rango ingresado.

    Pre: Recibe como parámetros el nombre del objeto, el mínimo y el máximo posible a ingresar.
    Post: Retorna el flotante ingresado por el usuario, validado previamente.
    """
    while True:
        flotante = input(f"Ingrese el valor de {nombre.lower()}: ")
        try: # Valida que lo ingresado sea un número y que se pueda castear a float
            flotante = float(flotante)
        except ValueError:
            print(f"ERROR - {nombre.capitalize()} debe ser un número.")
            continue

        if flotante < min or flotante > max: # Valida que se encuentre en el rango establecido
            print("ERROR - Rango inválido")
            continue
        else:
            return flotante
        
def titulo(titulo):
    guiones()
    print(f"    {titulo.upper()}")
    guiones()

def ingresar(tarea:str):
    limpiar_pantalla()
    titulo(tarea)
    opcion = input("Ingrese 0 para retroceder y 1 para continuar: ")
    limpiar_pantalla()
    titulo(tarea)
    return opcion