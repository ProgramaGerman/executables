"""
Manejadores de conversión para el Conversor de Audio Universal
Contiene la lógica para manejar las conversiones individuales y por lotes
"""

import os
import threading
from tkinter import messagebox

from config import MESSAGES


class ConversionHandlers:
    """
    Clase que maneja las operaciones de conversión de audio
    """
    
    def __init__(self, app_instance):
        """
        Inicializar los manejadores de conversión
        
        Args:
            app_instance: Instancia de la aplicación principal
        """
        self.app = app_instance
    
    def convert_single_file(self):
        """Manejar la conversión de un archivo individual"""
        if not self.app.single_file_path.get():
            messagebox.showerror("Error", MESSAGES['select_file'])
            return
        
        def conversion_thread():
            try:
                self._execute_single_conversion()
            except Exception as e:
                self._handle_conversion_error(str(e))
        
        # Ejecutar conversión en hilo separado
        thread = threading.Thread(target=conversion_thread)
        thread.daemon = True
        thread.start()
    
    def _execute_single_conversion(self):
        """Ejecutar la conversión de archivo individual"""
        try:
            # Inicializar progreso
            self.app.progress_bar.set(0.2)
            self.app.update_status(MESSAGES['conversion_started'])
            
            # Obtener parámetros
            input_file = self.app.single_file_path.get()
            output_format = self.app.single_format_var.get()
            output_dir = self.app.output_folder_path.get() if self.app.output_folder_path.get() else None
            
            # Actualizar progreso
            self.app.progress_bar.set(0.5)
            self.app.update_status(MESSAGES['converting_file'])
            
            # Realizar conversión
            success, result = self.app.converter.convert_audio_file(
                input_file, output_format, output_dir
            )
            
            # Finalizar
            self.app.progress_bar.set(1.0)
            
            if success:
                self._handle_single_conversion_success(result)
            else:
                self._handle_single_conversion_error(result)
            
            self.app.progress_bar.set(0)
            
        except Exception as e:
            self._handle_conversion_error(str(e))
    
    def _handle_single_conversion_success(self, result_path):
        """Manejar el éxito de conversión individual"""
        self.app.update_status(MESSAGES['conversion_success'])
        messagebox.showinfo("Éxito", f"Archivo convertido exitosamente:\n{result_path}")
    
    def _handle_single_conversion_error(self, error_message):
        """Manejar error de conversión individual"""
        self.app.update_status(MESSAGES['conversion_error'])
        messagebox.showerror("Error", f"Error durante la conversión:\n{error_message}")
    
    def convert_batch_files(self):
        """Manejar la conversión por lotes"""
        if not self.app.batch_folder_path.get():
            messagebox.showerror("Error", MESSAGES['select_folder'])
            return
        
        def batch_conversion_thread():
            try:
                self._execute_batch_conversion()
            except Exception as e:
                self._handle_batch_conversion_error(str(e))
        
        # Ejecutar conversión en hilo separado
        thread = threading.Thread(target=batch_conversion_thread)
        thread.daemon = True
        thread.start()
    
    def _execute_batch_conversion(self):
        """Ejecutar la conversión por lotes"""
        try:
            # Obtener parámetros
            input_dir = self.app.batch_folder_path.get()
            output_format = self.app.batch_format_var.get()
            include_sub = self.app.include_subfolders.get()
            
            # Validar directorio
            if not os.path.exists(input_dir):
                messagebox.showerror("Error", MESSAGES['folder_not_exists'])
                return
            
            # Buscar archivos de audio
            self.app.update_status(MESSAGES['searching_files'])
            audio_files = self.app.converter.find_audio_files(input_dir, include_sub)
            
            if not audio_files:
                messagebox.showwarning("Advertencia", MESSAGES['no_audio_files'])
                return
            
            # Realizar conversión por lotes
            stats = self._process_batch_files(audio_files, output_format)
            
            # Mostrar resultados
            self._show_batch_results(stats)
            
        except Exception as e:
            self._handle_batch_conversion_error(str(e))
    
    def _process_batch_files(self, audio_files, output_format):
        """Procesar archivos en lote"""
        total_files = len(audio_files)
        converted = 0
        failed = 0
        
        for i, file_path in enumerate(audio_files):
            # Actualizar progreso
            progress = (i + 1) / total_files
            self.app.progress_bar.set(progress)
            
            file_name = os.path.basename(file_path)
            self.app.update_status(f"Convirtiendo {i+1}/{total_files}: {file_name}")
            
            # Convertir archivo
            success, result = self.app.converter.convert_audio_file(file_path, output_format)
            
            if success:
                converted += 1
            else:
                failed += 1
                print(f"Error convirtiendo {file_path}: {result}")
        
        return {'converted': converted, 'failed': failed, 'total': total_files}
    
    def _show_batch_results(self, stats):
        """Mostrar resultados de conversión por lotes"""
        self.app.progress_bar.set(1.0)
        self.app.update_status(MESSAGES['batch_completed'])
        
        result_message = (
            f"Conversión por lotes finalizada:\n\n"
            f"✅ Archivos convertidos: {stats['converted']}\n"
            f"❌ Archivos fallidos: {stats['failed']}\n"
            f"📁 Total procesados: {stats['total']}"
        )
        
        messagebox.showinfo("Conversión Completada", result_message)
        self.app.progress_bar.set(0)
    
    def _handle_conversion_error(self, error_message):
        """Manejar errores generales de conversión"""
        self.app.progress_bar.set(0)
        self.app.update_status(MESSAGES['conversion_error'])
        messagebox.showerror("Error", f"Error inesperado:\n{error_message}")
    
    def _handle_batch_conversion_error(self, error_message):
        """Manejar errores de conversión por lotes"""
        self.app.progress_bar.set(0)
        self.app.update_status(MESSAGES['batch_error'])
        messagebox.showerror("Error", f"Error durante la conversión por lotes:\n{error_message}")


class ProgressCallback:
    """
    Clase para manejar callbacks de progreso durante las conversiones
    """
    
    def __init__(self, app_instance):
        """
        Inicializar el callback de progreso
        
        Args:
            app_instance: Instancia de la aplicación principal
        """
        self.app = app_instance
    
    def update_progress(self, current, total, current_file):
        """
        Actualizar el progreso de la conversión
        
        Args:
            current (int): Archivo actual
            total (int): Total de archivos
            current_file (str): Nombre del archivo actual
        """
        progress = current / total if total > 0 else 0
        self.app.progress_bar.set(progress)
        
        status_message = f"Convirtiendo {current}/{total}: {current_file}"
        self.app.update_status(status_message)
    
    def reset_progress(self):
        """Resetear la barra de progreso"""
        self.app.progress_bar.set(0)
        self.app.update_status(MESSAGES['ready'])