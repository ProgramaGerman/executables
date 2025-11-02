"""
Script para preparar la distribución del ejecutable QR Generator
"""

import os
import shutil
from pathlib import Path
import datetime

def create_distribution_package():
    """Crea un paquete de distribución completo"""
    
    # Rutas
    project_dir = Path(__file__).parent
    exe_path = project_dir / "dist" / "QR_Generator.exe"
    
    # Crear carpeta de distribución
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dist_folder = project_dir / f"QR_Generator_Release_{timestamp}"
    dist_folder.mkdir(exist_ok=True)
    
    print(f"📦 Creando paquete de distribución en: {dist_folder}")
    
    # Copiar ejecutable
    if exe_path.exists():
        shutil.copy2(exe_path, dist_folder / "QR_Generator.exe")
        print("✅ Ejecutable copiado")
    else:
        print("❌ Error: Ejecutable no encontrado")
        return False
    
    # Crear archivo de información
    info_content = f"""# QR Generator - Aplicación Compilada

## Información del Release
- **Fecha de compilación**: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
- **Versión**: 1.0.0
- **Tamaño**: {exe_path.stat().st_size / (1024*1024):.1f} MB

## Instrucciones de Uso

1. **Ejecutar**: Doble clic en `QR_Generator.exe`
2. **Requisitos**: Windows 7 o superior
3. **Instalación**: No requiere instalación, es portable

## Características

- ✅ Generación de códigos QR para texto, URLs, contactos y WiFi
- ✅ Interfaz moderna y fácil de usar
- ✅ Guardado de códigos QR en múltiples formatos
- ✅ Temas claro y oscuro
- ✅ Completamente portable (no requiere Python)

## Soporte

- El icono aparece en la barra de tareas al ejecutar
- No se muestra ventana de consola
- Todas las funcionalidades están incluidas

## Distribución

Este archivo puede copiarse y ejecutarse en cualquier PC con Windows.
No requiere instalación adicional de Python o librerías.
"""
    
    # Guardar información
    with open(dist_folder / "README.txt", "w", encoding="utf-8") as f:
        f.write(info_content)
    print("✅ Archivo README.txt creado")
    
    # Copiar icono para referencia
    icon_path = project_dir / "icons" / "codigo-qr.ico"
    if icon_path.exists():
        shutil.copy2(icon_path, dist_folder / "icono.ico")
        print("✅ Icono copiado para referencia")
    
    print("\n🎉 Paquete de distribución creado exitosamente!")
    print(f"📁 Ubicación: {dist_folder}")
    print("📊 Contenido:")
    for file in dist_folder.iterdir():
        size = file.stat().st_size / (1024*1024) if file.is_file() else 0
        print(f"   - {file.name} ({size:.1f} MB)" if size > 1 else f"   - {file.name}")
    
    return True

def open_distribution_folder():
    """Abre la carpeta de distribución en el explorador"""
    try:
        # Buscar la carpeta de distribución más reciente
        project_dir = Path(__file__).parent
        dist_folders = [d for d in project_dir.iterdir() if d.is_dir() and d.name.startswith("QR_Generator_Release_")]
        
        if dist_folders:
            latest_folder = max(dist_folders, key=lambda x: x.stat().st_mtime)
            os.startfile(latest_folder)
            print(f"📂 Abriendo carpeta: {latest_folder}")
        else:
            print("❌ No se encontraron carpetas de distribución")
            
    except Exception as e:
        print(f"❌ Error al abrir carpeta: {e}")

def main():
    """Función principal"""
    print("📦 Preparador de Distribución - QR Generator")
    print("=" * 50)
    
    if create_distribution_package():
        print("\n🚀 ¿Abrir carpeta de distribución? (s/n): ", end="")
        try:
            response = input().lower()
            if response in ['s', 'si', 'sí', 'y', 'yes']:
                open_distribution_folder()
        except KeyboardInterrupt:
            print("\n👋 Saliendo...")
    
    print("\n✨ ¡Listo para distribuir!")

if __name__ == "__main__":
    main()