#!/usr/bin/env python3
"""
Launcher robusto para el Conversor de Audio Universal
Diseñado específicamente para funcionar con PyInstaller
"""

import sys
import os

def setup_environment():
    """Configurar el entorno para la aplicación"""
    # Si estamos ejecutando desde un ejecutable de PyInstaller
    if getattr(sys, 'frozen', False):
        # Estamos en un ejecutable
        application_path = sys._MEIPASS
    else:
        # Estamos ejecutando el script directamente
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Agregar el directorio de la aplicación al path
    if application_path not in sys.path:
        sys.path.insert(0, application_path)
    
    return application_path

def main():
    """Función principal del launcher"""
    try:
        # Configurar entorno
        app_path = setup_environment()
        
        # Importar y ejecutar la aplicación
        from main_app import main as app_main
        app_main()
        
    except ImportError as e:
        error_msg = f"Error importando módulos: {e}"
        print(error_msg)
        
        # Solo mostrar input si no estamos en un ejecutable
        if not getattr(sys, 'frozen', False):
            input("Presiona Enter para salir...")
        
        sys.exit(1)
        
    except Exception as e:
        error_msg = f"Error ejecutando la aplicación: {e}"
        print(error_msg)
        
        # Solo mostrar input si no estamos en un ejecutable
        if not getattr(sys, 'frozen', False):
            input("Presiona Enter para salir...")
        
        sys.exit(1)

if __name__ == "__main__":
    main()