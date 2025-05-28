from models.venta import Venta
from models.cliente import Cliente
from models.producto import Producto

class GestionVentas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, id_venta, fecha, cliente, productos):
        nueva_venta = Venta(id_venta, fecha, cliente, productos)
        self.ventas.append(nueva_venta)
        return f"Venta #{id_venta} registrada con total de ${nueva_venta.total}"

    def listar_ventas(self):
        return [venta.mostrar_detalles() for venta in self.ventas]
