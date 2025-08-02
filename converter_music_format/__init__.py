"""
Conversor de Audio Universal - Paquete Modular

Este paquete contiene todos los módulos necesarios para el funcionamiento
del Conversor de Audio Universal con arquitectura modular.

Módulos:
- config: Configuración y constantes
- audio_converter: Lógica de conversión de audio
- ffmpeg_manager: Gestión de FFmpeg
- ui_components: Componentes de interfaz de usuario
- conversion_handlers: Manejadores de conversión
- main_app: Aplicación principal

Versión: 2.0 (Modular)
"""

__version__ = "2.0"
__author__ = "Conversor de Audio Universal"

# Importaciones principales para facilitar el uso del paquete
from .main_app import AudioConverterGUI, main
from .audio_converter import AudioConverter
from .ffmpeg_manager import FFmpegManager
from .config import SUPPORTED_FORMATS, COLORS

__all__ = [
    'AudioConverterGUI',
    'AudioConverter', 
    'FFmpegManager',
    'main',
    'SUPPORTED_FORMATS',
    'COLORS'
]