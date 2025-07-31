"""
Paquete del Generador de Códigos QR
Aplicación modular con interfaz gráfica moderna usando CustomTkinter
"""

__version__ = "2.0.0"
__author__ = "QR Generator Team"
__description__ = "Generador de códigos QR con interfaz gráfica moderna y modular"

# Importaciones principales para facilitar el uso del paquete
from .main_app import QRGeneratorApp
from .qr_generator import QRGenerator
from .file_manager import FileManager, ConfigManager

__all__ = [
    "QRGeneratorApp",
    "QRGenerator", 
    "FileManager",
    "ConfigManager"
]