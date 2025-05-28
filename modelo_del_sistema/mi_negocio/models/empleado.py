from models.persona import Persona

class Empleado(Persona):
    def __init__(self, id, nombre, apellido, email, telefono, puesto, salario):
        super().__init__(id, nombre, apellido, email, telefono)
        self.puesto = puesto
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre} {self.apellido} - Puesto: {self.puesto} - Salario: ${self.salario}"
