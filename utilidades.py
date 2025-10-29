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
    Imprime una linea de "=", cuya cantidad es la cantidad que indique el usuario, o 50 si no se especifica.

    Pre: No recibe parametros.
    Post: Imprime la linea de "=". No retorna nada
    """
    print("="*n)

def opciones(titulos: str, tupla_opciones: tuple[str]) -> None:
    """
    Lista y enumera las opciones recibidas como parametro, imprimiendo el titulo del modulo por encima.

    Pre: Recibe el titulo del modulo y la tupla con las opciones a listar. La ultima opcion debe ser la de Volver atras o Salir del programa.
    Post: No retorna nada, imprime el titulo y el listado de opciones.
    """
    imprimir_titulo(titulos)
    for i, op in enumerate(tupla_opciones):
        if i == len(tupla_opciones)-1: # Si es la ultima opcion va a ser la de salir del programa y lo imprime con un 0
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
        print("La libreria 'tabulate' no esta instalada. Instalala para ver tablas formateadas.")
        # Imprime de forma basica si tabulate no esta disponible
        print(" | ".join(headers))
        print("-" * (len(headers) * 10))
        for row in data:
            print(" | ".join(map(str, row)))

def imprimir_tabla_x_paginas(headers: list[str], lista_datos: list[dict], titulo: str) -> None:
    """
    Imprime una tabla de maximo 10 datos, con un sistema de avanzar o retroceder en paginas.
    la lista de diccionarios tiene un diccionario por empleado.
    Pre: Recibe como parametro una lista de encabezados y una lista de diccionarios correspondientes a cada elemento cuyos datos deben mostrarse en la tabla
    Post: No retorna nada, imprime la tabla con el sistema de paginas.
    """
    por_pagina = 10
    total = len(lista_datos)
    total_paginas = (total + por_pagina - 1) // por_pagina
    pagina = 0

    while True:
        limpiar_pantalla()
        guiones()
        print(f"{titulo.title()} (Pagina {pagina + 1} de {total_paginas})")
        guiones()

        inicio = pagina * por_pagina
        fin = min(inicio + por_pagina, total)

        data = [
            [valor if not isinstance(valor, str) and not isinstance(valor, list) and not isinstance(valor, dict) else valor.title() if isinstance(valor, str) and clave != "id" 
             else formatear_id(valor) if clave == "id" else len(valor) for clave, valor in dato.items()] # Si es int o float lo imprime tal como esta, si es string lo imprime con .title(), si representa la ID lo formatea y si es lista o diccionario imprime el len()
            for dato in lista_datos[inicio:fin]
        ]

        imprimir_tabla(headers, data)
        
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

def pedir_entero(nombre: str, max: int=1000000, min: int=1) -> int:
    """
    Pide un numero entero, maneja posibles errores de casteo y valida que este en el rango ingresado.

    Pre: Recibe como parametros el nombre del objeto, el maximo y el minimo posible a ingresar.
    Post: Retorna el entero ingresado por el usuario, validado previamente.
    """
    while True:
        entero = input(f"Ingrese {nombre.lower()}: ")
        try: # Valida que lo ingresado sea un numero y que se pueda castear a int
            entero = int(entero)
        except ValueError:
            print(f"ERROR - {nombre.capitalize()} debe ser un numero.")
            continue

        if entero < min or entero > max: # Valida que se encuentre en el rango establecido
            print("ERROR - Rango invalido")
            continue
        else:
            return entero

def pedir_float(nombre: str, max: int=1000000.0, min: int=1.0) -> float:
    """
    Pide un numero flotante, maneja posibles errores de casteo y valida que este en el rango ingresado.

    Pre: Recibe como parametros el nombre del objeto, el maximo y el minimo posible a ingresar.
    Post: Retorna el flotante ingresado por el usuario, validado previamente.
    """
    while True:
        flotante = input(f"Ingrese {nombre.lower()}: ")
        try: # Valida que lo ingresado sea un numero y que se pueda castear a float
            flotante = float(flotante)
        except ValueError:
            print(f"ERROR - {nombre.capitalize()} debe ser un numero.")
            continue

        if flotante < min or flotante > max: # Valida que se encuentre en el rango establecido
            print("ERROR - Rango invalido")
            continue
        else:
            return flotante


def listar_datos(elemento: dict) -> None:
    """
    Lista los datos del diccionario en formato apropiado.

    Pre: Recibe como parametro el diccionario cuyos datos deben listarse.
    Post: No retorna nada, se imprime un listado con cada clave y su respectivo valor, dependiendo su formato en tipo de dato que sea.
    """
    for titulo, dato in elemento.items():
        simbolo = "$" if isinstance(dato, float) else ""
        titulo = titulo.replace("_", " ").title() if isinstance(titulo, str) else titulo # Si es string reemplaza los guiones bajos por espacios y aplica el .title()
        dato = f"{dato:.2f}" if isinstance(dato, float) else dato.title() if isinstance(dato, str) else len(dato) if isinstance(dato, list) else dato # Si es un flotante lo formatea con dos decimales, si es string le aplica el title() y si es una lista imprime el len()

        if titulo == "Id":
            titulo, dato = titulo.upper(), formatear_id(dato) # Si es la ID la formatea
        elif titulo == "Estado" or dato == "no info":
            dato = dato.upper() # Si es el estado o si es 'NO INFO' lo imprime en mayusculas
        
        print(f"{titulo}: {dato} {simbolo}")


## Se agrega esta funcion
def seleccionar_item(lista_datos: list[dict], nombre_item: str, tarea: str) -> tuple[int, dict]:
    """Permite seleccionar un elemento por indice o nombre."""
    if not lista_datos:
        print(f"No hay {nombre_item.lower()} registrados.")
        input("Presione Enter para volver...")
        return None, None

    while True:
        limpiar_pantalla()
        imprimir_titulo(tarea)
        for i, item in enumerate(lista_datos, start=1):
            nombre = item.get("nombre", f"{nombre_item} {i}")
            texto = nombre.title() if isinstance(nombre, str) else nombre
            print(f"{i} - {texto}")

        seleccion = input(
            f"\nIngrese el nombre o numero del {nombre_item.lower()} (o 0 para volver): "
        ).strip()

        if seleccion == "0":
            return None, None

        for indice, item in enumerate(lista_datos):
            nombre = item.get("nombre", "")
            if seleccion.isdigit() and int(seleccion) - 1 == indice:
                return indice, item
            if isinstance(nombre, str) and seleccion.lower() == nombre.lower():
                return indice, item

        print(f"No se encontro ese {nombre_item.lower()}.")
        input("Presione Enter para intentarlo nuevamente...")


def formatear_id(id: str) -> str:
    """
    Convierte el dato de ID en formato de cinco digitos (ej: '00199').

    Pre: Recibe como parametro un string correspondiente a la ID.
    Post: Retorna una string con la ID en formato apropiado.
    """
    return f"{'0' * (5 - len(id))}{id}"

def imprimir_titulo(titulo: str) -> None:
    """
    Imprime el titulo entre guiones.

    Pre: Recibe como parametros una string con el titulo a imprimir.
    Post: No retorna nada, imprime el titulo en formato apropiado.
    """
    guiones()
    print(f"    {titulo.upper()}")
    guiones()

def ingresar(tarea:str):
    limpiar_pantalla()
    imprimir_titulo(tarea)
    opcion = input("Ingrese 0 para retroceder y 1 para continuar: ")
    limpiar_pantalla()
    imprimir_titulo(tarea)
    return opcion