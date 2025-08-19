#!/usr/bin/env python3
"""
Conversor de Audio Universal - Versión Modular
Punto de entrada principal para la aplicación con arquitectura modular

Autor: Conversor de Audio Universal
Versión: 2.0 (Modular)
"""

import sys
import os

# Agregar el directorio actual al path para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from main_app import main
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"Error importando módulos: {e}")
    print("Asegúrate de que todos los archivos del módulo estén en el mismo directorio.")
    input("Presiona Enter para salir...")
    sys.exit(1)
except Exception as e:
    print(f"Error ejecutando la aplicación: {e}")
    input("Presiona Enter para salir...")
    sys.exit(1)