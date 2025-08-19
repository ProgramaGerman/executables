from generador import generar_contraseña
from gestor_contraseñas import guardar_contraseña, cargar_contraseñas

def actualizar_contraseña_en_archivo(servicio, correo, nueva_contraseña):
    contraseñas = cargar_contraseñas()
    if servicio in contraseñas:
        contraseñas[servicio] = (correo, nueva_contraseña)
        with open('contraseñas.txt', 'w') as archivo:
            for s, (c, p) in contraseñas.items():
                archivo.write(f"{s}:{c}:{p}\n")
        print("Contraseña actualizada exitosamente.")
    else:
        print("Servicio no encontrado.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Generar y Guardar Nueva Contraseña")
        print("2. Regenerar Contraseña Existente")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            longitud = int(input("¿Cuántos dígitos tendrá la nueva contraseña? "))
            contraseña = generar_contraseña(longitud)
            servicio = input("¿Para qué servicio es esta contraseña? ")
            correo = input("¿A qué correo se asociará? ")
            guardar_contraseña(servicio, correo, contraseña)
            print(f"¡Éxito! Contraseña generada y guardada: {contraseña}")

        elif opcion == '2':
            servicio = input("¿Para qué servicio quieres regenerar la contraseña? ")
            contraseñas = cargar_contraseñas()

            if servicio in contraseñas:
                correo_guardado, _ = contraseñas[servicio]
                correo_usuario = input(f"Introduce el correo asociado a '{servicio}' para verificar: ")

                if correo_usuario == correo_guardado:
                    nueva_longitud = int(input("¿Cuántos dígitos tendrá la nueva contraseña? ") )
                    nueva_contraseña = generar_contraseña(nueva_longitud)
                    actualizar_contraseña_en_archivo(servicio, correo_usuario, nueva_contraseña)
                    print(f"Nueva contraseña para '{servicio}' generada y guardada: {nueva_contraseña}")
                else:
                    print("El correo no coincide. No se puede cambiar la contraseña.")
            else:
                print("Servicio no encontrado.")

        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
