from models.persona import Persona

class Cliente(Persona):
    def __init__(self, id, nombre, apellido, email, telefono):
        super().__init__(id, nombre, apellido, email, telefono)
