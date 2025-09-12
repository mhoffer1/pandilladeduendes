import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def kiosco() -> str:
    limpiar_pantalla()
    print("""
             1.Kiosco Dulce
             2. Kiosco Gomitas
             3. Super Kiosco
             4. Todos los Kioscos.
              """)
    opcion = int(input("Ingrese que kiosco desea manejar:"))
    while True:
        if opcion == 1:
            return "Kiosco Dulce"
        elif opcion == 2:
            return "Kiosco Gomitas"
        elif opcion == 3:
            return "Super Kiosco"
        elif opcion == 4:
            return "Todos los Kioscos"
        else:
            print("Opcion invalida")
print(kiosco())