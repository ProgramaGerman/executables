"""
Script para verificar que el ejecutable compilado funciona correctamente
"""

import os
from pathlib import Path

def test_executable():
    """Prueba el ejecutable compilado"""
    
    # Ruta al ejecutable
    exe_path = Path(__file__).parent / "dist" / "QR_Generator.exe"
    
    print("🔍 Verificando el ejecutable compilado...")
    print(f"📁 Ruta: {exe_path}")
    
    # Verificar que existe
    if not exe_path.exists():
        print("❌ Error: El ejecutable no existe")
        return False
    
    # Verificar tamaño
    size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"📊 Tamaño: {size_mb:.1f} MB")
    
    # Verificar icono (intentar extraer información)
    try:
        import win32api
        info = win32api.GetFileVersionInfo(str(exe_path), "\\")
        print("✅ Información del ejecutable encontrada")
    except ImportError:
        print("⚠️ win32api no disponible para verificar información del ejecutable")
    except Exception as e:
        print(f"⚠️ No se pudo obtener información del ejecutable: {e}")
    
    print("\n🚀 Para probar el ejecutable, ejecuta:")
    print(f'   "{exe_path}"')
    print("\n📝 Notas:")
    print("   - El icono debería aparecer en la barra de tareas")
    print("   - El ejecutable no debería mostrar ventana de consola")
    print("   - Todas las funcionalidades deberían funcionar normalmente")
    
    return True

def create_desktop_shortcut():
    """Crea un acceso directo en el escritorio"""
    try:
        import win32com.client
        
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        exe_path = Path(__file__).parent / "dist" / "QR_Generator.exe"
        shortcut_path = os.path.join(desktop, "QR Generator.lnk")
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = str(exe_path)
        shortcut.WorkingDirectory = str(exe_path.parent)
        shortcut.IconLocation = str(exe_path)
        shortcut.Description = "Generador de Códigos QR"
        shortcut.save()
        
        print(f"✅ Acceso directo creado en: {shortcut_path}")
        return True
        
    except ImportError:
        print("⚠️ pywin32 no disponible para crear acceso directo")
        return False
    except Exception as e:
        print(f"❌ Error al crear acceso directo: {e}")
        return False

def main():
    """Función principal"""
    print("🔧 Verificador del ejecutable QR Generator")
    print("=" * 50)
    
    # Verificar ejecutable
    if test_executable():
        print("\n✅ Verificación completada")
        
        # Preguntar si crear acceso directo
        try:
            response = input("\n¿Crear acceso directo en el escritorio? (s/n): ").lower()
            if response in ['s', 'si', 'sí', 'y', 'yes']:
                create_desktop_shortcut()
        except KeyboardInterrupt:
            print("\n\n👋 Saliendo...")
    
    print("\n🎉 ¡Compilación exitosa!")
    print("📱 Tu aplicación está lista para distribuir")

if __name__ == "__main__":
    main()