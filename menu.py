import sqlite3
conexion = sqlite3.connect("happyburger.db")


class Menu:
    """Clase para el manejo del menú."""

    def agregar_producto(self):
        """Agrega un nuevo producto al menú."""
        clave = input("Ingrese la clave del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))

        # Insertar el registro en la tabla Menu
        conexion.execute("INSERT INTO Menu VALUES (?, ?, ?)",
                         (clave, nombre, precio))
        conexion.commit()

    def eliminar_producto(self):
        """Elimina un producto del menú."""
        clave = input("Ingrese la clave del producto a eliminar: ")

        # Eliminar el registro de la tabla Menu
        conexion.execute("DELETE FROM Menu WHERE clave = ?", (clave,))
        conexion.commit()

    def actualizar_producto(self):
        """Actualiza los datos de un producto existente."""
        clave = input("Ingrese la clave del producto a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))

        # Actualizar el registro en la tabla Menu
        conexion.execute(
            "UPDATE Menu SET nombre = ?, precio = ? WHERE clave = ?", (nombre, precio, clave))
        conexion.commit()
