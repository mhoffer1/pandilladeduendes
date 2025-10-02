import json
import os
# from datetime import datetime
# from tabulate import tabulate

# Rutas de los archivos de datos, si existen se devuelven y si no se crea mas abajo!!!
DATA_DIR = "data" #carpeta
ARCHIVO_INVENTARIO = f"{DATA_DIR}/inventario.json" #carpeta, archivo.
ARCHIVO_VENTAS = f"{DATA_DIR}/ventas.json"
ARCHIVO_EMPLEADOS = f"{DATA_DIR}/empleados.json"



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
        guardar_datos_json(ARCHIVO_INVENTARIO, {"productos": [], "prox_id": 1})

    # Inicializa el archivo de ventas
    if not os.path.exists(ARCHIVO_VENTAS): #se usa como file path.
        guardar_datos_json(ARCHIVO_VENTAS, {"ventas": [], "prox_id": 1})

    # Inicializa el archivo de empleados
    if not os.path.exists(ARCHIVO_EMPLEADOS): #se usa como file path
        guardar_datos_json(ARCHIVO_EMPLEADOS, {"empleados": [], "prox_id": 1})
    
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

def opciones(titulo: str, tupla_opciones: tuple[str]) -> None:
    """
    Lista y enumera las opciones recibidas como parámetro, imprimiendo el título del módulo por encima.

    Pre: Recibe el título del módulo y la tupla con las opciones a listar. La última opción debe ser la de Volver atrás o Salir del programa.
    Post: No retorna nada, imprime el título y el listado de opciones.
    """
    guiones()
    print(f"    {titulo}")
    guiones()
    for i, op in enumerate(tupla_opciones):
        if i == len(tupla_opciones)-1: # Si es la última opción va a ser la de salir del programa y lo imprime con un 0
            i = -1
        print(f"{i+1}- {op}")
    guiones()