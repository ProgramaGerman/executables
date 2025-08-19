import argparse
import os
import sys
import analizador

def main():
    """
    Función principal para la interfaz de línea de comandos (CLI).
    """
    parser = argparse.ArgumentParser(
        description="Analizador de código Python que utiliza la IA de Gemini para encontrar errores y sugerir mejoras.",
        epilog="Ejemplo de uso: python -m debugger_ia.src.main ruta/a/tu/archivo.py"
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="La ruta al archivo de Python que quieres analizar."
    )
    
    args = parser.parse_args()
    
    file_path = args.file_path
    
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"Error: El archivo '{file_path}' no fue encontrado.", file=sys.stderr)
        sys.exit(1)
        
    # Verificar si es un archivo
    if not os.path.isfile(file_path):
        print(f"Error: La ruta '{file_path}' no corresponde a un archivo.", file=sys.stderr)
        sys.exit(1)

    try:
        # Leer el contenido del archivo especificado por el usuario
        with open(file_path, 'r', encoding='utf-8') as f:
            codigo = f.read()
            
        print(f"Analizando el archivo: {file_path}")
        print("Contactando a la IA... Esto puede tardar un momento.\n")
        
        # Enviar el código a nuestro módulo analizador
        resultado_analisis = analizador.analizar_codigo(codigo)
        
        # Imprimir el resultado
        print("--- ANÁLISIS COMPLETADO ---")
        print(resultado_analisis)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}", file=sys.stderr)
        sys.exit(1)
