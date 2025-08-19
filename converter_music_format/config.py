"""
Configuración y constantes para el Conversor de Audio Universal
"""

import customtkinter as ctk
import warnings

# Configuración de la aplicación
APP_TITLE = "Conversor de Audio Universal"
APP_GEOMETRY = "800x700"
APP_ICON = "icons/musica.ico"

# Formatos de audio soportados
SUPPORTED_FORMATS = ['mp3', 'wav', 'ogg', 'flac', 'm4a', 'aac', 'wma']

# Extensiones de archivos de audio
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma']

# Configuración de colores del tema
COLORS = {
    'primary_green': '#00ff88',
    'secondary_green': '#00aa66',
    'hover_green': '#00cc77',
    'button_green': '#00dd88',
    'button_hover': '#00ff99',
    'error_red': '#ff6b6b',
    'gray': '#666666',
    'gray_hover': '#777777'
}

# URLs y rutas
FFMPEG_DOWNLOAD_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_WEBSITE = "https://ffmpeg.org/download.html"

# Configuración de la interfaz
UI_CONFIG = {
    'main_frame_corner_radius': 10,
    'tab_width': 750,
    'tab_height': 500,
    'button_width': 120,
    'button_height': 35,
    'entry_height': 35,
    'progress_bar_width': 750
}

# Configurar el tema de customtkinter
def setup_theme():
    """Configurar el tema visual de la aplicación"""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    
    # Suprimir warnings de pydub sobre FFmpeg
    warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub")

# Tipos de archivos para diálogos
FILE_TYPES = [
    ("Archivos de Audio", "*.mp3 *.wav *.ogg *.flac *.m4a *.aac *.wma"),
    ("Todos los archivos", "*.*")
]

# Mensajes de la aplicación
MESSAGES = {
    'ready': "Listo para convertir archivos de audio",
    'select_file': "Por favor selecciona un archivo de audio",
    'select_folder': "Por favor selecciona una carpeta",
    'folder_not_exists': "La carpeta seleccionada no existe",
    'no_audio_files': "No se encontraron archivos de audio en la carpeta seleccionada",
    'conversion_started': "Iniciando conversión...",
    'converting_file': "Convirtiendo archivo...",
    'conversion_success': "¡Conversión completada exitosamente!",
    'conversion_error': "Error en la conversión",
    'batch_completed': "¡Conversión por lotes completada!",
    'batch_error': "Error en la conversión por lotes",
    'searching_files': "Buscando archivos de audio...",
    'ffmpeg_success': "FFmpeg se ha instalado correctamente.\nYa puedes convertir archivos de audio.",
    'ffmpeg_error': "Error al descargar FFmpeg:\n{}\n\nPor favor, instálalo manualmente."
}

# Información para la pestaña de ayuda
INFO_TEXT = {
    'formats': "🎵 Formatos Soportados:\n" + " • ".join(fmt.upper() for fmt in SUPPORTED_FORMATS),
    'features': """
🔧 Características:
 • Conversión de archivos individuales
 • Conversión por lotes de carpetas completas
 • Soporte para múltiples formatos de audio
 • Interfaz moderna y fácil de usar
 • Procesamiento en segundo plano

💡 Consejos:
 • Los archivos convertidos mantienen la calidad original
 • Puedes seleccionar una carpeta de destino diferente
 • La conversión por lotes incluye subcarpetas por defecto
 • El progreso se muestra en tiempo real
        """,
    'ffmpeg_info': """FFmpeg es necesario para convertir archivos de audio.

Opciones para instalar FFmpeg:

1. Instalación Automática (Recomendado):
   Haz clic en "Descargar FFmpeg" para instalarlo automáticamente.

2. Instalación Manual:
   • Descarga FFmpeg desde: https://ffmpeg.org/download.html
   • Extrae el archivo en C:\\ffmpeg\\
   • Agrega C:\\ffmpeg\\bin\\ al PATH del sistema

3. Usar Chocolatey (si está instalado):
   Ejecuta: choco install ffmpeg

4. Usar winget:
   Ejecuta: winget install ffmpeg"""
}