import json
import os
# from datetime import datetime
# from tabulate import tabulate

# Rutas de los archivos de datos, si existen se devuelven y si no se crea mas abajo!!!
DATA_DIR = "data" #carpeta
ARCHIVO_INVENTARIO = f"{DATA_DIR}/inventario.json" #carpeta, archivo.
ARCHIVO_VENTAS = f"{DATA_DIR}/ventas.json"
ARCHIVO_EMPLEADOS = f"{DATA_DIR}/empleados.json"
ARCHIVO_SUCURSALES = f"{DATA_DIR}/sucursales.json"


def cargar_datos_json(file_path:str) -> dict: #para mostrar SOLO sucursales(por ahora.).
    """Cargar datos desde un archivo JSON, se almacena en una variable
       Al principio de cada .py 
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error leyendo {file_path}. El archivo puede estar corrupto.")
        return {}

def guardar_datos_json(file_path:str, data:dict): #para guardar las sucursales(por ahora.)
    """Guardar datos en un archivo JSON"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
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

    # Inicializa el archivo de sucursales
    if not os.path.exists(ARCHIVO_SUCURSALES): #se usa como file path
        guardar_datos_json(ARCHIVO_SUCURSALES, {"sucursales": [], "prox_id": 1})

def limpiar_pantalla()-> None:
    """limpiar la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')