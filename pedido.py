import sqlite3
conexion = sqlite3.connect("./happyburger.db")


class Pedido:
    """Clase para el manejo de pedidos."""
    def mostrar_pedido(self):
        """Mostrar todos los pedidos."""
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Pedido')
        pedidos = cursor.fetchall()
        conexion.commit()

        for pedido in pedidos:
            print(pedido)

    def crear_pedido(self):
        """Crea un nuevo pedido."""
        cliente = input("Ingrese el nombre del cliente: ")
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = float(input("Ingrese la cantidad: "))

        conexion.execute(
            "INSERT INTO Pedido (cliente, producto, precio) VALUES (?, ?, ?)", (cliente, producto, precio))
        conexion.commit()

        with open("ticket.txt", "w") as archivo:
            archivo.write("Detalles del pedido:\n")
            archivo.write(f"Cliente: {cliente}\n")
            archivo.write(f"Producto: {producto}\n")
            archivo.write(f"Precio: {precio}\n")
            archivo.write(f"total a pagar es: {precio * cantidad}\n")

    def cancelar_pedido(self):
        """Cancela un pedido existente."""
        pedido = input("Ingrese la clave del pedido a eliminar: ")

        # Eliminar el registro de la tabla Clientes
        conexion.execute("DELETE FROM Pedido WHERE pedido = ?", (pedido,))
        conexion.commit()
