import os
from dotenv import load_dotenv
import sys

def get_api_key():
    """
    Carga la API key de Google desde el archivo .env.

    Si la clave no se encuentra, imprime un error y termina el programa.
    """
    # load_dotenv() buscará un archivo .env en el directorio actual o en los superiores.
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        # Usamos sys.stderr para imprimir mensajes de error.
        print("Error: No se encontró la GOOGLE_API_KEY.", file=sys.stderr)
        print("Asegúrate de haber creado un archivo .env en la raíz del proyecto (debugger_ia) con el formato: GOOGLE_API_KEY='tu_clave'", file=sys.stderr)
        sys.exit(1)  # Termina la ejecución si no hay clave.
        
    return api_key

# Este bloque se ejecuta solo si corremos este archivo directamente (ej. python src/config.py)
# Es útil para hacer pruebas rápidas.
if __name__ == '__main__':
    print("Intentando cargar la API key...")
    key = get_api_key()
    print("¡API Key cargada exitosamente!")
    # Por seguridad, solo mostramos los últimos 4 caracteres para verificar.
    print(f"Verificación de la Key (últimos 4 caracteres): ...{key[-4:]}")
