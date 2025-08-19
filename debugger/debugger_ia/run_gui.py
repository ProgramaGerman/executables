#!/usr/bin/env python3
"""
Script para ejecutar la interfaz gráfica del Debugger IA.
"""

import sys
import os

# Agregar el directorio src al path para las importaciones
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from gui import main

if __name__ == "__main__":
    main()