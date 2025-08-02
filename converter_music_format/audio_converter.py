"""
Módulo principal para la conversión de archivos de audio
Contiene la lógica de conversión usando pydub y FFmpeg
"""

import os
import sys
from pathlib import Path
from tkinter import messagebox

try:
    from pydub import AudioSegment
except ImportError:
    messagebox.showerror("Error", "pydub no está instalado. Ejecuta: pip install pydub")
    sys.exit(1)

from config import SUPPORTED_FORMATS, AUDIO_EXTENSIONS


class AudioConverter:
    """
    Clase principal para la conversión de archivos de audio
    """
    
    def __init__(self):
        """Inicializar el conversor"""
        self.supported_formats = SUPPORTED_FORMATS
        self.audio_extensions = AUDIO_EXTENSIONS
    
    def convert_audio_file(self, input_file, output_format, output_dir=None):
        """
        Convertir un archivo de audio al formato especificado
        
        Args:
            input_file (str): Ruta del archivo de entrada
            output_format (str): Formato de salida (mp3, wav, etc.)
            output_dir (str): Directorio de salida (opcional)
        
        Returns:
            tuple: (success: bool, result: str) - Éxito y ruta del archivo o mensaje de error
        """
        try:
            # Verificar que el archivo existe
            if not os.path.exists(input_file):
                return False, f"El archivo {input_file} no existe"
            
            # Verificar formato soportado
            if output_format.lower() not in self.supported_formats:
                return False, f"Formato {output_format} no soportado"
            
            # Obtener información del archivo
            input_path = Path(input_file)
            file_name = input_path.stem
            
            # Determinar directorio de salida
            if output_dir is None:
                output_dir = input_path.parent
            else:
                os.makedirs(output_dir, exist_ok=True)
            
            # Crear nombre del archivo de salida
            output_file = os.path.join(output_dir, f"{file_name}.{output_format.lower()}")
            
            # Cargar el archivo de audio
            audio = AudioSegment.from_file(input_file)
            
            # Convertir y guardar
            audio.export(output_file, format=output_format.lower())
            
            return True, output_file
            
        except Exception as e:
            return False, str(e)
    
    def find_audio_files(self, directory, include_subdirectories=True):
        """
        Buscar archivos de audio en un directorio
        
        Args:
            directory (str): Directorio donde buscar
            include_subdirectories (bool): Incluir subdirectorios en la búsqueda
        
        Returns:
            list: Lista de rutas de archivos de audio encontrados
        """
        audio_files = []
        
        try:
            if not os.path.exists(directory):
                return audio_files
            
            if include_subdirectories:
                # Búsqueda recursiva
                for file_path in Path(directory).rglob('*'):
                    if file_path.suffix.lower() in self.audio_extensions:
                        audio_files.append(str(file_path))
            else:
                # Búsqueda solo en el directorio actual
                for file_path in Path(directory).iterdir():
                    if file_path.is_file() and file_path.suffix.lower() in self.audio_extensions:
                        audio_files.append(str(file_path))
        
        except Exception as e:
            print(f"Error buscando archivos: {e}")
        
        return audio_files
    
    def batch_convert(self, input_directory, output_format, output_dir=None, include_subdirectories=True, progress_callback=None):
        """
        Convertir todos los archivos de audio en un directorio
        
        Args:
            input_directory (str): Directorio con archivos de entrada
            output_format (str): Formato de salida
            output_dir (str): Directorio de salida (opcional)
            include_subdirectories (bool): Incluir subdirectorios
            progress_callback (function): Función para reportar progreso
        
        Returns:
            dict: Estadísticas de la conversión (converted, failed, total)
        """
        stats = {'converted': 0, 'failed': 0, 'total': 0}
        
        try:
            # Buscar archivos de audio
            audio_files = self.find_audio_files(input_directory, include_subdirectories)
            stats['total'] = len(audio_files)
            
            if not audio_files:
                return stats
            
            # Convertir cada archivo
            for i, file_path in enumerate(audio_files):
                if progress_callback:
                    progress_callback(i + 1, stats['total'], os.path.basename(file_path))
                
                success, result = self.convert_audio_file(file_path, output_format, output_dir)
                
                if success:
                    stats['converted'] += 1
                else:
                    stats['failed'] += 1
                    print(f"Error convirtiendo {file_path}: {result}")
        
        except Exception as e:
            print(f"Error en conversión por lotes: {e}")
        
        return stats
    
    def get_audio_info(self, file_path):
        """
        Obtener información detallada de un archivo de audio
        
        Args:
            file_path (str): Ruta del archivo
        
        Returns:
            dict: Información del archivo o None si hay error
        """
        try:
            if not os.path.exists(file_path):
                return None
            
            audio = AudioSegment.from_file(file_path)
            
            info = {
                'filename': os.path.basename(file_path),
                'duration_seconds': len(audio) / 1000,
                'channels': audio.channels,
                'frame_rate': audio.frame_rate,
                'file_size_mb': os.path.getsize(file_path) / (1024 * 1024)
            }
            
            return info
            
        except Exception as e:
            print(f"Error obteniendo información del archivo: {e}")
            return None
    
    def validate_file(self, file_path):
        """
        Validar si un archivo es un archivo de audio válido
        
        Args:
            file_path (str): Ruta del archivo a validar
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            if not os.path.exists(file_path):
                return False
            
            # Verificar extensión
            file_extension = Path(file_path).suffix.lower()
            if file_extension not in self.audio_extensions:
                return False
            
            # Intentar cargar el archivo
            AudioSegment.from_file(file_path)
            return True
            
        except Exception:
            return False