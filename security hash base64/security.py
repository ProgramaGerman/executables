"""Programa educativo sobre conceptos de seguridad: hashing de contraseñas y codificación de datos."""

# Programa creado por: @GermanGonzalez
# Fecha de creación: 2024-07-30

import hashlib
import base64
import os


def hash_password(password: str) -> str:
    """
    Genera un hash seguro de la contraseña usando un salt y lo devuelve
    en un formato combinado (salt:hash) para un fácil almacenamiento.
    """
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Almacenar el salt y el hash juntos, separados por un delimitador
    return f"{salt.hex()}:{hashed_password.hex()}"


def verify_password(stored_password: str, password_to_check: str) -> bool:
    """Verifica si una contraseña coincide con un hash y salt almacenados."""
    try:
        salt_hex, stored_hash_hex = stored_password.split(':')
        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(stored_hash_hex)
    except ValueError:
        # Si el formato es incorrecto, la contraseña no puede ser válida
        return False

    # Hashea la contraseña a verificar usando el mismo salt
    new_hash = hashlib.pbkdf2_hmac('sha256', password_to_check.encode('utf-8'), salt, 100000)
    return new_hash == stored_hash


def encode_data_b64(data: str) -> str:
    """Codifica datos a formato Base64. NO es un cifrado seguro."""
    return base64.b64encode(data.encode("utf-8")).decode("utf-8")


def decode_data_b64(encoded_data: str) -> str:
    """Decodifica datos desde el formato Base64."""
    return base64.b64decode(encoded_data.encode("utf-8")).decode("utf-8")


if __name__ == "__main__":
    # Ejemplo de uso
    password = input("Introduce una contraseña: ")
    
    # Al crear una cuenta, guardas la contraseña hasheada en tu base de datos
    stored_password = hash_password(password)
    print(f"Contraseña original: {password}")
    print(f"Contraseña hasheada (guardar en BBDD): {stored_password}")

    # Cuando el usuario inicia sesión
    is_valid = verify_password(stored_password, password)
    print(f"\n¿La contraseña '{password}' es correcta? {is_valid}")
    
    is_invalid = verify_password(stored_password, "contraseña_incorrecta")
    print(f"¿La contraseña 'contraseña_incorrecta' es correcta? {is_invalid}\n")

    DATA = "Datos sensibles que necesitan ser codificados"
    encoded_data = encode_data_b64(DATA)
    print(f"Datos codificados en Base64: {encoded_data}")

    decoded_data = decode_data_b64(encoded_data)
    print(f"Datos decodificados: {decoded_data}")