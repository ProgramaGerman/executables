"""
Módulo de componentes de interfaz de usuario
Contiene widgets y formularios reutilizables para la aplicación
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class FormComponents:
    """Clase con componentes de formulario reutilizables"""
    
    @staticmethod
    def create_title(parent, text, size=24):
        """Crea un título estilizado"""
        title = ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(size=size, weight="bold")
        )
        title.pack(pady=30)
        return title
    
    @staticmethod
    def create_form_frame(parent):
        """Crea un frame para formularios"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        return form_frame
    
    @staticmethod
    def create_labeled_entry(parent, label_text, placeholder="", show=None):
        """Crea una entrada con etiqueta"""
        ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, show=show)
        entry.pack(fill="x", padx=20, pady=(0, 10))
        return entry
    
    @staticmethod
    def create_labeled_textbox(parent, label_text, height=100):
        """Crea un textbox con etiqueta"""
        ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
        textbox = ctk.CTkTextbox(parent, height=height)
        textbox.pack(fill="x", padx=20, pady=(0, 20))
        return textbox
    
    @staticmethod
    def create_labeled_combobox(parent, label_text, values, default_value=None):
        """Crea un combobox con etiqueta"""
        ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        combo = ctk.CTkComboBox(parent, values=values)
        combo.pack(fill="x", padx=20, pady=(0, 10))
        if default_value:
            combo.set(default_value)
        return combo
    
    @staticmethod
    def create_labeled_slider(parent, label_text, from_value, to_value, default_value, steps=None):
        """Crea un slider con etiqueta"""
        ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        
        if steps:
            slider = ctk.CTkSlider(parent, from_=from_value, to=to_value, number_of_steps=steps)
        else:
            slider = ctk.CTkSlider(parent, from_=from_value, to=to_value)
            
        slider.pack(fill="x", padx=20, pady=(0, 5))
        slider.set(default_value)
        return slider
    
    @staticmethod
    def create_action_buttons(parent, back_command, generate_command):
        """Crea botones de acción (Volver y Generar)"""
        buttons_frame = ctk.CTkFrame(parent)
        buttons_frame.pack(fill="x", padx=20, pady=20)
        
        # Botón Volver
        back_btn = ctk.CTkButton(
            buttons_frame,
            text="⬅️ Volver al Menú",
            command=back_command,
            font=ctk.CTkFont(size=14),
            fg_color="gray",
            hover_color="darkgray"
        )
        back_btn.pack(side="left", padx=(0, 10))
        
        # Botón Generar
        generate_btn = ctk.CTkButton(
            buttons_frame,
            text="🎯 Generar QR",
            command=generate_command,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        generate_btn.pack(side="right", padx=(10, 0))
        
        return back_btn, generate_btn


class MenuComponents:
    """Clase con componentes específicos del menú"""
    
    @staticmethod
    def create_main_title(parent):
        """Crea el título principal de la aplicación"""
        title = ctk.CTkLabel(
            parent,
            text="🎯 Generador de Códigos QR",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title.pack(pady=(30, 40))
        
        subtitle = ctk.CTkLabel(
            parent,
            text="Selecciona el tipo de código QR que deseas generar",
            font=ctk.CTkFont(size=16)
        )
        subtitle.pack(pady=(0, 30))
        
        return title, subtitle
    
    @staticmethod
    def create_menu_buttons(parent, button_commands):
        """
        Crea los botones del menú principal
        
        Args:
            parent: Widget padre
            button_commands: Diccionario con {texto: comando} para cada botón
        """
        buttons_frame = ctk.CTkFrame(parent)
        buttons_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Configurar grid
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        # Lista de botones con sus posiciones
        buttons_config = [
            ("📝 Texto Simple", button_commands.get("text"), 0, 0),
            ("🌐 URL/Página Web", button_commands.get("url"), 0, 1),
            ("👤 Información de Contacto", button_commands.get("contact"), 1, 0),
            ("📶 Configuración WiFi", button_commands.get("wifi"), 1, 1),
            ("🎨 QR Personalizado", button_commands.get("custom"), 2, 0),
            ("📚 Ejemplos de Aprendizaje", button_commands.get("examples"), 2, 1),
        ]
        
        buttons = []
        for text, command, row, col in buttons_config:
            if command:  # Solo crear botón si hay comando
                btn = ctk.CTkButton(
                    buttons_frame,
                    text=text,
                    command=command,
                    font=ctk.CTkFont(size=16, weight="bold"),
                    height=60,
                    corner_radius=15
                )
                btn.grid(row=row, column=col, padx=15, pady=15, sticky="ew")
                buttons.append(btn)
        
        return buttons_frame, buttons
    
    @staticmethod
    def create_theme_controls(parent, theme_command):
        """Crea los controles de tema"""
        theme_frame = ctk.CTkFrame(parent)
        theme_frame.pack(fill="x", padx=40, pady=(10, 0))
        
        theme_label = ctk.CTkLabel(theme_frame, text="Tema de la aplicación:")
        theme_label.pack(side="left", padx=10, pady=10)
        
        theme_switch = ctk.CTkSwitch(
            theme_frame,
            text="Modo Oscuro",
            command=theme_command
        )
        theme_switch.pack(side="right", padx=10, pady=10)
        theme_switch.select()  # Activado por defecto
        
        return theme_frame, theme_switch


class ResultComponents:
    """Clase con componentes para mostrar resultados"""
    
    @staticmethod
    def create_result_title(parent, description):
        """Crea el título de resultado"""
        title = ctk.CTkLabel(
            parent,
            text="✅ Código QR Generado",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=20)
        
        desc_label = ctk.CTkLabel(
            parent,
            text=description,
            font=ctk.CTkFont(size=14)
        )
        desc_label.pack(pady=(0, 20))
        
        return title, desc_label
    
    @staticmethod
    def create_image_frame(parent):
        """Crea el frame para mostrar la imagen"""
        image_frame = ctk.CTkFrame(parent)
        image_frame.pack(fill="both", expand=True, padx=40, pady=20)
        return image_frame
    
    @staticmethod
    def display_qr_image(parent, qr_image, size=(300, 300)):
        """
        Muestra la imagen del QR en el frame
        
        Args:
            parent: Widget padre
            qr_image: Imagen PIL del QR
            size: Tupla con el tamaño de visualización
        """
        try:
            # Redimensionar imagen para mostrar
            qr_display = qr_image.resize(size, Image.Resampling.NEAREST)
            
            # Convertir a PhotoImage
            photo = ImageTk.PhotoImage(qr_display)
            
            # Crear label para mostrar la imagen
            image_label = tk.Label(parent, image=photo, bg=parent.cget("fg_color")[1])
            image_label.image = photo  # Mantener referencia
            image_label.pack(expand=True)
            
            return image_label
            
        except Exception as e:
            error_label = ctk.CTkLabel(parent, text=f"Error al mostrar imagen: {str(e)}")
            error_label.pack(expand=True)
            return error_label
    
    @staticmethod
    def create_result_buttons(parent, back_command, save_command):
        """Crea los botones de resultado (Volver y Guardar)"""
        buttons_frame = ctk.CTkFrame(parent)
        buttons_frame.pack(fill="x", padx=40, pady=20)
        
        # Botón Volver
        back_btn = ctk.CTkButton(
            buttons_frame,
            text="⬅️ Volver al Menú",
            command=back_command,
            font=ctk.CTkFont(size=14),
            fg_color="gray",
            hover_color="darkgray"
        )
        back_btn.pack(side="left", padx=(0, 10))
        
        # Botón Guardar Como
        save_btn = ctk.CTkButton(
            buttons_frame,
            text="💾 Guardar Como...",
            command=save_command,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        save_btn.pack(side="right", padx=(10, 0))
        
        return buttons_frame, back_btn, save_btn


class ValidationUtils:
    """Utilidades para validación de formularios"""
    
    @staticmethod
    def validate_text_input(text, field_name="campo"):
        """Valida entrada de texto"""
        if not text or not text.strip():
            messagebox.showwarning("Advertencia", f"Por favor ingresa {field_name}")
            return False
        return True
    
    @staticmethod
    def validate_contact_fields(name, phone, email):
        """Valida campos de contacto"""
        if not all([name.strip(), phone.strip(), email.strip()]):
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos")
            return False
        return True
    
    @staticmethod
    def validate_url(url):
        """Valida y corrige URL"""
        if not url or not url.strip():
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL")
            return None
            
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            
        return url