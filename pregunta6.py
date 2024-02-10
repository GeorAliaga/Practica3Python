class Producto:
    def __init__(self, nombre, marca, precio, año):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} ({self.marca}), Precio: {self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de Productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

try:
    catalogo = Catalogo()

    producto1 = Producto("Motor", "Promix", 120, 2022)
    producto2 = Producto("Aceite", "Quality", 100, 2021)
    producto3 = Producto("Pintura", "Refinish", 1000, 2022)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)




    catalogo.mostrar_productos()


    año_filtro = int(input("Ingrese el año para filtrar productos: "))
    productos_filtrados = catalogo.filtrar_por_año(año_filtro)

    if productos_filtrados:
        print(f"\nProductos para el año {año_filtro}:")
        for producto in productos_filtrados:
            print(producto)
    else:
        print(f"No hay productos para el año {año_filtro}.")

except ValueError:
    print("Error: Ingrese un valor numerico para el año.")
