def calcular_costo_producto():
    """Calcula el costo de un producto basado en la entrada del usuario."""
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    unidades_producto = int(input("Ingrese la cantidad de unidades a solicitar: "))

    costo_total = precio_producto * unidades_producto

    print("ticket de usuario:")
    print(f"Producto: {nombre_producto}")
    print(f"Precio: {precio_producto}")
    print(f"Unidades: {unidades_producto}")
    print(f"Costo total: {costo_total}")