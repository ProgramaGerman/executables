import os

def guardar_contraseña(servicio, correo, contraseña):
    with open('contraseñas.txt', 'a') as archivo:
        archivo.write(f"{servicio}:{correo}:{contraseña}\n")

def cargar_contraseñas():
    if not os.path.exists('contraseñas.txt'):
        return {}
    contraseñas = {}
    with open('contraseñas.txt', 'r') as archivo:
        for linea in archivo:
            try:
                servicio, correo, contraseña = linea.strip().split(':', 2)
                contraseñas[servicio] = (correo, contraseña)
            except ValueError:
                # Maneja el caso de líneas con formato antiguo o incorrecto
                print(f"Omitiendo línea con formato incorrecto: {linea.strip()}")
    return contraseñas

def actualizar_contraseña_en_archivo(servicio, correo, nueva_contraseña):
    contraseñas = cargar_contraseñas()
    if servicio in contraseñas:
        contraseñas[servicio] = (correo, nueva_contraseña)
        with open('contraseñas.txt', 'w') as archivo:
            for s, (c, p) in contraseñas.items():
                archivo.write(f"{s}:{c}:{p}\n")
