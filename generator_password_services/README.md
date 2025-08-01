# Generador de Contraseñas

Este es un gestor de contraseñas completo con interfaz gráfica y de consola para generar y guardar contraseñas seguras.

## Funcionalidades

- **Interfaz Gráfica (GUI)**: Aplicación moderna con CustomTkinter
  - Generar contraseñas con longitud personalizable (8-32 caracteres)
  - Guardar contraseñas para diferentes servicios (Instagram, Gmail, Facebook, GitHub)
  - Regenerar contraseñas existentes con verificación de seguridad
  - Iconos de servicios integrados
  - Tema oscuro moderno

- **Interfaz de Consola (CLI)**: Programa de línea de comandos
  - Generar contraseñas con longitud especificada
  - Guardar las contraseñas para diferentes servicios
  - Editar las contraseñas guardadas

## Archivos del Proyecto

- `app_gui.py` - Aplicación principal con interfaz gráfica
- `main.py` - Aplicación de consola
- `generador.py` - Módulo para generar contraseñas seguras
- `gestor_contraseñas.py` - Módulo para gestionar el almacenamiento
- `icons/` - Directorio con iconos de servicios
- `dist/Gestor_de_Contraseñas.exe` - Ejecutable compilado

## Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutable Compilado (Recomendado)
1. Ejecuta directamente el archivo compilado:
   ```
   dist\Gestor_de_Contraseñas.exe
   ```
   O usa el archivo batch:
   ```
   ejecutar_gui.bat
   ```

### Interfaz Gráfica (Desde código fuente)
1. Ejecuta la aplicación GUI:
   ```
   python app_gui.py
   ```

### Interfaz de Consola
1. Ejecuta el programa de consola:
   ```
   python main.py
   ```
   O usa el archivo batch:
   ```
   ejecutar_cli.bat
   ```

## Compilación

Para recompilar el ejecutable:
```bash
pyinstaller app_gui.spec
```

## Características de Seguridad

- Las contraseñas se generan usando caracteres alfanuméricos y símbolos especiales
- Verificación de usuario antes de regenerar contraseñas
- Almacenamiento local en archivo de texto plano (contraseñas.txt)
- Interfaz intuitiva para gestión de múltiples servicios

## Servicios Soportados

- Instagram
- Gmail  
- Facebook
- GitHub

El sistema es extensible para agregar más servicios fácilmente.
