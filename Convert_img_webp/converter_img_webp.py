"""Programa que se encarga de convertir imágenes de n formato a formato WebP
#Toma carpeta de imagenes de n formatos, las convierte y guarda en una carpeta """

#Programa creado por: @GermanGonzalez
#Fecha de creación: 2025-07-30

import pathlib
from PIL import Image

def convert_image_to_webp(input_image_path, output_image_path):
    """Convierte una imagen a formato WebP."""
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "WEBP")

def convert_folder_images_to_webp(input_folder, output_folder):
    """
    Convierte todas las imágenes en una carpeta a formato WebP.
    """
    input_path = pathlib.Path(input_folder)
    output_path = pathlib.Path(output_folder)

    if not output_path.exists():
        output_path.mkdir(parents=True)

    for image_file in input_path.glob("*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
            output_file = output_path / (image_file.stem + ".webp")
            convert_image_to_webp(image_file, output_file)

if __name__ == "__main__":
    input_folder_Main = input("Ingrese la ruta de la carpeta de imágenes a convertir: ")
    output_folder_Main = input("Ingrese la Ruta para las imagenes convertidas: ")

    convert_folder_images_to_webp(input_folder_Main, output_folder_Main)
    print(f"Imágenes convertidas y guardadas en {output_folder_Main}")
