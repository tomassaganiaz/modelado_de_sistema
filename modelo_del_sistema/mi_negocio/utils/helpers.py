import datetime

def log_event(mensaje):
    """Registra eventos en un archivo de log."""
    with open("eventos.log", "a") as file:
        file.write(f"{datetime.datetime.now()} - {mensaje}\n")

def validar_email(email):
    """Verifica si un email tiene un formato válido."""
    return "@" in email and "." in email

def calcular_descuento(precio, porcentaje):
    """Calcula el precio con descuento."""
    return precio - (precio * porcentaje / 100)
