"""
Componentes de interfaz de usuario para el Conversor de Audio Universal
Contiene las clases para crear las pestañas y elementos de la GUI
"""

import os
import customtkinter as ctk
from tkinter import filedialog

from config import COLORS, UI_CONFIG, FILE_TYPES, INFO_TEXT


class SingleFileTab:
    """Pestaña para conversión de archivos individuales"""
    
    def __init__(self, parent_tab, app_instance):
        """
        Inicializar la pestaña de archivo individual
        
        Args:
            parent_tab: Pestaña padre donde agregar los elementos
            app_instance: Instancia de la aplicación principal
        """
        self.parent_tab = parent_tab
        self.app = app_instance
        self.setup_tab()
    
    def setup_tab(self):
        """Configurar todos los elementos de la pestaña"""
        self._create_file_selection_frame()
        self._create_configuration_frame()
    
    def _create_file_selection_frame(self):
        """Crear el frame para selección de archivo"""
        file_frame = ctk.CTkFrame(self.parent_tab, corner_radius=UI_CONFIG['main_frame_corner_radius'])
        file_frame.pack(fill="x", padx=20, pady=20)
        
        # Título de sección
        ctk.CTkLabel(
            file_frame, 
            text="📄 Seleccionar Archivo de Audio",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLORS['primary_green']
        ).pack(pady=(15, 10))
        
        # Frame para entrada de archivo
        input_frame = ctk.CTkFrame(file_frame, fg_color="transparent")
        input_frame.pack(fill="x", padx=20, pady=10)
        
        self.app.single_file_entry = ctk.CTkEntry(
            input_frame, 
            textvariable=self.app.single_file_path,
            placeholder_text="Selecciona un archivo de audio...",
            width=500,
            height=UI_CONFIG['entry_height']
        )
        self.app.single_file_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        browse_btn = ctk.CTkButton(
            input_frame,
            text="📁 Examinar",
            command=self.browse_single_file,
            width=UI_CONFIG['button_width'],
            height=UI_CONFIG['button_height'],
            fg_color=COLORS['secondary_green'],
            hover_color=COLORS['hover_green']
        )
        browse_btn.pack(side="right")
    
    def _create_configuration_frame(self):
        """Crear el frame de configuración"""
        config_frame = ctk.CTkFrame(self.parent_tab, corner_radius=UI_CONFIG['main_frame_corner_radius'])
        config_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(
            config_frame, 
            text="⚙️ Configuración de Conversión",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLORS['primary_green']
        ).pack(pady=(15, 10))
        
        self._create_format_selection(config_frame)
        self._create_output_directory_selection(config_frame)
        self._create_convert_button(config_frame)
    
    def _create_format_selection(self, parent):
        """Crear selector de formato"""
        format_frame = ctk.CTkFrame(parent, fg_color="transparent")
        format_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(format_frame, text="Formato de salida:", font=ctk.CTkFont(size=14)).pack(side="left", padx=(0, 10))
        
        self.app.single_format_var = ctk.StringVar(value="mp3")
        format_menu = ctk.CTkOptionMenu(
            format_frame,
            variable=self.app.single_format_var,
            values=self.app.converter.supported_formats,
            width=150,
            fg_color=COLORS['secondary_green'],
            button_color=COLORS['hover_green'],
            button_hover_color=COLORS['button_green']
        )
        format_menu.pack(side="left")
    
    def _create_output_directory_selection(self, parent):
        """Crear selector de directorio de salida"""
        output_frame = ctk.CTkFrame(parent, fg_color="transparent")
        output_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(output_frame, text="Carpeta de destino:", font=ctk.CTkFont(size=14)).pack(anchor="w", pady=(0, 5))
        
        output_entry_frame = ctk.CTkFrame(output_frame, fg_color="transparent")
        output_entry_frame.pack(fill="x")
        
        self.app.single_output_entry = ctk.CTkEntry(
            output_entry_frame,
            textvariable=self.app.output_folder_path,
            placeholder_text="Misma carpeta del archivo original",
            width=400,
            height=UI_CONFIG['entry_height']
        )
        self.app.single_output_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        output_browse_btn = ctk.CTkButton(
            output_entry_frame,
            text="📁 Examinar",
            command=self.browse_output_folder,
            width=UI_CONFIG['button_width'],
            height=UI_CONFIG['button_height'],
            fg_color=COLORS['secondary_green'],
            hover_color=COLORS['hover_green']
        )
        output_browse_btn.pack(side="right")
    
    def _create_convert_button(self, parent):
        """Crear botón de conversión"""
        convert_btn = ctk.CTkButton(
            parent,
            text="🔄 Convertir Archivo",
            command=self.app.convert_single_file,
            width=200,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=COLORS['button_green'],
            hover_color=COLORS['button_hover']
        )
        convert_btn.pack(pady=20)
    
    def browse_single_file(self):
        """Abrir diálogo para seleccionar archivo individual"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de audio",
            filetypes=FILE_TYPES
        )
        
        if filename:
            self.app.single_file_path.set(filename)
    
    def browse_output_folder(self):
        """Abrir diálogo para seleccionar carpeta de destino"""
        folder = filedialog.askdirectory(title="Seleccionar carpeta de destino")
        
        if folder:
            self.app.output_folder_path.set(folder)


class BatchTab:
    """Pestaña para conversión por lotes"""
    
    def __init__(self, parent_tab, app_instance):
        """
        Inicializar la pestaña de conversión por lotes
        
        Args:
            parent_tab: Pestaña padre donde agregar los elementos
            app_instance: Instancia de la aplicación principal
        """
        self.parent_tab = parent_tab
        self.app = app_instance
        self.setup_tab()
    
    def setup_tab(self):
        """Configurar todos los elementos de la pestaña"""
        self._create_folder_selection_frame()
        self._create_batch_configuration_frame()
    
    def _create_folder_selection_frame(self):
        """Crear el frame para selección de carpeta"""
        folder_frame = ctk.CTkFrame(self.parent_tab, corner_radius=UI_CONFIG['main_frame_corner_radius'])
        folder_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(
            folder_frame, 
            text="📁 Seleccionar Carpeta con Archivos de Audio",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLORS['primary_green']
        ).pack(pady=(15, 10))
        
        # Frame para entrada de carpeta
        batch_input_frame = ctk.CTkFrame(folder_frame, fg_color="transparent")
        batch_input_frame.pack(fill="x", padx=20, pady=10)
        
        self.app.batch_folder_entry = ctk.CTkEntry(
            batch_input_frame,
            textvariable=self.app.batch_folder_path,
            placeholder_text="Selecciona una carpeta con archivos de audio...",
            width=500,
            height=UI_CONFIG['entry_height']
        )
        self.app.batch_folder_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        batch_browse_btn = ctk.CTkButton(
            batch_input_frame,
            text="📁 Examinar",
            command=self.browse_batch_folder,
            width=UI_CONFIG['button_width'],
            height=UI_CONFIG['button_height'],
            fg_color=COLORS['secondary_green'],
            hover_color=COLORS['hover_green']
        )
        batch_browse_btn.pack(side="right")
    
    def _create_batch_configuration_frame(self):
        """Crear el frame de configuración por lotes"""
        batch_config_frame = ctk.CTkFrame(self.parent_tab, corner_radius=UI_CONFIG['main_frame_corner_radius'])
        batch_config_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(
            batch_config_frame, 
            text="⚙️ Configuración de Conversión por Lotes",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLORS['primary_green']
        ).pack(pady=(15, 10))
        
        self._create_batch_format_selection(batch_config_frame)
        self._create_subfolder_option(batch_config_frame)
        self._create_batch_convert_button(batch_config_frame)
    
    def _create_batch_format_selection(self, parent):
        """Crear selector de formato para lotes"""
        batch_format_frame = ctk.CTkFrame(parent, fg_color="transparent")
        batch_format_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(batch_format_frame, text="Formato de salida:", font=ctk.CTkFont(size=14)).pack(side="left", padx=(0, 10))
        
        self.app.batch_format_var = ctk.StringVar(value="mp3")
        batch_format_menu = ctk.CTkOptionMenu(
            batch_format_frame,
            variable=self.app.batch_format_var,
            values=self.app.converter.supported_formats,
            width=150,
            fg_color=COLORS['secondary_green'],
            button_color=COLORS['hover_green'],
            button_hover_color=COLORS['button_green']
        )
        batch_format_menu.pack(side="left")
    
    def _create_subfolder_option(self, parent):
        """Crear checkbox para incluir subcarpetas"""
        self.app.include_subfolders = ctk.BooleanVar(value=True)
        subfolder_check = ctk.CTkCheckBox(
            parent,
            text="Incluir subcarpetas",
            variable=self.app.include_subfolders,
            font=ctk.CTkFont(size=14),
            checkbox_width=20,
            checkbox_height=20
        )
        subfolder_check.pack(padx=20, pady=10, anchor="w")
    
    def _create_batch_convert_button(self, parent):
        """Crear botón de conversión por lotes"""
        batch_convert_btn = ctk.CTkButton(
            parent,
            text="🔄 Convertir Todos los Archivos",
            command=self.app.convert_batch_files,
            width=250,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=COLORS['button_green'],
            hover_color=COLORS['button_hover']
        )
        batch_convert_btn.pack(pady=20)
    
    def browse_batch_folder(self):
        """Abrir diálogo para seleccionar carpeta para conversión por lotes"""
        folder = filedialog.askdirectory(title="Seleccionar carpeta con archivos de audio")
        
        if folder:
            self.app.batch_folder_path.set(folder)


class InfoTab:
    """Pestaña de información y ayuda"""
    
    def __init__(self, parent_tab, app_instance):
        """
        Inicializar la pestaña de información
        
        Args:
            parent_tab: Pestaña padre donde agregar los elementos
            app_instance: Instancia de la aplicación principal
        """
        self.parent_tab = parent_tab
        self.app = app_instance
        self.setup_tab()
    
    def setup_tab(self):
        """Configurar todos los elementos de la pestaña"""
        info_frame = ctk.CTkFrame(self.parent_tab, corner_radius=UI_CONFIG['main_frame_corner_radius'])
        info_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        ctk.CTkLabel(
            info_frame, 
            text="ℹ️ Información del Conversor",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLORS['primary_green']
        ).pack(pady=(20, 15))
        
        # Información sobre formatos soportados
        ctk.CTkLabel(
            info_frame,
            text=INFO_TEXT['formats'],
            font=ctk.CTkFont(size=14),
            justify="left"
        ).pack(pady=10, padx=20, anchor="w")
        
        # Información adicional
        ctk.CTkLabel(
            info_frame,
            text=INFO_TEXT['features'],
            font=ctk.CTkFont(size=12),
            justify="left"
        ).pack(pady=10, padx=20, anchor="w")