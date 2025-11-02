#!/usr/bin/env python3
"""
Script de instalación automática para el Conversor de Audio Universal
Instala todas las dependencias necesarias incluyendo FFmpeg
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
import shutil

def install_pip_packages():
    """Instalar paquetes de Python necesarios"""
    print("📦 Instalando paquetes de Python...")
    
    packages = [
        "customtkinter>=5.2.0",
        "pydub>=0.25.1",
        "pathlib2>=2.3.7"
    ]
    
    for package in packages:
        try:
            print(f"   Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"   ✅ {package} instalado correctamente")
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Error instalando {package}: {e}")
            return False
    
    return True

def download_ffmpeg():
    """Descargar e instalar FFmpeg"""
    print("🎵 Descargando FFmpeg...")
    
    try:
        # URL de descarga de FFmpeg para Windows
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        current_dir = os.getcwd()
        ffmpeg_dir = os.path.join(current_dir, "ffmpeg")
        zip_path = os.path.join(current_dir, "ffmpeg.zip")
        
        print("   Descargando archivo...")
        urllib.request.urlretrieve(ffmpeg_url, zip_path)
        print("   ✅ Descarga completada")
        
        print("   Extrayendo archivos...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(current_dir)
        
        # Encontrar la carpeta extraída y renombrarla
        for item in os.listdir(current_dir):
            if item.startswith("ffmpeg-") and os.path.isdir(item):
                if os.path.exists(ffmpeg_dir):
                    shutil.rmtree(ffmpeg_dir)
                os.rename(item, ffmpeg_dir)
                break
        
        # Limpiar archivo zip
        if os.path.exists(zip_path):
            os.remove(zip_path)
        
        print("   ✅ FFmpeg instalado correctamente")
        return True
        
    except Exception as e:
        print(f"   ❌ Error descargando FFmpeg: {e}")
        return False

def check_ffmpeg():
    """Verificar si FFmpeg está disponible"""
    try:
        # Verificar en ubicaciones comunes
        common_paths = [
            os.path.join(os.getcwd(), "ffmpeg", "bin", "ffmpeg.exe"),
            "C:\\ffmpeg\\bin\\ffmpeg.exe"
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return True
        
        # Verificar en PATH
        try:
            subprocess.run(["ffmpeg", "-version"], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        return False
        
    except Exception:
        return False

def create_batch_file():
    """Crear archivo batch para ejecutar la aplicación fácilmente"""
    batch_content = f"""@echo off
cd /d "{os.getcwd()}"
set PATH=%PATH%;{os.path.join(os.getcwd(), "ffmpeg", "bin")}
python audio_converter_gui.py
pause
"""
    
    batch_path = os.path.join(os.getcwd(), "Ejecutar_Conversor.bat")
    
    try:
        with open(batch_path, 'w', encoding='utf-8') as f:
            f.write(batch_content)
        print(f"✅ Archivo de ejecución creado: {batch_path}")
        return True
    except Exception as e:
        print(f"❌ Error creando archivo batch: {e}")
        return False

def main():
    """Función principal de instalación"""
    print("🎵 Instalador del Conversor de Audio Universal")
    print("=" * 50)
    
    # Verificar Python
    if sys.version_info < (3, 7):
        print("❌ Se requiere Python 3.7 o superior")
        return False
    
    print(f"✅ Python {sys.version} detectado")
    
    # Instalar paquetes de Python
    if not install_pip_packages():
        print("❌ Error instalando paquetes de Python")
        return False
    
    # Verificar/instalar FFmpeg
    if check_ffmpeg():
        print("✅ FFmpeg ya está disponible")
    else:
        print("⚠️  FFmpeg no encontrado, descargando...")
        if not download_ffmpeg():
            print("❌ Error instalando FFmpeg")
            print("💡 Puedes instalarlo manualmente desde: https://ffmpeg.org/download.html")
            return False
    
    # Crear archivo batch
    create_batch_file()
    
    print("\n" + "=" * 50)
    print("🎉 ¡Instalación completada exitosamente!")
    print("=" * 50)
    print("Para ejecutar el conversor:")
    print("1. Ejecuta: python audio_converter_gui.py")
    print("2. O haz doble clic en: Ejecutar_Conversor.bat")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            input("\nPresiona Enter para salir...")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ Instalación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("\nPresiona Enter para salir...")
        sys.exit(1)