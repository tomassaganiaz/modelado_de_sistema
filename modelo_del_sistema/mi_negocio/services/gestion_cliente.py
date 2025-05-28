from models.cliente import Cliente

class GestionClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, id, nombre, apellido, email, telefono):
        nuevo_cliente = Cliente(id, nombre, apellido, email, telefono)
        self.clientes.append(nuevo_cliente)
