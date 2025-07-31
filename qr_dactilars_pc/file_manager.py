"""
Módulo para manejo de archivos
Contiene funciones para guardar, cargar y gestionar archivos QR
"""

import os
from tkinter import filedialog, messagebox
from PIL import Image


class FileManager:
    """Clase para gestionar operaciones de archivos"""
    
    @staticmethod
    def save_qr_dialog(qr_image, default_name="qr_code", parent=None):
        """
        Abre diálogo para guardar el código QR
        
        Args:
            qr_image: Imagen PIL del QR
            default_name: Nombre por defecto del archivo
            parent: Ventana padre para el diálogo
            
        Returns:
            str: Ruta del archivo guardado o None si se canceló
        """
        if not qr_image:
            messagebox.showerror("Error", "No hay imagen QR para guardar", parent=parent)
            return None
            
        try:
            # Configurar el diálogo de guardar
            filename = filedialog.asksaveasfilename(
                parent=parent,
                title="Guardar código QR como...",
                defaultextension=".png",
                initialfile=f"{default_name}.png",
                filetypes=[
                    ("Archivos PNG", "*.png"),
                    ("Archivos JPEG", "*.jpg"),
                    ("Archivos BMP", "*.bmp"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            if filename:
                # Crear directorio si no existe
                FileManager.create_directory_if_needed(filename)
                
                # Guardar imagen
                qr_image.save(filename)
                messagebox.showinfo("Éxito", f"✅ Código QR guardado como:\n{filename}", parent=parent)
                return filename
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar archivo: {str(e)}", parent=parent)
            
        return None
    
    @staticmethod
    def create_directory_if_needed(file_path):
        """
        Crea el directorio padre si no existe
        
        Args:
            file_path (str): Ruta completa del archivo
        """
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
                return True
            except OSError as e:
                raise Exception(f"Error al crear directorio {directory}: {e}")
        return True
    
    @staticmethod
    def get_safe_filename(base_name, extension=".png"):
        """
        Genera un nombre de archivo seguro
        
        Args:
            base_name (str): Nombre base del archivo
            extension (str): Extensión del archivo
            
        Returns:
            str: Nombre de archivo seguro
        """
        # Remover caracteres no válidos
        invalid_chars = '<>:"/\\|?*'
        safe_name = ''.join(c for c in base_name if c not in invalid_chars)
        
        # Limitar longitud
        if len(safe_name) > 50:
            safe_name = safe_name[:50]
            
        # Agregar extensión si no la tiene
        if not safe_name.lower().endswith(extension.lower()):
            safe_name += extension
            
        return safe_name
    
    @staticmethod
    def save_examples_batch(examples_folder="ejemplos_qr"):
        """
        Guarda ejemplos en lote
        
        Args:
            examples_folder (str): Carpeta donde guardar los ejemplos
            
        Returns:
            list: Lista de archivos generados
        """
        try:
            from qr_generator import QRGenerator
            
            # Crear carpeta si no existe
            if not os.path.exists(examples_folder):
                os.makedirs(examples_folder, exist_ok=True)
                
            # Generar ejemplos usando QRGenerator
            generated_files = QRGenerator.generate_examples(examples_folder)
            
            return generated_files
            
        except Exception as e:
            raise Exception(f"Error al generar ejemplos: {e}")
    
    @staticmethod
    def open_file_location(file_path):
        """
        Abre la ubicación del archivo en el explorador
        
        Args:
            file_path (str): Ruta del archivo
        """
        try:
            import subprocess
            import platform
            
            if platform.system() == "Windows":
                subprocess.run(["explorer", "/select,", file_path])
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "-R", file_path])
            else:  # Linux
                subprocess.run(["xdg-open", os.path.dirname(file_path)])
                
        except Exception as e:
            messagebox.showwarning("Advertencia", f"No se pudo abrir la ubicación: {e}")
    
    @staticmethod
    def get_recent_files(max_files=5):
        """
        Obtiene lista de archivos recientes (placeholder para futura implementación)
        
        Args:
            max_files (int): Número máximo de archivos recientes
            
        Returns:
            list: Lista de archivos recientes
        """
        # Placeholder para implementación futura
        # Podría leer de un archivo de configuración o registro
        return []
    
    @staticmethod
    def validate_image_format(file_path):
        """
        Valida que el archivo sea una imagen válida
        
        Args:
            file_path (str): Ruta del archivo
            
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            with Image.open(file_path) as img:
                img.verify()
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_file_info(file_path):
        """
        Obtiene información del archivo
        
        Args:
            file_path (str): Ruta del archivo
            
        Returns:
            dict: Información del archivo
        """
        try:
            if os.path.exists(file_path):
                stat = os.stat(file_path)
                return {
                    "size": stat.st_size,
                    "modified": stat.st_mtime,
                    "created": stat.st_ctime,
                    "exists": True
                }
            else:
                return {"exists": False}
        except Exception as e:
            return {"exists": False, "error": str(e)}


class ConfigManager:
    """Clase para gestionar configuración de la aplicación"""
    
    CONFIG_FILE = "qr_app_config.json"
    
    @staticmethod
    def load_config():
        """
        Carga la configuración de la aplicación
        
        Returns:
            dict: Configuración cargada
        """
        import json
        
        default_config = {
            "theme": "dark",
            "default_save_location": "",
            "recent_files": [],
            "window_size": "800x600",
            "auto_save_examples": False
        }
        
        try:
            if os.path.exists(ConfigManager.CONFIG_FILE):
                with open(ConfigManager.CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Combinar con valores por defecto
                    default_config.update(config)
            return default_config
        except Exception:
            return default_config
    
    @staticmethod
    def save_config(config):
        """
        Guarda la configuración de la aplicación
        
        Args:
            config (dict): Configuración a guardar
        """
        import json
        
        try:
            with open(ConfigManager.CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
    
    @staticmethod
    def add_recent_file(file_path, max_recent=5):
        """
        Agrega un archivo a la lista de recientes
        
        Args:
            file_path (str): Ruta del archivo
            max_recent (int): Número máximo de archivos recientes
        """
        config = ConfigManager.load_config()
        recent = config.get("recent_files", [])
        
        # Remover si ya existe
        if file_path in recent:
            recent.remove(file_path)
            
        # Agregar al inicio
        recent.insert(0, file_path)
        
        # Limitar cantidad
        recent = recent[:max_recent]
        
        config["recent_files"] = recent
        ConfigManager.save_config(config)