from clientes import Clientes
from menu import Menu
from pedido import Pedido
from costoProducto import calcular_costo_producto
import sqlite3

conexion = sqlite3.connect("happyburger.db")

conexion.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    direccion TEXT,
    correo_electronico TEXT,
    telefono TEXT
)
""")

conexion.execute("""
CREATE TABLE IF NOT EXISTS Menu (
    clave TEXT PRIMARY KEY,
    nombre TEXT,
    precio REAL
)
""")

conexion.execute("""
CREATE TABLE IF NOT EXISTS Pedido (
    pedido INTEGER PRIMARY KEY,
    cliente TEXT,
    producto TEXT,
    precio REAL
)
""")


def inciarApp():
    """Controla el flujo del programa según la opción seleccionada por el usuario."""
    while True:
        print("------------------------------------")
        print("Bienvenido al sistema de HAYPPY BURGER ")
        print(""" 
                1.- Pedido
                2.- Clientes
                3.- Menu
                4.- Salir del programa
                """)
        opcion = int(input("Indica una opción del menú: "))

        if opcion == 1:
            print("Ha seleccionado la opción Pedidos")
            print(""" 
                1.- CREAR PEDIDO
                2.- CANCELAR PEDIDO
                3.- SIMULADOR Calcular COSTO PEDIDO 
                4.- Regresar Ménu principal
                """)
           
           
            opcionP = int(input("indica una opción:"))
            if opcionP == 1:
                print("Crea tu pedido")
                pedido = Pedido()
                pedido.crear_pedido()
               
            if opcionP == 2:
                print("Lista de pedidos actuales")
                print("------------------------------------")
                pedido = Pedido()
                pedido.mostrar_pedido()
                print("------------------------------------")
                print("Escoge tu pedido a Cancela")
                pedido = Pedido()
                pedido.cancelar_pedido()

            if opcionP == 3:
                print("Calcula el costo deL producto")
                calcular_costo_producto()

            if opcionP == 4:
                return inciarApp()
           

        elif opcion == 2:

            print("Ha seleccionado la opción Clientes")
            print(""" 
                1.- AGREGAR CLIENTE
                2.- ACTUALIZAR CLIENTE
                3.- ELIMINAR CLIENTE
                4.- Regresar Ménu principal
                """)
            opcionC = int(input("indica una opción:"))
            if opcionC == 1:
                print("AGREGA UN CLIENTE")
                clientes = Clientes()
                clientes.agregar_cliente()

            if opcionC == 2:
                print("ACTUALIZAR CLIENTE")
                clientes = Clientes()
                clientes.actualizar_cliente()

            if opcionC == 3:
                print("ELIMINA UN CLIENTE")
                clientes = Clientes()
                clientes.eliminar_cliente()

            if opcionC == 4:
                return inciarApp()
           
        elif opcion == 3:

            print("Ha seleccionado la opción Menú")
            print(""" 
                1.- AGREGAR PRODUCTO
                2.- ACTUALIZAR PRODUCTO
                3.- ELIMINAR PRODUCTO
                4.- Regresar Ménu principal
                """)
            opcionM = int(input("indica una opción:"))
            if opcionM == 1:
                print("AGREGA UN PRODUCTO")
                menu = Menu()
                menu.agregar_producto()

            if opcionM == 2:
                print("ACTUALIZAR CLIENTE")
                menu = Menu()
                menu.actualizar_producto()

            if opcionM == 3:
                print("ELIMINA UN CLIENTE")
                menu = Menu()
                menu.eliminar_producto()

            if opcionM == 4:
                return inciarApp()
           

        elif opcion == 4:

            print("Ha seleccionado la opción Salir. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


inciarApp()
