#!/usr/bin/env python3
"""
Script de compilación para el Conversor de Audio Universal
Crea un ejecutable usando PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Instalar PyInstaller si no está disponible"""
    try:
        import PyInstaller
        print("✅ PyInstaller ya está instalado")
        return True
    except ImportError:
        print("📦 Instalando PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller instalado correctamente")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando PyInstaller: {e}")
            return False

def clean_build_directories():
    """Limpiar directorios de compilación anteriores"""
    directories_to_clean = ['build', 'dist', '__pycache__']
    
    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"🧹 Limpiando directorio: {directory}")
            shutil.rmtree(directory)
    
    # Limpiar archivos .spec antiguos (excepto el nuestro)
    for spec_file in Path('.').glob('*.spec'):
        if spec_file.name != 'ConversorAudioUniversal.spec':
            print(f"🧹 Eliminando archivo spec: {spec_file}")
            spec_file.unlink()

def create_executable():
    """Crear el ejecutable usando PyInstaller"""
    print("🔨 Compilando aplicación...")
    
    # Usar archivo .spec personalizado
    spec_file = "ConversorAudioUniversal.spec"
    
    # Comando de PyInstaller usando archivo .spec
    pyinstaller_cmd = [
        "pyinstaller",
        "--clean",                      # Limpiar cache
        spec_file
    ]
    
    try:
        # Ejecutar PyInstaller
        result = subprocess.run(pyinstaller_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Compilación exitosa!")
            
            # Verificar que el ejecutable se creó
            exe_path = os.path.join("dist", "ConversorAudioUniversal.exe")
            if os.path.exists(exe_path):
                file_size = os.path.getsize(exe_path) / (1024 * 1024)  # MB
                print(f"📁 Ejecutable creado: {exe_path}")
                print(f"📊 Tamaño: {file_size:.1f} MB")
                return True
            else:
                print("❌ El ejecutable no se encontró en la carpeta dist/")
                return False
        else:
            print("❌ Error durante la compilación:")
            print(result.stderr)
            if result.stdout:
                print("Salida estándar:")
                print(result.stdout)
            return False
            
    except FileNotFoundError:
        print("❌ PyInstaller no encontrado. Asegúrate de que esté instalado.")
        return False
    except Exception as e:
        print(f"❌ Error inesperado durante la compilación: {e}")
        return False

def copy_additional_files():
    """Copiar archivos adicionales al directorio de distribución"""
    print("📋 Copiando archivos adicionales...")
    
    files_to_copy = [
        "README_MODULAR.md",
        "requirements.txt"
    ]
    
    dist_dir = "dist"
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            shutil.copy2(file_name, dist_dir)
            print(f"   ✅ Copiado: {file_name}")
        else:
            print(f"   ⚠️  No encontrado: {file_name}")

def create_installer_info():
    """Crear archivo de información del instalador"""
    info_content = """
# Conversor de Audio Universal - Ejecutable

## 🚀 Ejecución

Simplemente ejecuta `ConversorAudioUniversal.exe` para iniciar la aplicación.

## 📋 Características

- Ejecutable independiente (no requiere Python instalado)
- Incluye todas las dependencias necesarias
- FFmpeg se descarga automáticamente si es necesario
- Interfaz gráfica moderna con tema oscuro

## 🔧 Solución de Problemas

### El antivirus bloquea el ejecutable
- Esto es normal para ejecutables creados con PyInstaller
- Agrega una excepción en tu antivirus
- El archivo es seguro, puedes verificar el código fuente

### Error al iniciar
- Ejecuta como administrador si es necesario
- Verifica que tengas permisos de escritura en la carpeta
- Revisa que no haya otro antivirus bloqueando la ejecución

## 📁 Archivos Incluidos

- `ConversorAudioUniversal.exe` - Aplicación principal
- `README_MODULAR.md` - Documentación completa
- `requirements.txt` - Lista de dependencias (referencia)

---

**¡Disfruta convirtiendo tus archivos de audio! 🎵**
"""
    
    with open("dist/LEEME.txt", "w", encoding="utf-8") as f:
        f.write(info_content)
    
    print("✅ Archivo de información creado: dist/LEEME.txt")

def main():
    """Función principal de compilación"""
    print("🎵 Compilador del Conversor de Audio Universal")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("audio_converter_gui_modular.py"):
        print("❌ Error: No se encontró el archivo principal.")
        print("   Asegúrate de ejecutar este script desde el directorio del proyecto.")
        return False
    
    # Verificar que existe el icono
    if not os.path.exists("icons/musica.ico"):
        print("❌ Error: No se encontró el icono en icons/musica.ico")
        return False
    
    # Instalar PyInstaller
    if not install_pyinstaller():
        return False
    
    # Limpiar directorios anteriores
    clean_build_directories()
    
    # Crear ejecutable
    if not create_executable():
        return False
    
    # Copiar archivos adicionales
    copy_additional_files()
    
    # Crear información del instalador
    create_installer_info()
    
    print("\n" + "=" * 50)
    print("🎉 ¡Compilación completada exitosamente!")
    print("=" * 50)
    print("📁 El ejecutable está en: dist/ConversorAudioUniversal.exe")
    print("📋 Archivos adicionales copiados a la carpeta dist/")
    print("🚀 Puedes distribuir toda la carpeta dist/ o solo el .exe")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            input("\nPresiona Enter para salir...")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ Compilación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("\nPresiona Enter para salir...")
        sys.exit(1)