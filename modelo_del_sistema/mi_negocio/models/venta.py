from models.producto import Producto
from models.cliente import Cliente

class Venta:
    def __init__(self, id_venta, fecha, cliente, productos):
        self.id_venta = id_venta
        self.fecha = fecha
        self.cliente = cliente  # Instancia de Cliente
        self.productos = productos  # Lista de objetos Producto
        self.total = sum(p.precio for p in productos)

    def mostrar_detalles(self):
        detalle_productos = "\n".join([f"{p.nombre} - ${p.precio}" for p in self.productos])
        return f"Venta #{self.id_venta} - Cliente: {self.cliente.nombre}\nFecha: {self.fecha}\nProductos:\n{detalle_productos}\nTotal: ${self.total}"
