"""Interfaz para la seguridad de contraseñas y codificación de datos, usando tecnología CustomTkinter."""

import customtkinter as ctk
from tkinter import messagebox
import base64
import os
import re
import pyperclip # Para copiar al portapapeles

# Importar funciones de seguridad desde el archivo security.py
from security import hash_password, verify_password


class SecurityApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Herramienta de Seguridad")
        self.geometry("450x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.primary_color = "#007BFF"
        self.success_color = "#28A745"
        self.error_color = "#DC3545"
        self.bg_color = "#1E1E1E"
        self.fg_color = "#2C2C2C"

        self.users = {}

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.auth_page = self.create_auth_page(self.container)
        self.base64_page = self.create_base64_page(self.container)
        self.strength_page = self.create_strength_page(self.container)

        for page in [self.auth_page, self.base64_page, self.strength_page]:
            page.grid(row=0, column=0, sticky="nsew")

        self.nav_frame = ctk.CTkFrame(self, fg_color=self.fg_color, corner_radius=15)
        self.nav_frame.pack(fill="x", padx=20, pady=(0, 20))
        self.nav_frame.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(self.nav_frame, text="Autenticación", command=lambda: self.show_page(self.auth_page)).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="Codificador", command=lambda: self.show_page(self.base64_page)).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="Fortaleza", command=lambda: self.show_page(self.strength_page)).grid(row=0, column=2, padx=10, pady=10)

        self.show_page(self.auth_page)

    def show_page(self, page_to_show):
        page_to_show.tkraise()

    def create_auth_page(self, parent):
        page = ctk.CTkFrame(parent, fg_color=self.fg_color, corner_radius=15)
        page.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(page, text="Autenticación", font=ctk.CTkFont(size=22, weight="bold")).grid(row=0, column=0, pady=(20, 15))

        self.username_entry = ctk.CTkEntry(page, placeholder_text="Usuario", width=250, height=35, corner_radius=10)
        self.username_entry.grid(row=1, column=0, pady=10, padx=20)

        self.password_entry = ctk.CTkEntry(page, placeholder_text="Contraseña", show="*", width=250, height=35, corner_radius=10)
        self.password_entry.grid(row=2, column=0, pady=10, padx=20)

        ctk.CTkButton(page, text="Iniciar Sesión", command=self.perform_login, width=250, height=35, corner_radius=10, fg_color=self.primary_color, hover_color="#0056B3").grid(row=3, column=0, pady=10)
        ctk.CTkButton(page, text="Registrarse", command=self.perform_register, width=250, height=35, corner_radius=10, fg_color="transparent", border_color=self.primary_color, border_width=2, hover_color=self.fg_color).grid(row=4, column=0, pady=(5, 20))
        
        return page

    def create_base64_page(self, parent):
        page = ctk.CTkFrame(parent, fg_color=self.fg_color, corner_radius=15)
        page.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(page, text="Codificador Base64", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(20, 15))

        self.data_input_entry = ctk.CTkEntry(page, placeholder_text="Introduce datos para codificar o decodificar...", width=350, height=35, corner_radius=10)
        self.data_input_entry.grid(row=1, column=0, pady=10, padx=20)

        button_frame = ctk.CTkFrame(page, fg_color="transparent")
        button_frame.grid(row=2, column=0, pady=10, padx=20)
        button_frame.grid_columnconfigure((0,1), weight=1)

        ctk.CTkButton(button_frame, text="Codificar", command=self.perform_encode, width=170, height=35, corner_radius=10).grid(row=0, column=0, padx=(0,5))
        ctk.CTkButton(button_frame, text="Decodificar", command=self.perform_decode, width=170, height=35, corner_radius=10).grid(row=0, column=1, padx=(5,0))

        ctk.CTkLabel(page, text="Resultado:", font=ctk.CTkFont(size=14)).grid(row=3, column=0, pady=(10, 0), padx=20, sticky="w")

        output_frame = ctk.CTkFrame(page, fg_color="transparent")
        output_frame.grid(row=4, column=0, pady=(0, 20), padx=20, sticky="ew")
        output_frame.grid_columnconfigure(0, weight=1)

        self.result_output = ctk.CTkEntry(output_frame, width=280, height=35, corner_radius=10, state="readonly")
        self.result_output.grid(row=0, column=0, sticky="ew")

        self.copy_button = ctk.CTkButton(output_frame, text="Copiar", command=self.copy_to_clipboard, width=60, height=35, corner_radius=10)
        self.copy_button.grid(row=0, column=1, padx=(10, 0))

        return page

    def create_strength_page(self, parent):
        page = ctk.CTkFrame(parent, fg_color=self.fg_color, corner_radius=15)
        page.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(page, text="Fortaleza de Contraseña", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(20, 15))

        self.check_password_entry = ctk.CTkEntry(page, placeholder_text="Introduce una contraseña...", show="*", width=300, height=35, corner_radius=10)
        self.check_password_entry.grid(row=1, column=0, pady=10, padx=20)

        ctk.CTkButton(page, text="Verificar Fortaleza", command=self.check_password_strength, width=300, height=35, corner_radius=10).grid(row=2, column=0, pady=10)

        self.strength_result_label = ctk.CTkLabel(page, text="Fortaleza:", wraplength=380, justify="left")
        self.strength_result_label.grid(row=3, column=0, pady=(10, 20), padx=20)

        return page

    def set_output_text(self, text):
        self.result_output.configure(state="normal")
        self.result_output.delete(0, "end")
        self.result_output.insert(0, text)
        self.result_output.configure(state="readonly")

    def copy_to_clipboard(self):
        pyperclip.copy(self.result_output.get())
        messagebox.showinfo("Copiado", "¡Resultado copiado al portapapeles!")

    def perform_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Error de Login", "Usuario y contraseña no pueden estar vacíos.")
            return
        stored_pw = self.users.get(username)
        if stored_pw and verify_password(stored_pw, password):
            messagebox.showinfo("Login Exitoso", f"Bienvenido, {username}!")
        else:
            messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos.")

    def perform_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Error de Registro", "Usuario y contraseña no pueden estar vacíos.")
            return
        if username in self.users:
            messagebox.showerror("Error de Registro", "El usuario ya existe.")
        else:
            self.users[username] = hash_password(password)
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")

    def perform_encode(self):
        data = self.data_input_entry.get()
        if not data:
            self.set_output_text("Introduce datos para codificar.")
            return
        try:
            encoded_data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
            self.set_output_text(encoded_data)
        except Exception as e:
            self.set_output_text(f"Error: {e}")

    def perform_decode(self):
        data = self.data_input_entry.get()
        if not data:
            self.set_output_text("Introduce datos para decodificar.")
            return
        try:
            decoded_data = base64.b64decode(data).decode("utf-8")
            self.set_output_text(decoded_data)
        except Exception as e:
            self.set_output_text(f"Error de decodificación.")

    def check_password_strength(self):
        password = self.check_password_entry.get()
        strength = "Débil"
        color = self.error_color
        if len(password) >= 8 and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
            strength = "Media"
            color = "orange"
        if len(password) >= 12 and re.search(r"[0-9]", password) and re.search(r"[\W_]", password):
            strength = "Fuerte"
            color = self.success_color
        self.strength_result_label.configure(text=f"Fortaleza: {strength}", text_color=color)

if __name__ == "__main__":
    app = SecurityApp()
    app.mainloop()