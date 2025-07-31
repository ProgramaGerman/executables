"""Interfaz para la conversión de imágenes a formato WebP, usando tecnología CustomTkinter"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from converter_img_webp import convert_folder_images_to_webp
import tkinter.messagebox as messagebox


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
        """Convierte las imágenes de la carpeta de entrada a formato WebP y las guarda en la carpeta de salida."""
        input_folder = self.input_entry.get()
        output_folder = self.output_entry.get()

        self.convert_button.configure(state="disabled")
        self.status_label.configure(text="Procesando...", text_color="blue")

        if not input_folder or not output_folder:
            self.status_label.configure(
                text="Por favor, seleccione ambas carpetas.", text_color="red"
            )
            messagebox.showerror("Error", "Por favor, seleccione ambas carpetas.")
            self.convert_button.configure(state="normal")
            return

        import pathlib

        valid_exts = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
        input_path = pathlib.Path(input_folder)
        image_files = [
            f
            for f in input_path.rglob("*")
            if f.suffix.lower() in valid_exts and f.is_file()
        ]

        if not image_files:
            self.status_label.configure(
                text="No se encontraron imágenes válidas en la carpeta seleccionada.",
                text_color="orange",
            )
            messagebox.showwarning(
                "Sin imágenes",
                "No se encontraron imágenes válidas en la carpeta seleccionada.",
            )
            self.convert_button.configure(state="normal")
            return

        from PIL import Image

        output_path = pathlib.Path(output_folder)
        if not output_path.exists():
            output_path.mkdir(parents=True)
        convertidos = 0
        errores = 0
        for image_file in image_files:
            output_file = output_path / (image_file.stem + ".webp")
            try:
                with Image.open(image_file) as img:
                    img.save(output_file, "WEBP")
                convertidos += 1
            except Exception as e:
                errores += 1
        if convertidos > 0:
            msg = (
                f"{convertidos} imagen(es) convertidas y guardadas en {output_folder}."
            )
            if errores > 0:
                msg += f"\n{errores} imagen(es) no se pudieron convertir."
            self.status_label.configure(text=msg, text_color="green")
            messagebox.showinfo("Conversión completada", msg)
        else:
            self.status_label.configure(
                text="No se pudo convertir ninguna imagen.", text_color="red"
            )
            messagebox.showerror("Error", "No se pudo convertir ninguna imagen.")
        self.convert_button.configure(state="normal")


if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()
