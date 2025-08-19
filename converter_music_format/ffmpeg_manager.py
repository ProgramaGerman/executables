"""
Gestor de FFmpeg para el Conversor de Audio Universal
Maneja la detección, descarga e instalación de FFmpeg
"""

import os
import sys
import threading
import subprocess
import urllib.request
import zipfile
import shutil
import webbrowser
from pathlib import Path
import customtkinter as ctk
from tkinter import messagebox

try:
    from pydub.utils import which
except ImportError:
    which = None

from config import FFMPEG_DOWNLOAD_URL, FFMPEG_WEBSITE, COLORS, MESSAGES


class FFmpegManager:
    """
    Clase para gestionar FFmpeg (detección, descarga e instalación)
    """
    
    def __init__(self, parent_window=None):
        """
        Inicializar el gestor de FFmpeg
        
        Args:
            parent_window: Ventana padre para los diálogos
        """
        self.parent_window = parent_window
        self.ffmpeg_paths = [
            os.path.join(os.getcwd(), "ffmpeg", "bin", "ffmpeg.exe"),
            os.path.join(os.path.expanduser("~"), "ffmpeg", "bin", "ffmpeg.exe"),
            "C:\\ffmpeg\\bin\\ffmpeg.exe"
        ]
    
    def is_ffmpeg_available(self):
        """
        Verificar si FFmpeg está disponible en el sistema
        
        Returns:
            bool: True si FFmpeg está disponible, False en caso contrario
        """
        try:
            # Verificar si ffmpeg está en el PATH
            if which and which("ffmpeg"):
                return True
            
            # Verificar en ubicaciones comunes
            for path in self.ffmpeg_paths:
                if os.path.exists(path):
                    # Agregar al PATH temporalmente
                    ffmpeg_dir = os.path.dirname(path)
                    if ffmpeg_dir not in os.environ["PATH"]:
                        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
                    return True
            
            return False
            
        except Exception as e:
            print(f"Error verificando FFmpeg: {e}")
            return False
    
    def check_and_setup_ffmpeg(self):
        """
        Verificar FFmpeg y mostrar diálogo de instalación si es necesario
        
        Returns:
            bool: True si FFmpeg está disponible, False en caso contrario
        """
        if self.is_ffmpeg_available():
            return True
        
        # Si no está disponible, mostrar diálogo de instalación
        if self.parent_window:
            self.show_ffmpeg_dialog()
        
        return False
    
    def show_ffmpeg_dialog(self):
        """Mostrar diálogo para instalar FFmpeg"""
        dialog = ctk.CTkToplevel(self.parent_window)
        dialog.title("FFmpeg Requerido")
        dialog.geometry("500x400")
        dialog.transient(self.parent_window)
        dialog.grab_set()
        
        # Centrar el diálogo
        self._center_window(dialog, 500, 400)
        
        # Contenido del diálogo
        self._setup_dialog_content(dialog)
    
    def _center_window(self, window, width, height):
        """Centrar una ventana en la pantalla"""
        window.update_idletasks()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def _setup_dialog_content(self, dialog):
        """Configurar el contenido del diálogo de FFmpeg"""
        # Título
        ctk.CTkLabel(
            dialog,
            text="⚠️ FFmpeg Requerido",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=COLORS['error_red']
        ).pack(pady=20)
        
        # Información
        ctk.CTkLabel(
            dialog,
            text=MESSAGES.get('ffmpeg_info', ''),
            font=ctk.CTkFont(size=12),
            justify="left"
        ).pack(pady=10, padx=20, fill="both", expand=True)
        
        # Botones
        self._setup_dialog_buttons(dialog)
    
    def _setup_dialog_buttons(self, dialog):
        """Configurar los botones del diálogo"""
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=20)
        
        # Botón de descarga automática
        download_btn = ctk.CTkButton(
            button_frame,
            text="🔽 Descargar FFmpeg",
            command=lambda: self.download_ffmpeg(dialog),
            width=150,
            height=35,
            fg_color=COLORS['secondary_green'],
            hover_color=COLORS['hover_green']
        )
        download_btn.pack(side="left", padx=10)
        
        # Botón de instalación manual
        manual_btn = ctk.CTkButton(
            button_frame,
            text="📖 Instalación Manual",
            command=self.open_ffmpeg_website,
            width=150,
            height=35,
            fg_color=COLORS['gray'],
            hover_color=COLORS['gray_hover']
        )
        manual_btn.pack(side="left", padx=10)
        
        # Botón continuar
        continue_btn = ctk.CTkButton(
            button_frame,
            text="✅ Continuar",
            command=dialog.destroy,
            width=100,
            height=35,
            fg_color=COLORS['button_green'],
            hover_color=COLORS['button_hover']
        )
        continue_btn.pack(side="left", padx=10)
    
    def download_ffmpeg(self, dialog):
        """
        Descargar e instalar FFmpeg automáticamente
        
        Args:
            dialog: Diálogo padre a cerrar
        """
        def download_thread():
            try:
                dialog.destroy()
                
                # Crear ventana de progreso
                progress_window = self._create_progress_window()
                
                # Realizar descarga
                self._perform_ffmpeg_download(progress_window)
                
            except Exception as e:
                if 'progress_window' in locals():
                    progress_window.destroy()
                messagebox.showerror(
                    "Error", 
                    MESSAGES['ffmpeg_error'].format(str(e))
                )
        
        # Ejecutar descarga en hilo separado
        thread = threading.Thread(target=download_thread)
        thread.daemon = True
        thread.start()
    
    def _create_progress_window(self):
        """Crear ventana de progreso para la descarga"""
        progress_window = ctk.CTkToplevel(self.parent_window)
        progress_window.title("Descargando FFmpeg")
        progress_window.geometry("400x150")
        progress_window.transient(self.parent_window)
        progress_window.grab_set()
        
        # Centrar ventana
        self._center_window(progress_window, 400, 150)
        
        # Elementos de la ventana
        progress_window.status_label = ctk.CTkLabel(
            progress_window, 
            text="Descargando FFmpeg..."
        )
        progress_window.status_label.pack(pady=20)
        
        progress_window.progress_bar = ctk.CTkProgressBar(progress_window, width=350)
        progress_window.progress_bar.pack(pady=10)
        progress_window.progress_bar.set(0)
        
        return progress_window
    
    def _perform_ffmpeg_download(self, progress_window):
        """Realizar la descarga e instalación de FFmpeg"""
        try:
            # Configurar rutas
            current_dir = os.getcwd()
            ffmpeg_dir = os.path.join(current_dir, "ffmpeg")
            zip_path = os.path.join(current_dir, "ffmpeg.zip")
            
            # Descargar archivo
            progress_window.status_label.configure(text="Descargando FFmpeg...")
            progress_window.progress_bar.set(0.3)
            progress_window.update()
            
            urllib.request.urlretrieve(FFMPEG_DOWNLOAD_URL, zip_path)
            
            # Extraer archivo
            progress_window.status_label.configure(text="Extrayendo archivos...")
            progress_window.progress_bar.set(0.6)
            progress_window.update()
            
            self._extract_ffmpeg(zip_path, current_dir, ffmpeg_dir)
            
            # Configurar PATH
            self._setup_ffmpeg_path(ffmpeg_dir)
            
            # Limpiar archivos temporales
            if os.path.exists(zip_path):
                os.remove(zip_path)
            
            # Finalizar
            progress_window.progress_bar.set(1.0)
            progress_window.status_label.configure(text="¡FFmpeg instalado correctamente!")
            progress_window.update()
            
            # Cerrar ventana después de 2 segundos
            progress_window.after(2000, progress_window.destroy)
            
            messagebox.showinfo("Éxito", MESSAGES['ffmpeg_success'])
            
        except Exception as e:
            raise e
    
    def _extract_ffmpeg(self, zip_path, extract_dir, target_dir):
        """Extraer el archivo ZIP de FFmpeg"""
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        # Encontrar la carpeta extraída y renombrarla
        for item in os.listdir(extract_dir):
            if item.startswith("ffmpeg-") and os.path.isdir(os.path.join(extract_dir, item)):
                extracted_path = os.path.join(extract_dir, item)
                if os.path.exists(target_dir):
                    shutil.rmtree(target_dir)
                os.rename(extracted_path, target_dir)
                break
    
    def _setup_ffmpeg_path(self, ffmpeg_dir):
        """Configurar FFmpeg en el PATH del sistema"""
        ffmpeg_bin = os.path.join(ffmpeg_dir, "bin")
        if ffmpeg_bin not in os.environ["PATH"]:
            os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]
    
    def open_ffmpeg_website(self):
        """Abrir el sitio web de FFmpeg en el navegador"""
        webbrowser.open(FFMPEG_WEBSITE)