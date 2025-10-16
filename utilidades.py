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

# def editar_dato_json(file_path: str, nombre_seccion: str):
#     if not os.path.exists(file_path):
#         print(f"El archivo '{file_path}' no existe.")
#         return
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#     except json.JSONDecodeError:
#         print("Error: el archivo JSON está dañado o malformado.")
#     except Exception as e:
#         print(f"Error inesperado: {e}")
#     else:
#         if type(data) != dict or not data:
#             print("El archivo JSON no tiene un formato válido (debe ser un diccionario con listas).")
#         print("Claves disponibles en el JSON:")
#         for i, secciones in enumerate(data[next(iter(data))], start=1):
#             print(f"{i}. Cambiar el {nombre_seccion} con el id {secciones["id"]}.")
#         while True:
#             seccion = input(f"Ingrese el {nombre_seccion} que desea modificar: ").strip()
#             if int(seccion) > data[nombre_seccion]["id"]:
#                 print(f"La seccion '{seccion}' no existe en el archivo.") 
#             else:
#                 for k,v in secciones.items():
#                     if seccion == v:
#                         print(f"{secciones}")
#                 input("Presione enter.")

    #     for i,elem in enumerate(seccion):
    #         print(f"{i+1} - {elem["id"]}")
    #     dato = input(f"Ingrese el {elem} que desea modificar: ")
    #     if dato not in elem:
    #         print(f"{dato} no esta en {elem}") 
    #     lista = data[seccion]
    #     if type(lista) != list or not lista:
    #         print(f"'{seccion}' no contiene una lista válida o está vacía.")
    #         return
    #     print(f"\nElementos dentro de '{seccion}':")
    #     for i, elemento in enumerate(lista, start=1):
    #         nombre = elemento.get("nombre", f"Elemento {i}")
    #         print(f"{i}. {nombre}")
    #     eleccion = input("\nIngrese el número o el nombre del elemento que desea modificar: ").strip()
    #     seleccionado = None
    #     if eleccion.isdigit():
    #         indice = int(eleccion) - 1
    #         if 0 <= indice < len(lista):
    #             seleccionado = lista[indice]
    #     else:
    #         for elem in lista:
    #             if elem.get("nombre", "").lower() == eleccion.lower():
    #                 seleccionado = elem
    #                 break
    #     if not seleccionado:
    #         print("No se encontró el elemento seleccionado.")
    #         return
    #     print("\nCampos disponibles para modificar:")
    #     for clave, valor in seleccionado.items():
    #         print(f" - {clave}: {valor}")
    #     campo = input("\nIngrese el nombre del campo que desea modificar: ").strip()
    #     if campo not in seleccionado:
    #         print(f"El campo '{campo}' no existe.")
    #         return
    #     nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip()
    #     if str(seleccionado[campo]).isdigit() and nuevo_valor.isdigit():
    #         nuevo_valor = int(nuevo_valor)
    #     print(f"\nConfirmar cambio de '{campo}' de '{seleccionado[campo]}' a '{nuevo_valor}'?")
    #     confirmar = input("Escriba 's' para confirmar: ").lower()
    #     if confirmar == 's':
    #         seleccionado[campo] = nuevo_valor
    #         with open(file_path, 'w', encoding='utf-8') as file:
    #             json.dump(data, file, indent=2, ensure_ascii=False)
    #         print("Cambio guardado correctamente.")
    #     else:
    #         print("Cambio cancelado.")