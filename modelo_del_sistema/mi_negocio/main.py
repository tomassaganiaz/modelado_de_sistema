from models.cliente import Cliente
from models.producto import Producto
from models.venta import Venta
from models.cliente import Cliente


if __name__ == "__main__":
    gestion = Cliente()
    gestion.agregar_cliente(1, "Tomás", "García", "tomas@email.com", "+54 123456789")
    print("Cliente agregado correctamente")

# Crear cliente
cliente1 = Cliente(1, "Tomás", "García", "tomas@email.com", "+54 123456789")

# Crear productos
prod1 = Producto(101, "Laptop", 1200, 5)
prod2 = Producto(102, "Mouse", 25, 20)

# Crear venta
venta1 = Venta(1, "2025-05-28", cliente1, [prod1, prod2])

# Mostrar detalles de la venta
print(venta1.mostrar_detalles())