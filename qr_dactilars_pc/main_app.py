"""
Aplicación principal modularizada para el generador de códigos QR
Interfaz gráfica moderna usando CustomTkinter
"""

import customtkinter as ctk
from tkinter import messagebox
import os
from PIL import Image, ImageTk


# Importar módulos locales
from ui_components import MenuComponents, ResultComponents
from forms import TextForm, URLForm, ContactForm, WiFiForm, CustomForm
from file_manager import FileManager, ConfigManager
from qr_generator import QRGenerator


class QRGeneratorApp:
    """Aplicación principal del generador de códigos QR"""

    def __init__(self):
        # Cargar configuración
        self.config = ConfigManager.load_config()
        
        # Configuración de CustomTkinter
        ctk.set_appearance_mode(self.config.get("theme", "dark"))
        ctk.set_default_color_theme("blue")
        

        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Generador de Códigos QR - Interfaz Moderna")
        self.root.geometry(self.config.get("window_size", "800x600"))
        self.root.resizable(True, True)
        
        # Configurar icono de la aplicación
        self.setup_icon()
        
        # Variables de estado
        self.current_qr_image = None
        self.current_page = "menu"
        
        # Configurar eventos de cierre
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Crear la interfaz
        self.setup_ui()
        
    def setup_icon(self):
        """Configura el icono de la aplicación"""
        try:
            # Ruta al icono .ico (preferido para aplicaciones Windows)
            ico_path = os.path.join(os.path.dirname(__file__), "icons", "codigo-qr.ico")
            png_path = os.path.join(os.path.dirname(__file__), "icons", "codigo-qr.png")
            
            # Intentar usar el archivo .ico primero (más eficiente)
            if os.path.exists(ico_path):
                try:
                    # Configurar icono usando el archivo .ico nativo
                    self.root.iconbitmap(ico_path)
                    print("✅ Icono .ico configurado correctamente")
                    
                    # También configurar con wm_iconphoto para mejor compatibilidad
                    try:
                        from PIL import Image, ImageTk
                        icon_image = Image.open(ico_path)
                        icon_photo = ImageTk.PhotoImage(icon_image)
                        self.root.wm_iconphoto(True, icon_photo)
                        self.icon_photo = icon_photo
                    except Exception:
                        pass  # No es crítico si falla esta parte
                        
                except Exception as e:
                    print(f"⚠️ Advertencia: Error con archivo .ico: {e}")
                    # Fallback al PNG si el .ico falla
                    self._setup_png_icon(png_path)
                    
            elif os.path.exists(png_path):
                # Usar PNG como fallback
                self._setup_png_icon(png_path)
                
            else:
                print("⚠️ Advertencia: No se encontró ningún archivo de icono")
                
        except Exception as e:
            print(f"⚠️ Advertencia: Error al configurar el icono: {e}")
    
    def _setup_png_icon(self, png_path):
        """Configura el icono usando archivo PNG como fallback"""
        try:
            
            # Cargar la imagen del icono
            icon_image = Image.open(png_path)
            
            # Crear diferentes tamaños para mejor visualización
            small_icon = icon_image.resize((16, 16), Image.Resampling.LANCZOS)
            small_photo = ImageTk.PhotoImage(small_icon)
            
            medium_icon = icon_image.resize((32, 32), Image.Resampling.LANCZOS)
            medium_photo = ImageTk.PhotoImage(medium_icon)
            
            # Configurar iconos para la ventana
            self.root.wm_iconphoto(True, medium_photo, small_photo)
            
            # Mantener referencias para evitar garbage collection
            self.small_icon_photo = small_photo
            self.medium_icon_photo = medium_photo
            
            print("✅ Icono PNG configurado correctamente como fallback")
            
        except ImportError:
            print("⚠️ Advertencia: PIL no está disponible para configurar el icono PNG")
        except Exception as e:
            print(f"⚠️ Advertencia: No se pudo configurar el icono PNG: {e}")
        
    def setup_ui(self):
        """Configura la interfaz de usuario principal"""
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Mostrar página inicial (menú)
        self.show_menu()
        
    def clear_frame(self):
        """Limpia el frame principal"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
    def show_menu(self):
        """Muestra el menú principal con todas las opciones"""
        self.clear_frame()
        self.current_page = "menu"
        
        # Título principal
        MenuComponents.create_main_title(self.main_frame)
        
        # Configurar comandos de botones
        button_commands = {
            "text": self.show_text_form,
            "url": self.show_url_form,
            "contact": self.show_contact_form,
            "wifi": self.show_wifi_form,
            "custom": self.show_custom_form,
            "examples": self.generate_examples
        }
        
        # Crear botones del menú
        MenuComponents.create_menu_buttons(self.main_frame, button_commands)
        
        # Controles de tema
        theme_frame, self.theme_switch = MenuComponents.create_theme_controls(
            self.main_frame, 
            self.toggle_theme
        )
        
        # Configurar switch según configuración actual
        if self.config.get("theme", "dark") == "dark":
            self.theme_switch.select()
        else:
            self.theme_switch.deselect()
            
    def toggle_theme(self):
        """Cambia entre modo claro y oscuro"""
        if self.theme_switch.get():
            ctk.set_appearance_mode("dark")
            self.config["theme"] = "dark"
        else:
            ctk.set_appearance_mode("light")
            self.config["theme"] = "light"
            
        # Guardar configuración
        ConfigManager.save_config(self.config)
        
    def show_text_form(self):
        """Muestra el formulario para texto simple"""
        self.current_page = "text"
        form = TextForm(self.main_frame, self.show_menu, self.show_qr_result)
        form.create_form()
        
    def show_url_form(self):
        """Muestra el formulario para URL"""
        self.current_page = "url"
        form = URLForm(self.main_frame, self.show_menu, self.show_qr_result)
        form.create_form()
        
    def show_contact_form(self):
        """Muestra el formulario para contacto"""
        self.current_page = "contact"
        form = ContactForm(self.main_frame, self.show_menu, self.show_qr_result)
        form.create_form()
        
    def show_wifi_form(self):
        """Muestra el formulario para WiFi"""
        self.current_page = "wifi"
        form = WiFiForm(self.main_frame, self.show_menu, self.show_qr_result)
        form.create_form()
        
    def show_custom_form(self):
        """Muestra el formulario para QR personalizado"""
        self.current_page = "custom"
        form = CustomForm(self.main_frame, self.show_menu, self.show_qr_result)
        form.create_form()
        
    def generate_examples(self):
        """Genera ejemplos de códigos QR"""
        try:
            generated_files = FileManager.save_examples_batch()
            
            messagebox.showinfo(
                "Éxito", 
                f"✅ {len(generated_files)} ejemplos generados exitosamente en la carpeta 'ejemplos_qr'\n\n"
                f"Archivos creados:\n" + "\n".join([os.path.basename(f) for f in generated_files])
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar ejemplos: {str(e)}")
            
    def show_qr_result(self, qr_image, description):
        """
        Muestra el resultado del QR generado
        
        Args:
            qr_image: Imagen PIL del QR
            description: Descripción del QR
        """
        self.clear_frame()
        self.current_qr_image = qr_image
        
        # Título y descripción
        ResultComponents.create_result_title(self.main_frame, description)
        
        # Frame para la imagen
        image_frame = ResultComponents.create_image_frame(self.main_frame)
        
        # Mostrar imagen del QR
        ResultComponents.display_qr_image(image_frame, qr_image)
        
        # Botones de acción
        ResultComponents.create_result_buttons(
            self.main_frame,
            self.show_menu,
            self.save_qr_as
        )
        
    def save_qr_as(self):
        """Abre diálogo para guardar el QR"""
        if not self.current_qr_image:
            messagebox.showerror("Error", "No hay imagen QR para guardar", parent=self.root)
            return
            
        # Generar nombre por defecto basado en la página actual
        default_names = {
            "text": "qr_texto",
            "url": "qr_url", 
            "contact": "qr_contacto",
            "wifi": "qr_wifi",
            "custom": "qr_personalizado"
        }
        
        default_name = default_names.get(self.current_page, "qr_code")
        
        # Guardar archivo
        saved_path = FileManager.save_qr_dialog(self.current_qr_image, default_name, self.root)
        
        if saved_path:
            # Agregar a archivos recientes
            ConfigManager.add_recent_file(saved_path)
            
    def on_closing(self):
        """Maneja el evento de cierre de la aplicación"""
        # Guardar configuración de ventana
        self.config["window_size"] = self.root.geometry()
        ConfigManager.save_config(self.config)
        
        # Cerrar aplicación
        self.root.destroy()
        
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()


def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    try:
        import customtkinter
        import qrcode
        from PIL import Image
        return True
    except ImportError as e:
        print(f"❌ Error: Falta instalar dependencias: {e}")
        print("💡 Ejecuta: pip install customtkinter qrcode[pil]")
        return False


def main():
    """Función principal"""
    print("🚀 Iniciando el generador de códigos QR...")
    
    # Verificar dependencias
    if not check_dependencies():
        input("Presiona Enter para salir...")
        return
        
    try:
        # Crear y ejecutar aplicación
        app = QRGeneratorApp()
        app.run()
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        messagebox.showerror("Error Fatal", f"Error inesperado: {e}")


if __name__ == "__main__":
    main()