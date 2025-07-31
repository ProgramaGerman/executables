"""
Módulo de formularios específicos
Contiene las clases para cada tipo de formulario de la aplicación
"""

import customtkinter as ctk
from ui_components import FormComponents, ValidationUtils
from qr_generator import QRGenerator


class BaseForm:
    """Clase base para todos los formularios"""
    
    def __init__(self, parent, back_command, result_callback):
        self.parent = parent
        self.back_command = back_command
        self.result_callback = result_callback
        self.form_frame = None
        
    def clear_parent(self):
        """Limpia el widget padre"""
        for widget in self.parent.winfo_children():
            widget.destroy()
            
    def create_form(self):
        """Método abstracto para crear el formulario"""
        raise NotImplementedError("Subclases deben implementar create_form")
        
    def generate_qr(self):
        """Método abstracto para generar el QR"""
        raise NotImplementedError("Subclases deben implementar generate_qr")


class TextForm(BaseForm):
    """Formulario para generar QR de texto simple"""
    
    def create_form(self):
        self.clear_parent()
        
        # Título
        FormComponents.create_title(self.parent, "📝 Generar QR de Texto Simple")
        
        # Formulario
        self.form_frame = FormComponents.create_form_frame(self.parent)
        
        # Campo de texto
        self.text_entry = FormComponents.create_labeled_textbox(
            self.form_frame, 
            "Texto para el QR:", 
            height=100
        )
        
        # Botones
        FormComponents.create_action_buttons(
            self.form_frame, 
            self.back_command, 
            self.generate_qr
        )
        
    def generate_qr(self):
        text = self.text_entry.get("1.0", "end-1c").strip()
        if ValidationUtils.validate_text_input(text, "un texto"):
            try:
                image = QRGenerator.generate_text_qr(text)
                self.result_callback(image, f"QR de texto: {text[:30]}...")
            except Exception as e:
                ValidationUtils.show_error("Error al generar QR", str(e))


class URLForm(BaseForm):
    """Formulario para generar QR de URL"""
    
    def create_form(self):
        self.clear_parent()
        
        FormComponents.create_title(self.parent, "🌐 Generar QR de URL")
        self.form_frame = FormComponents.create_form_frame(self.parent)
        
        self.url_entry = FormComponents.create_labeled_entry(
            self.form_frame,
            "URL:",
            "https://ejemplo.com"
        )
        
        FormComponents.create_action_buttons(
            self.form_frame,
            self.back_command,
            self.generate_qr
        )
        
    def generate_qr(self):
        url = ValidationUtils.validate_url(self.url_entry.get())
        if url:
            try:
                image = QRGenerator.generate_url_qr(url)
                self.result_callback(image, f"QR de URL: {url}")
            except Exception as e:
                ValidationUtils.show_error("Error al generar QR", str(e))


class ContactForm(BaseForm):
    """Formulario para generar QR de contacto"""
    
    def create_form(self):
        self.clear_parent()
        
        FormComponents.create_title(self.parent, "👤 Generar QR de Contacto")
        self.form_frame = FormComponents.create_form_frame(self.parent)
        
        # Campos del formulario
        self.nombre_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Nombre:", "Juan Pérez"
        )
        self.telefono_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Teléfono:", "+1234567890"
        )
        self.email_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Email:", "juan@email.com"
        )
        
        FormComponents.create_action_buttons(
            self.form_frame,
            self.back_command,
            self.generate_qr
        )
        
    def generate_qr(self):
        nombre = self.nombre_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if ValidationUtils.validate_contact_fields(nombre, telefono, email):
            try:
                image = QRGenerator.generate_contact_qr(nombre, telefono, email)
                self.result_callback(image, f"QR de contacto: {nombre}")
            except Exception as e:
                ValidationUtils.show_error("Error al generar QR", str(e))


class WiFiForm(BaseForm):
    """Formulario para generar QR de WiFi"""
    
    def create_form(self):
        self.clear_parent()
        
        FormComponents.create_title(self.parent, "📶 Generar QR de WiFi")
        self.form_frame = FormComponents.create_form_frame(self.parent)
        
        self.ssid_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Nombre de la red (SSID):", "MiWiFi"
        )
        self.password_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Contraseña:", "contraseña123", show="*"
        )
        self.security_combo = FormComponents.create_labeled_combobox(
            self.form_frame, 
            "Tipo de seguridad:", 
            ["WPA", "WEP", "nopass"], 
            "WPA"
        )
        
        FormComponents.create_action_buttons(
            self.form_frame,
            self.back_command,
            self.generate_qr
        )
        
    def generate_qr(self):
        ssid = self.ssid_entry.get().strip()
        password = self.password_entry.get().strip()
        security = self.security_combo.get()
        
        if ValidationUtils.validate_text_input(ssid, "el nombre de la red"):
            try:
                image = QRGenerator.generate_wifi_qr(ssid, password, security)
                self.result_callback(image, f"QR de WiFi: {ssid}")
            except Exception as e:
                ValidationUtils.show_error("Error al generar QR", str(e))


class CustomForm(BaseForm):
    """Formulario para generar QR personalizado"""
    
    def create_form(self):
        self.clear_parent()
        
        FormComponents.create_title(self.parent, "🎨 Generar QR Personalizado")
        self.form_frame = FormComponents.create_form_frame(self.parent)
        
        # Texto
        self.custom_text_entry = FormComponents.create_labeled_entry(
            self.form_frame, "Texto:", "Texto personalizado"
        )
        
        # Frame para colores
        colors_frame = ctk.CTkFrame(self.form_frame)
        colors_frame.pack(fill="x", padx=20, pady=10)
        
        # Color del QR
        self.fill_color_combo = FormComponents.create_labeled_combobox(
            colors_frame,
            "Color del QR:",
            ["black", "blue", "red", "green", "purple", "orange", "brown"],
            "black"
        )
        
        # Color de fondo
        self.back_color_combo = FormComponents.create_labeled_combobox(
            colors_frame,
            "Color de fondo:",
            ["white", "yellow", "lightblue", "lightgreen", "pink", "lightgray"],
            "white"
        )
        
        # Tamaño
        self.size_slider = FormComponents.create_labeled_slider(
            self.form_frame, "Tamaño:", 5, 20, 10, 15
        )
        
        self.size_label = ctk.CTkLabel(self.form_frame, text="Tamaño: 10")
        self.size_label.pack(pady=(0, 20))
        self.size_slider.configure(command=self.update_size_label)
        
        FormComponents.create_action_buttons(
            self.form_frame,
            self.back_command,
            self.generate_qr
        )
        
    def update_size_label(self, value):
        """Actualiza la etiqueta del tamaño"""
        self.size_label.configure(text=f"Tamaño: {int(value)}")
        
    def generate_qr(self):
        text = self.custom_text_entry.get().strip()
        if ValidationUtils.validate_text_input(text, "un texto"):
            try:
                fill_color = self.fill_color_combo.get()
                back_color = self.back_color_combo.get()
                size = int(self.size_slider.get())
                
                image = QRGenerator.generate_custom_qr(text, fill_color, back_color, size)
                self.result_callback(image, f"QR personalizado: {text[:30]}...")
            except Exception as e:
                ValidationUtils.show_error("Error al generar QR", str(e))


# Agregar método de error a ValidationUtils
def show_error(title, message):
    """Muestra un mensaje de error"""
    from tkinter import messagebox
    messagebox.showerror(title, message)

# Agregar el método a la clase
ValidationUtils.show_error = staticmethod(show_error)