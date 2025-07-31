"""Interfaz para la conversión de imágenes a formato WebP, usando tecnología CustomTkinter"""

import customtkinter as ctk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from PIL import Image
import threading
import pathlib

class ImageConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Imágenes a WebP")
        self.geometry("600x300")

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Input Folder
        self.input_label = ctk.CTkLabel(self, text="Carpeta de Entrada:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.input_entry = ctk.CTkEntry(
            self, placeholder_text="Seleccione la carpeta de imágenes a convertir"
        )
        self.input_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.input_button = ctk.CTkButton(
            self, text="Examinar", command=self.browse_input_folder
        )
        self.input_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Output Folder
        self.output_label = ctk.CTkLabel(self, text="Carpeta de Salida:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.output_entry = ctk.CTkEntry(
            self, placeholder_text="Seleccione la carpeta para guardar las imágenes"
        )
        self.output_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.output_button = ctk.CTkButton(
            self, text="Examinar", command=self.browse_output_folder
        )
        self.output_button.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        # Convert Button
        self.convert_button = ctk.CTkButton(
            self, text="Convertir", command=self.convert_images
        )
        self.convert_button.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew"
        )

        # Status Label
        self.status_label = ctk.CTkLabel(self, text="", text_color="green")
        self.status_label.grid(
            row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew"
        )

    def browse_input_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.input_entry.delete(0, ctk.END)
            self.input_entry.insert(0, folder_selected)

    def browse_output_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_entry.delete(0, ctk.END)
            self.output_entry.insert(0, folder_selected)

    def convert_images(self):
        """Valida las entradas e inicia el proceso de conversión en un hilo separado para no bloquear la GUI."""
        input_folder = self.input_entry.get()
        output_folder = self.output_entry.get()

        if not input_folder or not output_folder:
            messagebox.showerror("Error", "Por favor, seleccione ambas carpetas.")
            return

        self.convert_button.configure(state="disabled")
        self.status_label.configure(text="Procesando...", text_color="blue")

        # Ejecutar la conversión en un hilo separado para no congelar la interfaz
        conversion_thread = threading.Thread(
            target=self._run_conversion_task,
            args=(input_folder, output_folder),
            daemon=True,
        )
        conversion_thread.start()

    def _run_conversion_task(self, input_folder, output_folder):
        """
        Busca y convierte imágenes. Esta función está diseñada para ejecutarse en un hilo de fondo.
        """
        try:
            valid_exts = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
            input_path = pathlib.Path(input_folder)
            image_files = [
                f
                for f in input_path.rglob("*")
                if f.suffix.lower() in valid_exts and f.is_file()
            ]

            if not image_files:
                self.after(
                    0,
                    self._update_ui_after_conversion,
                    "No se encontraron imágenes válidas en la carpeta seleccionada.",
                    "orange",
                    "warning",
                )
                return

            output_path = pathlib.Path(output_folder)
            output_path.mkdir(parents=True, exist_ok=True)

            convertidos = 0
            errores = 0
            for image_file in image_files:
                output_file = output_path / (image_file.stem + ".webp")
                try:
                    with Image.open(image_file) as img:
                        img.save(output_file, "WEBP")
                    convertidos += 1
                except Exception as e:
                    print(f"Error al convertir {image_file.name}: {e}")
                    errores += 1

            if convertidos > 0:
                msg = f"{convertidos} imagen(es) convertidas y guardadas."
                if errores > 0:
                    msg += f"\n{errores} imagen(es) no se pudieron convertir."
                self.after(0, self._update_ui_after_conversion, msg, "green", "info")
            else:
                msg = "No se pudo convertir ninguna imagen."
                if errores > 0:
                    msg += f"\nOcurrieron {errores} errores durante el proceso."
                self.after(0, self._update_ui_after_conversion, msg, "red", "error")

        except Exception as e:
            print(f"Error inesperado en el hilo de conversión: {e}")
            self.after(
                0,
                self._update_ui_after_conversion,
                f"Ocurrió un error inesperado: {e}",
                "red",
                "error",
            )

    def _update_ui_after_conversion(self, message, color, message_type):
        """
        Actualiza la etiqueta de estado y muestra un cuadro de mensaje.
        Se llama desde el hilo principal usando `self.after`.
        """
        self.status_label.configure(text=message, text_color=color)
        self.convert_button.configure(state="normal")

        if message_type == "info":
            messagebox.showinfo("Conversión Completada", message)
        elif message_type == "warning":
            messagebox.showwarning("Atención", message)
        elif message_type == "error":
            messagebox.showerror("Error", message)

if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()
