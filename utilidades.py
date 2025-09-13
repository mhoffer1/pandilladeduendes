import json
import os
from datetime import datetime
from tabulate import tabulate

# Rutas de los archivos de datos
DATA_DIR = "data"
ARCHIVO_INVENTARIO = os.path.join(DATA_DIR, "inventario.json")
ARCHIVO_VENTAS = os.path.join(DATA_DIR, "ventas.json")
ARCHIVO_EMPLEADOS = os.path.join(DATA_DIR, "empleados.json")

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

def validar_numero(texto:str, valor_min=0, valor_max=None) -> float:
    """Validada que la entrada sea un numero
       args:
        texto: str - Texto a mostrar al usuario
        valor_min: float / Valor minimo aceptado (default 0)
        valor_max: float / Valor maximo aceptado (default None, sin maximo)
       return: float / Numero validado
    """
    while True:
        try:
            valor = float(input(texto))
            if valor < valor_min:
                print(f"El valor debe ser al menos: {valor_min}")
                continue
            if valor_max is not None and valor > valor_max:
                print(f"El valor debe ser como maximo: {valor_max}")
                continue
            return valor
        except ValueError:
            print("Por favor ingrese un numero valido.")

def validar_entero(texto:str, valor_min=0, valor_max=None) -> int:
    """valida que la entrada sea un entero
       args:
        texto: str - Texto a mostrar al usuario
        valor_min: int / Valor minimo aceptado (default 0)
        valor_max: int / Valor maximo aceptado (default None, sin maximo)
       return: int / entero validado"""
    while True:
        try:
            valor = int(input(texto))
            if valor < valor_min:
                print(f"El valor debe ser al menos: {valor_min}")
                continue
            if valor_max is not None and valor > valor_max:
                print(f"El valor debe ser como maximo: {valor_max}")
                continue
            return valor
        except ValueError:
            print("Por favor ingrese un numero valido.")

def timestamp_actual():
    """Obtiene la marca de tiempo actual como string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def formatear_tabla(datos_lista:list[dict], mapeo_campos:dict) -> list[list]:
    """Formatea una lista de diccionarios en una tabla para mostrar en consola.
       args:
        datos_lista: list[dict] - Lista de diccionarios con los datos a formatear
        mapeo_campos: dict - Diccionario que mapea los campos a formatear y sus configuraciones
       returns: list[list] - Lista de listas formateadas para tabulate
       """
    datos_formateados = []
    
    for item in datos_lista:
        fila = []
        for campo, config in mapeo_campos.items():
            valor = item.get(campo, 'N/A')
            
            # aplicar segun configuracion
            # isinstance verifica si es un diccionario
            if isinstance(config, dict):
                if 'formato' in config:
                    if config['formato'] == 'moneda':
                        valor = formato_moneda(valor) if isinstance(valor, (int, float)) else valor
                    elif config['formato'] == 'fecha':
                        valor = valor[:10] if isinstance(valor, str) and len(valor) >= 10 else valor
                
                if 'max_largo' in config:
                    valor = truncar_str(valor, config['max_largo'])
            
            fila.append(valor)
        
        datos_formateados.append(fila)
    
    return datos_formateados

def truncar_str(texto:str, max_largo=20) -> str:
    """Trunca una cadena si excede la longitud maxima
       args:
        texto: str - Texto a truncar
        max_largo: int - Longitud maxima permitida (default 20)
       returns: str - Texto truncado con '...' si es necesario
    """
    if not texto:
        return "N/A"
    texto = str(texto)
    return texto[:max_largo-3] + "..." if len(texto) > max_largo else texto

def formato_moneda(monto:float) -> str:
    """Formatea un monto como moneda
       args: monto: float - Monto a formatear
       returns: str - Monto formateado como cadena de moneda"""
    return f"${monto:,.2f}"

def datos_paginados(datos:list[list], tamanio_pag=10) -> list[list[list]]:
    """Divide una lista de datos en paginas
       args:
        datos: list[list] - Lista de listas con los datos a paginar
        tamanio_pagina: int - Numero de elementos por pagina (default 10)
       returns: list[list[list]] - Lista de paginas, cada pagina es una lista de listas
    """
    if not datos:
        return []
    
    paginas = []
    for i in range(0, len(datos), tamanio_pag):
        paginas.append(datos[i:i + tamanio_pag])
    
    return paginas

def mostrar_tabla_pag(datos:list[list], headers:list[str], titulo="Datos", tamanio_pag=10, tablefmt="grid") -> None:
    """ Muestra una tabla paginada en la consola
       args:
        datos: list[list] - Lista de listas con los datos a mostrar
        headers: list[str] - Lista de encabezados de columna
        titulo: str - Titulo de la tabla (default "Datos")
        tamanio_pagina: int - Numero de filas por pagina (default 10)
        fmttabla: str - Formato de tabla para tabulate (default "grid")
    """
    if not datos:
        print(f"No {titulo.lower()} encontrado.")
        input("Presione Enter para continuar...")
        return
    
    paginas = datos_paginados(datos, tamanio_pag)
    pagina_actual = 0
    
    while True:
        limpiar_pantalla()
        print("=" * 70)
        print(f"    {titulo.upper()} - Pagina {pagina_actual + 1} de {len([paginas])}")
        print("=" * 70)
        
        # prerpara los datos para la pagina actual
        datos_pagina = []
        for item in paginas[pagina_actual]:
            if isinstance(item, dict):
                fila = [item.get(header, 'N/A') for header in headers]
            else:
                fila = item
            datos_pagina.append(fila)
        
        # mostrar tabla
        print(tabulate(datos_pagina, headers=headers, tablefmt=tablefmt))
        
        print("-" * 70)
        print(f"Mostrando {len(datos_pagina)} of {len(datos)} total registros")
        
        # opciones de navegacion
        op_nav = []
        if pagina_actual > 0:
            op_nav.append("P - PAgina Anterior")
        if pagina_actual < len(paginas) - 1:
            op_nav.append("N - Pagina Siguiente")
        op_nav.extend(["F - Primera pagina", "L - Ultima Pagina", "Enter - Salir"])
        
        print("\nNavegacion: " + " | ".join(op_nav))
        
        opcion = input("Elegir opcion: ").strip().upper()
        
        if opcion == "N" and pagina_actual < len(paginas) - 1:
            pagina_actual += 1
        elif opcion == "P" and pagina_actual > 0:
            pagina_actual -= 1
        elif opcion == "F":
            pagina_actual = 0
        elif opcion == "L":
            pagina_actual = len(paginas) - 1
        elif opcion == "" or opcion == "EXIT":
            break
        else:
            if opcion not in ["N", "P", "F", "L"]:
                print("Opcion invalida.")
                input("Presione Enter para continuar...")