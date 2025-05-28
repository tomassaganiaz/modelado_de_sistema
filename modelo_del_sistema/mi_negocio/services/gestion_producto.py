from models.producto import Producto

class GestionProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, nombre, precio, stock):
        nuevo_producto = Producto(id, nombre, precio, stock)
        self.productos.append(nuevo_producto)

    def actualizar_stock(self, id_producto, nuevo_stock):
        for producto in self.productos:
            if producto.id == id_producto:
                producto.stock = nuevo_stock
                return f"Stock actualizado para {producto.nombre}: {producto.stock} unidades"
        return "Producto no encontrado"

    def listar_productos(self):
        return [f"{p.nombre} - ${p.precio} - Stock: {p.stock}" for p in self.productos]
