import customtkinter as ctk
from PIL import Image
import os
import sys
from generador import generar_contraseña
from gestor_contraseñas import guardar_contraseña, cargar_contraseñas, actualizar_contraseña_en_archivo

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Configuración de la Apariencia ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class PasswordManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuración de la Ventana Principal ---
        self.title("Gestor de Contraseñas")
        self.geometry("500x480") # Aumenté un poco la altura
        self.resizable(False, False)
        try:
            self.iconbitmap(resource_path("icons/candado.ico"))
        except:
            pass  # If icon not found, continue without it

        # --- Cargar Iconos de Servicios ---
        self.load_service_icons()

        # --- Contenedor Principal ---
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(padx=20, pady=20, fill="both", expand=True)

        # --- Creación de las Pestañas ---
        self.tab_view = ctk.CTkTabview(self.main_container)
        self.tab_view.pack(padx=10, pady=10, fill="both", expand=True)

        self.tab_generar = self.tab_view.add("Generar Nueva Contraseña")
        self.tab_regenerar = self.tab_view.add("Regenerar Contraseña")

        # --- Contenido de la Pestaña "Generar" ---
        self.setup_generate_tab()

        # --- Contenido de la Pestaña "Regenerar" ---
        self.setup_regenerate_tab()

    def load_service_icons(self):
        self.service_icons = {}
        icon_files = {
            "Instagram": "instagram.ico",
            "Gmail": "gmail.ico",
            "Facebook": "facebook.ico",
            "GitHub": "github.ico"
        }
        
        for service, icon_file in icon_files.items():
            try:
                icon_path = resource_path(f"icons/{icon_file}")
                self.service_icons[service] = ctk.CTkImage(Image.open(icon_path), size=(24, 24))
            except Exception as e:
                # If icon not found, create a placeholder or skip
                print(f"Warning: Could not load icon for {service}: {e}")
                self.service_icons[service] = None

    def setup_generate_tab(self):
        frame = self.tab_generar
        services = list(self.service_icons.keys())

        title_label = ctk.CTkLabel(frame, text="Crear Nueva Contraseña", font=ctk.CTkFont(size=16, weight="bold"))
        title_label.pack(pady=(10, 20))

        # Marco para Servicio (Menú + Icono)
        service_frame = ctk.CTkFrame(frame)
        service_frame.pack(pady=10, padx=20, fill="x")

        self.service_menu_gen = ctk.CTkOptionMenu(service_frame, values=services, command=self.update_icon_gen)
        self.service_menu_gen.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.icon_label_gen = ctk.CTkLabel(service_frame, text="")
        self.icon_label_gen.pack(side="right")
        self.update_icon_gen(services[0]) # Mostrar el primer icono por defecto

        self.entry_email_gen = ctk.CTkEntry(frame, placeholder_text="Correo Electrónico o Nombre de Usuario")
        self.entry_email_gen.pack(pady=10, padx=20, fill="x")

        slider_frame = ctk.CTkFrame(frame)
        slider_frame.pack(pady=10, padx=20, fill="x")
        self.slider_label_gen = ctk.CTkLabel(slider_frame, text="Longitud: 12")
        self.slider_label_gen.pack(side="left", padx=10)
        self.slider_gen = ctk.CTkSlider(slider_frame, from_=8, to=32, number_of_steps=24, command=lambda v: self.slider_label_gen.configure(text=f"Longitud: {int(v)}"))
        self.slider_gen.set(12)
        self.slider_gen.pack(side="right", fill="x", expand=True, padx=10)

        generate_button = ctk.CTkButton(frame, text="Generar y Guardar", command=self.generate_and_save_password)
        generate_button.pack(pady=20, padx=20, fill="x")

        self.result_label_gen = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=12), wraplength=400)
        self.result_label_gen.pack(pady=10)

    def setup_regenerate_tab(self):
        frame = self.tab_regenerar
        services = list(self.service_icons.keys())

        title_label = ctk.CTkLabel(frame, text="Regenerar Contraseña Existente", font=ctk.CTkFont(size=16, weight="bold"))
        title_label.pack(pady=(10, 20))

        service_frame = ctk.CTkFrame(frame)
        service_frame.pack(pady=10, padx=20, fill="x")

        self.service_menu_regen = ctk.CTkOptionMenu(service_frame, values=services, command=self.update_icon_regen)
        self.service_menu_regen.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.icon_label_regen = ctk.CTkLabel(service_frame, text="")
        self.icon_label_regen.pack(side="right")
        self.update_icon_regen(services[0])

        self.entry_email_regen = ctk.CTkEntry(frame, placeholder_text="Correo o Usuario de Verificación")
        self.entry_email_regen.pack(pady=10, padx=20, fill="x")

        slider_frame = ctk.CTkFrame(frame)
        slider_frame.pack(pady=10, padx=20, fill="x")
        self.slider_label_regen = ctk.CTkLabel(slider_frame, text="Nueva Longitud: 16")
        self.slider_label_regen.pack(side="left", padx=10)
        self.slider_regen = ctk.CTkSlider(slider_frame, from_=8, to=32, number_of_steps=24, command=lambda v: self.slider_label_regen.configure(text=f"Nueva Longitud: {int(v)}"))
        self.slider_regen.set(16)
        self.slider_regen.pack(side="right", fill="x", expand=True, padx=10)

        regenerate_button = ctk.CTkButton(frame, text="Verificar y Regenerar", command=self.regenerate_password)
        regenerate_button.pack(pady=20, padx=20, fill="x")

        self.status_label_regen = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=12), wraplength=400)
        self.status_label_regen.pack(pady=10)

    def update_icon_gen(self, service: str):
        icon = self.service_icons.get(service)
        self.icon_label_gen.configure(image=icon)

    def update_icon_regen(self, service: str):
        icon = self.service_icons.get(service)
        self.icon_label_regen.configure(image=icon)

    def generate_and_save_password(self):
        servicio = self.service_menu_gen.get()
        correo = self.entry_email_gen.get()
        longitud = int(self.slider_gen.get())

        if not servicio or not correo:
            self.result_label_gen.configure(text="Por favor, completa todos los campos.", text_color="orange")
            return

        contraseña = generar_contraseña(longitud)
        guardar_contraseña(servicio, correo, contraseña)
        self.result_label_gen.configure(text=f"Guardado con éxito. Tu contraseña es: {contraseña}", text_color="lightgreen")

    def regenerate_password(self):
        servicio = self.service_menu_regen.get()
        correo_verificacion = self.entry_email_regen.get()
        
        if not servicio or not correo_verificacion:
            self.status_label_regen.configure(text="Introduce el servicio y el correo para verificar.", text_color="orange")
            return

        contraseñas = cargar_contraseñas()

        if servicio not in contraseñas:
            self.status_label_regen.configure(text="Servicio no encontrado en la base de datos.", text_color="red")
            return

        correo_guardado, _ = contraseñas[servicio]
        if correo_verificacion != correo_guardado:
            self.status_label_regen.configure(text="El correo o usuario no coincide. Verificación fallida.", text_color="red")
            return

        nueva_longitud = int(self.slider_regen.get())
        nueva_contraseña = generar_contraseña(nueva_longitud)
        actualizar_contraseña_en_archivo(servicio, correo_guardado, nueva_contraseña)
        self.status_label_regen.configure(text=f"¡Éxito! Nueva contraseña: {nueva_contraseña}", text_color="lightgreen")

if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()
