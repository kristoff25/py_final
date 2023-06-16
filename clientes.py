import sqlite3
conexion = sqlite3.connect("happyburger.db")

class Clientes:
    """Clase para el manejo de clientes."""

    def agregar_cliente(self):
        """Agrega un nuevo cliente al directorio."""
        clave = input("Ingrese la clave del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")

        # Insertar el registro en la tabla Clientes
        conexion.execute("INSERT INTO Clientes VALUES (?, ?, ?, ?, ?)", (clave, nombre, direccion, correo, telefono))
        conexion.commit()
        pass

    def eliminar_cliente(self):
        """Elimina un cliente del directorio."""
        clave = input("Ingrese la clave del cliente a eliminar: ")

        # Eliminar el registro de la tabla Clientes
        conexion.execute("DELETE FROM Clientes WHERE clave = ?", (clave,))
        conexion.commit()

    def actualizar_cliente(self):
        """Actualiza los datos de un cliente existente."""
        clave = input("Ingrese la clave del cliente a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        direccion = input("Ingrese la nueva dirección del cliente: ")
        correo = input("Ingrese el nuevo correo electrónico del cliente: ")
        telefono = input("Ingrese el nuevo teléfono del cliente: ")

        # Actualizar el registro en la tabla Clientes
        conexion.execute("UPDATE Clientes SET nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? WHERE clave = ?", (nombre, direccion, correo, telefono, clave))
        conexion.commit()
