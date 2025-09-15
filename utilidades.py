import json
import os
from datetime import datetime
from tabulate import tabulate

# Rutas de los archivos de datos
DATA_DIR = "data"
ARCHIVO_INVENTARIO = os.path.join(DATA_DIR, "inventario.json")
ARCHIVO_VENTAS = os.path.join(DATA_DIR, "ventas.json")
ARCHIVO_EMPLEADOS = os.path.join(DATA_DIR, "empleados.json")
ARCHIVO_SUCURSALES = os.path.join(DATA_DIR, "sucursales.json")

def incializar_datos():
    """Incializa todos los archivos de datos con estructuras vacias"""
    # Crea el directorio de datos si no existe
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Incializa el archivo de inventario
    if not os.path.exists(ARCHIVO_INVENTARIO):
        guardar_datos_json(ARCHIVO_INVENTARIO, {"productos": [], "prox_id": 1})
    
    # Inicializa el archivo de ventas
    if not os.path.exists(ARCHIVO_VENTAS):
        guardar_datos_json(ARCHIVO_VENTAS, {"ventas": [], "prox_id": 1})
    
    # Inicializa el archivo de empleados
    if not os.path.exists(ARCHIVO_EMPLEADOS):
        guardar_datos_json(ARCHIVO_EMPLEADOS, {"empleados": [], "prox_id": 1})

    # Inicializa el archivo de sucursales
    if not os.path.exists(ARCHIVO_SUCURSALES):
        guardar_datos_json(ARCHIVO_SUCURSALES, {"sucursales": [], "prox_id": 1})

def cargar_datos_json(file_path):
    """Cargar datos desde un archivo JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error leyendo {file_path}. El archivo puede estar corrupto.")
        return {}

def guardar_datos_json(file_path, data):
    """Guardar datos en un archivo JSON"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error guardando en {file_path}: {e}")
        return False

def limpiar_pantalla():
    """limpiar la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')