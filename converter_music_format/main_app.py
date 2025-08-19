"""
Aplicación principal del Conversor de Audio Universal
Clase principal que coordina todos los componentes
"""

import os
import customtkinter as ctk
from tkinter import messagebox

from config import setup_theme, APP_TITLE, APP_GEOMETRY, APP_ICON, UI_CONFIG, COLORS, MESSAGES
from audio_converter import AudioConverter
from ffmpeg_manager import FFmpegManager
from ui_components import SingleFileTab, BatchTab, InfoTab
from conversion_handlers import ConversionHandlers


class AudioConverterGUI:
    """
    Clase principal de la interfaz gráfica del conversor de audio
    """
    
    def __init__(self):
        """Inicializar la aplicación"""
        # Configurar tema
        setup_theme()
        
        # Inicializar ventana principal
        self.root = ctk.CTk()
        self.root.title(APP_TITLE)
        self.root.geometry(APP_GEOMETRY)
        self.root.resizable(True, True)
        
        # Configurar icono de la aplicación
        self._set_app_icon()
        
        # Inicializar componentes
        self.converter = AudioConverter()
        self.ffmpeg_manager = FFmpegManager(self.root)
        self.conversion_handlers = ConversionHandlers(self)
        
        # Variables para almacenar rutas
        self._initialize_variables()
        
        # Verificar FFmpeg al iniciar
        self.ffmpeg_manager.check_and_setup_ffmpeg()
        
        # Configurar interfaz
        self.setup_ui()
    
    def _set_app_icon(self):
        """Configurar el icono de la aplicación"""
        try:
            icon_path = os.path.join(os.path.dirname(__file__), APP_ICON)
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
            else:
                print(f"Icono no encontrado en: {icon_path}")
        except Exception as e:
            print(f"Error configurando icono: {e}")
    
    def _initialize_variables(self):
        """Inicializar variables de la aplicación"""
        self.single_file_path = ctk.StringVar()
        self.batch_folder_path = ctk.StringVar()
        self.output_folder_path = ctk.StringVar()
        self.single_format_var = None
        self.batch_format_var = None
        self.include_subfolders = None
        
        # Referencias a elementos UI (se inicializan en setup_ui)
        self.single_file_entry = None
        self.batch_folder_entry = None
        self.single_output_entry = None
        self.progress_bar = None
        self.status_label = None
        self.tabview = None
    
    def setup_ui(self):
        """Configurar la interfaz de usuario principal"""
        # Frame principal con scroll
        main_frame = ctk.CTkScrollableFrame(
            self.root, 
            corner_radius=UI_CONFIG['main_frame_corner_radius']
        )
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título principal
        self._create_title(main_frame)
        
        # Crear pestañas
        self._create_tabs(main_frame)
        
        # Barra de progreso y estado
        self._create_progress_section(main_frame)
    
    def _create_title(self, parent):
        """Crear el título principal"""
        title_label = ctk.CTkLabel(
            parent, 
            text="Conversor de Audio Universal", 
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=COLORS['primary_green']
        )
        title_label.pack(pady=(0, 30))
    
    def _create_tabs(self, parent):
        """Crear las pestañas de la aplicación"""
        self.tabview = ctk.CTkTabview(
            parent, 
            width=UI_CONFIG['tab_width'], 
            height=UI_CONFIG['tab_height']
        )
        self.tabview.pack(fill="both", expand=True, pady=10)
        
        # Crear pestañas
        tab_single = self.tabview.add("📄 Archivo Individual")
        tab_batch = self.tabview.add("📁 Conversión por Lotes")
        tab_info = self.tabview.add("ℹ️ Información")
        
        # Inicializar componentes de pestañas
        self.single_tab = SingleFileTab(tab_single, self)
        self.batch_tab = BatchTab(tab_batch, self)
        self.info_tab = InfoTab(tab_info, self)
    
    def _create_progress_section(self, parent):
        """Crear la sección de progreso y estado"""
        # Barra de progreso global
        self.progress_bar = ctk.CTkProgressBar(
            parent, 
            width=UI_CONFIG['progress_bar_width']
        )
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        
        # Label de estado
        self.status_label = ctk.CTkLabel(
            parent, 
            text=MESSAGES['ready'],
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=5)
    
    def update_status(self, message):
        """
        Actualizar el mensaje de estado
        
        Args:
            message (str): Mensaje a mostrar
        """
        self.status_label.configure(text=message)
        self.root.update_idletasks()
    
    def convert_single_file(self):
        """Delegar conversión de archivo individual"""
        self.conversion_handlers.convert_single_file()
    
    def convert_batch_files(self):
        """Delegar conversión por lotes"""
        self.conversion_handlers.convert_batch_files()
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()


def main():
    """Función principal de la aplicación"""
    try:
        app = AudioConverterGUI()
        app.run()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error", f"Error al iniciar la aplicación:\n{e}")


if __name__ == "__main__":
    main()