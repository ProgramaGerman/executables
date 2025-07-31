"""
Interfaz gráfica moderna para el generador de códigos QR
Usando CustomTkinter para una apariencia elegante y moderna
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os
import io


class QRGeneratorApp:
    def __init__(self):
        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")  # Modo oscuro por defecto
        ctk.set_default_color_theme("blue")  # Tema azul
        
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("🎯 Generador de Códigos QR - Interfaz Moderna")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Variables para almacenar datos
        self.current_qr_image = None
        self.current_page = "menu"
        
        # Crear la interfaz
        self.setup_ui()
        
    def setup_ui(self):
        """Configura la interfaz de usuario"""
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
        title = ctk.CTkLabel(
            self.main_frame,
            text="🎯 Generador de Códigos QR",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title.pack(pady=(30, 40))
        
        # Subtítulo
        subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Selecciona el tipo de código QR que deseas generar",
            font=ctk.CTkFont(size=16)
        )
        subtitle.pack(pady=(0, 30))
        
        # Frame para los botones
        buttons_frame = ctk.CTkFrame(self.main_frame)
        buttons_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Configurar grid para los botones
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        # Botones del menú
        buttons = [
            ("📝 Texto Simple", self.show_text_form, 0, 0),
            ("🌐 URL/Página Web", self.show_url_form, 0, 1),
            ("👤 Información de Contacto", self.show_contact_form, 1, 0),
            ("📶 Configuración WiFi", self.show_wifi_form, 1, 1),
            ("🎨 QR Personalizado", self.show_custom_form, 2, 0),
            ("📚 Ejemplos de Aprendizaje", self.generate_examples, 2, 1),
        ]
        
        for text, command, row, col in buttons:
            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                command=command,
                font=ctk.CTkFont(size=16, weight="bold"),
                height=60,
                corner_radius=15
            )
            btn.grid(row=row, column=col, padx=15, pady=15, sticky="ew")
            
        # Botón de configuración de tema
        theme_frame = ctk.CTkFrame(self.main_frame)
        theme_frame.pack(fill="x", padx=40, pady=(10, 0))
        
        theme_label = ctk.CTkLabel(theme_frame, text="Tema de la aplicación:")
        theme_label.pack(side="left", padx=10, pady=10)
        
        self.theme_switch = ctk.CTkSwitch(
            theme_frame,
            text="Modo Oscuro",
            command=self.toggle_theme
        )
        self.theme_switch.pack(side="right", padx=10, pady=10)
        self.theme_switch.select()  # Activado por defecto
        
    def toggle_theme(self):
        """Cambia entre modo claro y oscuro"""
        if self.theme_switch.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
            
    def show_text_form(self):
        """Muestra el formulario para texto simple"""
        self.clear_frame()
        self.current_page = "text"
        
        # Título
        title = ctk.CTkLabel(
            self.main_frame,
            text="📝 Generar QR de Texto Simple",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=30)
        
        # Formulario
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Campo de texto
        ctk.CTkLabel(form_frame, text="Texto para el QR:", font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
        self.text_entry = ctk.CTkTextbox(form_frame, height=100)
        self.text_entry.pack(fill="x", padx=20, pady=(0, 20))
        
        # Botones
        self.create_action_buttons(form_frame, self.generate_text_qr)
        
    def show_url_form(self):
        """Muestra el formulario para URL"""
        self.clear_frame()
        self.current_page = "url"
        
        title = ctk.CTkLabel(
            self.main_frame,
            text="🌐 Generar QR de URL",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=30)
        
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        ctk.CTkLabel(form_frame, text="URL:", font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
        self.url_entry = ctk.CTkEntry(form_frame, placeholder_text="https://ejemplo.com")
        self.url_entry.pack(fill="x", padx=20, pady=(0, 20))
        
        self.create_action_buttons(form_frame, self.generate_url_qr)
        
    def show_contact_form(self):
        """Muestra el formulario para contacto"""
        self.clear_frame()
        self.current_page = "contact"
        
        title = ctk.CTkLabel(
            self.main_frame,
            text="👤 Generar QR de Contacto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=30)
        
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Campos del formulario
        fields = [
            ("Nombre:", "nombre_entry", "Juan Pérez"),
            ("Teléfono:", "telefono_entry", "+1234567890"),
            ("Email:", "email_entry", "juan@email.com")
        ]
        
        for label_text, attr_name, placeholder in fields:
            ctk.CTkLabel(form_frame, text=label_text, font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
            entry = ctk.CTkEntry(form_frame, placeholder_text=placeholder)
            entry.pack(fill="x", padx=20, pady=(0, 10))
            setattr(self, attr_name, entry)
            
        self.create_action_buttons(form_frame, self.generate_contact_qr)
        
    def show_wifi_form(self):
        """Muestra el formulario para WiFi"""
        self.clear_frame()
        self.current_page = "wifi"
        
        title = ctk.CTkLabel(
            self.main_frame,
            text="📶 Generar QR de WiFi",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=30)
        
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Campos
        ctk.CTkLabel(form_frame, text="Nombre de la red (SSID):", font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
        self.ssid_entry = ctk.CTkEntry(form_frame, placeholder_text="MiWiFi")
        self.ssid_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="Contraseña:", font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        self.password_entry = ctk.CTkEntry(form_frame, placeholder_text="contraseña123", show="*")
        self.password_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="Tipo de seguridad:", font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        self.security_combo = ctk.CTkComboBox(form_frame, values=["WPA", "WEP", "nopass"])
        self.security_combo.pack(fill="x", padx=20, pady=(0, 20))
        self.security_combo.set("WPA")
        
        self.create_action_buttons(form_frame, self.generate_wifi_qr)
        
    def show_custom_form(self):
        """Muestra el formulario para QR personalizado"""
        self.clear_frame()
        self.current_page = "custom"
        
        title = ctk.CTkLabel(
            self.main_frame,
            text="🎨 Generar QR Personalizado",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=30)
        
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Texto
        ctk.CTkLabel(form_frame, text="Texto:", font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
        self.custom_text_entry = ctk.CTkEntry(form_frame, placeholder_text="Texto personalizado")
        self.custom_text_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Colores
        colors_frame = ctk.CTkFrame(form_frame)
        colors_frame.pack(fill="x", padx=20, pady=10)
        
        # Color del QR
        ctk.CTkLabel(colors_frame, text="Color del QR:", font=ctk.CTkFont(size=14)).pack(pady=(10, 5))
        self.fill_color_combo = ctk.CTkComboBox(
            colors_frame, 
            values=["black", "blue", "red", "green", "purple", "orange", "brown"]
        )
        self.fill_color_combo.pack(fill="x", padx=10, pady=(0, 10))
        self.fill_color_combo.set("black")
        
        # Color de fondo
        ctk.CTkLabel(colors_frame, text="Color de fondo:", font=ctk.CTkFont(size=14)).pack(pady=(10, 5))
        self.back_color_combo = ctk.CTkComboBox(
            colors_frame,
            values=["white", "yellow", "lightblue", "lightgreen", "pink", "lightgray"]
        )
        self.back_color_combo.pack(fill="x", padx=10, pady=(0, 10))
        self.back_color_combo.set("white")
        
        # Tamaño
        ctk.CTkLabel(form_frame, text="Tamaño:", font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
        self.size_slider = ctk.CTkSlider(form_frame, from_=5, to=20, number_of_steps=15)
        self.size_slider.pack(fill="x", padx=20, pady=(0, 5))
        self.size_slider.set(10)
        
        self.size_label = ctk.CTkLabel(form_frame, text="Tamaño: 10")
        self.size_label.pack(pady=(0, 20))
        self.size_slider.configure(command=self.update_size_label)
        
        self.create_action_buttons(form_frame, self.generate_custom_qr)
        
    def update_size_label(self, value):
        """Actualiza la etiqueta del tamaño"""
        self.size_label.configure(text=f"Tamaño: {int(value)}")
        
    def create_action_buttons(self, parent, generate_command):
        """Crea los botones de acción (Generar, Volver)"""
        buttons_frame = ctk.CTkFrame(parent)
        buttons_frame.pack(fill="x", padx=20, pady=20)
        
        # Botón Volver
        back_btn = ctk.CTkButton(
            buttons_frame,
            text="⬅️ Volver al Menú",
            command=self.show_menu,
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
        
    def generate_qr_base(self, data, fill_color="black", back_color="white", box_size=10):
        """Función base para generar códigos QR"""
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=box_size,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            image = qr.make_image(fill_color=fill_color, back_color=back_color)
            return image
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar QR: {str(e)}")
            return None
            
    def generate_text_qr(self):
        """Genera QR de texto simple"""
        text = self.text_entry.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Advertencia", "Por favor ingresa un texto")
            return
            
        image = self.generate_qr_base(text)
        if image:
            self.show_qr_result(image, f"QR de texto: {text[:30]}...")
            
    def generate_url_qr(self):
        """Genera QR de URL"""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL")
            return
            
        # Agregar https:// si no lo tiene
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            
        image = self.generate_qr_base(url)
        if image:
            self.show_qr_result(image, f"QR de URL: {url}")
            
    def generate_contact_qr(self):
        """Genera QR de contacto"""
        nombre = self.nombre_entry.get().strip()
        telefono = self.telefono_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if not all([nombre, telefono, email]):
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos")
            return
            
        # Formato vCard
        vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{nombre}
TEL:{telefono}
EMAIL:{email}
END:VCARD"""
        
        image = self.generate_qr_base(vcard)
        if image:
            self.show_qr_result(image, f"QR de contacto: {nombre}")
            
    def generate_wifi_qr(self):
        """Genera QR de WiFi"""
        ssid = self.ssid_entry.get().strip()
        password = self.password_entry.get().strip()
        security = self.security_combo.get()
        
        if not ssid:
            messagebox.showwarning("Advertencia", "Por favor ingresa el nombre de la red")
            return
            
        wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"
        
        image = self.generate_qr_base(wifi_config)
        if image:
            self.show_qr_result(image, f"QR de WiFi: {ssid}")
            
    def generate_custom_qr(self):
        """Genera QR personalizado"""
        text = self.custom_text_entry.get().strip()
        if not text:
            messagebox.showwarning("Advertencia", "Por favor ingresa un texto")
            return
            
        fill_color = self.fill_color_combo.get()
        back_color = self.back_color_combo.get()
        size = int(self.size_slider.get())
        
        image = self.generate_qr_base(text, fill_color, back_color, size)
        if image:
            self.show_qr_result(image, f"QR personalizado: {text[:30]}...")
            
    def generate_examples(self):
        """Genera ejemplos de códigos QR"""
        try:
            # Crear carpeta para ejemplos
            carpeta_ejemplos = "ejemplos_qr"
            if not os.path.exists(carpeta_ejemplos):
                os.makedirs(carpeta_ejemplos, exist_ok=True)
                
            examples = [
                ("¡Hola! Este es mi primer código QR", "ejemplo1_texto.png"),
                ("https://www.python.org", "ejemplo2_url.png"),
            ]
            
            # Generar ejemplos
            for text, filename in examples:
                image = self.generate_qr_base(text)
                if image:
                    image.save(os.path.join(carpeta_ejemplos, filename))
                    
            # Generar ejemplo de contacto
            vcard = """BEGIN:VCARD
VERSION:3.0
FN:Juan Pérez
TEL:+1234567890
EMAIL:juan@email.com
END:VCARD"""
            contact_image = self.generate_qr_base(vcard)
            if contact_image:
                contact_image.save(os.path.join(carpeta_ejemplos, "ejemplo3_contacto.png"))
                
            # Generar ejemplo de WiFi
            wifi_config = "WIFI:T:WPA;S:MiWiFi;P:contraseña123;;"
            wifi_image = self.generate_qr_base(wifi_config)
            if wifi_image:
                wifi_image.save(os.path.join(carpeta_ejemplos, "ejemplo4_wifi.png"))
                
            # Generar ejemplo personalizado
            custom_image = self.generate_qr_base("Código QR Colorido!", "purple", "lightblue", 12)
            if custom_image:
                custom_image.save(os.path.join(carpeta_ejemplos, "ejemplo5_colores.png"))
                
            messagebox.showinfo(
                "Éxito", 
                f"✅ Ejemplos generados exitosamente en la carpeta '{carpeta_ejemplos}'"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar ejemplos: {str(e)}")
            
    def show_qr_result(self, qr_image, description):
        """Muestra el resultado del QR generado"""
        self.clear_frame()
        self.current_qr_image = qr_image
        
        # Título
        title = ctk.CTkLabel(
            self.main_frame,
            text="✅ Código QR Generado",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=20)
        
        # Descripción
        desc_label = ctk.CTkLabel(
            self.main_frame,
            text=description,
            font=ctk.CTkFont(size=14)
        )
        desc_label.pack(pady=(0, 20))
        
        # Frame para la imagen
        image_frame = ctk.CTkFrame(self.main_frame)
        image_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Mostrar imagen del QR
        self.display_qr_image(image_frame, qr_image)
        
        # Botones de acción
        buttons_frame = ctk.CTkFrame(self.main_frame)
        buttons_frame.pack(fill="x", padx=40, pady=20)
        
        # Botón Volver
        back_btn = ctk.CTkButton(
            buttons_frame,
            text="⬅️ Volver al Menú",
            command=self.show_menu,
            font=ctk.CTkFont(size=14),
            fg_color="gray",
            hover_color="darkgray"
        )
        back_btn.pack(side="left", padx=(0, 10))
        
        # Botón Guardar Como
        save_btn = ctk.CTkButton(
            buttons_frame,
            text="💾 Guardar Como...",
            command=self.save_qr_as,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        save_btn.pack(side="right", padx=(10, 0))
        
    def display_qr_image(self, parent, qr_image):
        """Muestra la imagen del QR en la interfaz"""
        try:
            # Redimensionar imagen para mostrar
            display_size = (300, 300)
            qr_display = qr_image.resize(display_size, Image.Resampling.NEAREST)
            
            # Convertir a PhotoImage
            photo = ImageTk.PhotoImage(qr_display)
            
            # Crear label para mostrar la imagen
            image_label = tk.Label(parent, image=photo, bg=parent.cget("fg_color")[1])
            image_label.image = photo  # Mantener referencia
            image_label.pack(expand=True)
            
        except Exception as e:
            error_label = ctk.CTkLabel(parent, text=f"Error al mostrar imagen: {str(e)}")
            error_label.pack(expand=True)
            
    def save_qr_as(self):
        """Abre diálogo para guardar el QR"""
        if not self.current_qr_image:
            messagebox.showerror("Error", "No hay imagen QR para guardar")
            return
            
        try:
            # Abrir diálogo de guardar archivo
            filename = filedialog.asksaveasfilename(
                title="Guardar código QR como...",
                defaultextension=".png",
                filetypes=[
                    ("Archivos PNG", "*.png"),
                    ("Archivos JPEG", "*.jpg"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            if filename:
                # Crear directorio si no existe
                directory = os.path.dirname(filename)
                if directory and not os.path.exists(directory):
                    os.makedirs(directory, exist_ok=True)
                    
                # Guardar imagen
                self.current_qr_image.save(filename)
                messagebox.showinfo("Éxito", f"✅ Código QR guardado como:\n{filename}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar archivo: {str(e)}")
            
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()


def main():
    """Función principal"""
    try:
        app = QRGeneratorApp()
        app.run()
    except ImportError as e:
        print(f"❌ Error: Falta instalar dependencias: {e}")
        print("💡 Ejecuta: pip install customtkinter qrcode[pil]")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()