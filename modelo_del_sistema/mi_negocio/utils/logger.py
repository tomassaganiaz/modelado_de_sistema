import datetime

def log_event(mensaje):
    with open("eventos.log", "a") as file:
        file.write(f"{datetime.datetime.now()} - {mensaje}\n")
