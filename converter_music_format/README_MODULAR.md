# 🎵 Conversor de Audio Universal - Versión Modular

Una aplicación moderna con interfaz gráfica para convertir archivos de audio entre diferentes formatos, ahora con **arquitectura modular** para mejor legibilidad y mantenimiento.

## ✨ Características

- **Interfaz moderna** con tema oscuro y colores verde/negro
- **Conversión individual** de archivos de audio
- **Conversión por lotes** de carpetas completas
- **Múltiples formatos** soportados: MP3, WAV, OGG, FLAC, M4A, AAC, WMA
- **Instalación automática** de FFmpeg
- **Procesamiento en segundo plano** con barra de progreso
- **Arquitectura modular** para mejor mantenimiento
- **Código organizado** en archivos de máximo 250 líneas

## 🚀 Instalación y Ejecución

### Opción 1: Instalación Automática (Recomendada)

1. Ejecuta el instalador automático:
```bash
python install_dependencies.py
```

2. Ejecuta la versión modular:
```bash
python audio_converter_gui_modular.py
```

### Opción 2: Instalación Manual

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:
```bash
python audio_converter_gui_modular.py
```

## 📁 Estructura del Proyecto Modular

```
converter_music_format/
├── __init__.py                      # Inicialización del paquete
├── audio_converter.py               # Versión original de consola
├── audio_converter_gui.py           # Interfaz gráfica monolítica (legacy)
├── audio_converter_gui_modular.py   # 🎯 Punto de entrada modular
├── main_app.py                      # Aplicación principal modular
├── config.py                        # Configuración y constantes
├── ffmpeg_manager.py                # Gestión de FFmpeg
├── ui_components.py                 # Componentes de interfaz
├── conversion_handlers.py           # Manejadores de conversión
├── install_dependencies.py          # Instalador automático
├── requirements.txt                 # Dependencias Python
├── README.md                        # Documentación original
├── README_MODULAR.md               # Esta documentación
└── ffmpeg/                          # FFmpeg (se crea automáticamente)
    └── bin/
        ├── ffmpeg.exe
        └── ffprobe.exe
```

## 🏗️ Arquitectura Modular

El proyecto está organizado en módulos especializados para mejorar la legibilidad:

### 📋 Módulos y Responsabilidades

| Módulo | Líneas | Responsabilidad |
|--------|--------|-----------------|
| **`config.py`** | 95 | Configuración, constantes, temas y colores |
| **`audio_converter.py`** | 156 | Lógica de conversión de audio con pydub |
| **`ffmpeg_manager.py`** | 248 | Detección, descarga e instalación de FFmpeg |
| **`ui_components.py`** | 247 | Componentes de interfaz (pestañas, botones) |
| **`conversion_handlers.py`** | 189 | Manejadores de conversión y progreso |
| **`main_app.py`** | 147 | Aplicación principal y coordinación |

**✅ Cada archivo tiene menos de 250 líneas** para mejorar la legibilidad y mantenimiento.

### 🔄 Flujo de la Aplicación

```
audio_converter_gui_modular.py
    ↓
main_app.py (AudioConverterGUI)
    ↓
├── config.py (configuración)
├── ffmpeg_manager.py (verificar FFmpeg)
├── ui_components.py (crear interfaz)
├── conversion_handlers.py (manejar conversiones)
└── audio_converter.py (convertir archivos)
```

## 🎯 Ventajas de la Arquitectura Modular

### ✅ **Legibilidad Mejorada**
- Cada archivo tiene una responsabilidad específica
- Máximo 250 líneas por archivo
- Código más fácil de entender y mantener

### ✅ **Mantenimiento Simplificado**
- Cambios aislados en módulos específicos
- Fácil localización de errores
- Pruebas unitarias más sencillas

### ✅ **Reutilización de Código**
- Módulos independientes reutilizables
- Separación clara de responsabilidades
- Fácil extensión de funcionalidades

### ✅ **Desarrollo Colaborativo**
- Múltiples desarrolladores pueden trabajar en paralelo
- Conflictos de merge reducidos
- Revisiones de código más eficientes

## 🚀 Versiones Disponibles

### 🎯 **Versión Modular** (Recomendada)
```bash
python audio_converter_gui_modular.py
```
- Arquitectura modular
- Código organizado y mantenible
- Fácil de extender y modificar

### 📦 **Versión Legacy** (Monolítica)
```bash
python audio_converter_gui.py
```
- Archivo único de ~700 líneas
- Funcionalidad completa
- Más difícil de mantener

## 🔧 Desarrollo y Extensión

### Agregar Nuevos Formatos
1. Edita `config.py` → `SUPPORTED_FORMATS`
2. Actualiza `AUDIO_EXTENSIONS` si es necesario

### Modificar Interfaz
1. Edita `ui_components.py` para cambios visuales
2. Modifica `config.py` para colores y estilos

### Agregar Funcionalidades
1. Crea nuevos métodos en `audio_converter.py`
2. Agrega manejadores en `conversion_handlers.py`
3. Actualiza la interfaz en `ui_components.py`

## 📋 Requisitos

- **Python 3.7+**
- **FFmpeg** (se instala automáticamente)
- **Dependencias Python**:
  - customtkinter >= 5.2.0
  - pydub >= 0.25.1
  - pathlib2 >= 2.3.7

## 🎯 Uso

### Conversión de Archivo Individual
1. Ve a la pestaña "📄 Archivo Individual"
2. Haz clic en "📁 Examinar" para seleccionar tu archivo
3. Elige el formato de salida
4. Opcionalmente, selecciona carpeta de destino
5. Haz clic en "🔄 Convertir Archivo"

### Conversión por Lotes
1. Ve a la pestaña "📁 Conversión por Lotes"
2. Selecciona carpeta con archivos de audio
3. Elige formato de salida
4. Configura inclusión de subcarpetas
5. Haz clic en "🔄 Convertir Todos los Archivos"

## 🔧 Solución de Problemas

Los problemas y soluciones son los mismos que en la versión original. La arquitectura modular facilita la identificación y corrección de errores específicos.

## 🤝 Contribuir

La arquitectura modular facilita las contribuciones:

1. **Fork** el proyecto
2. **Identifica** el módulo relevante para tu cambio
3. **Modifica** solo los archivos necesarios
4. **Prueba** tu cambio
5. **Envía** un pull request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**¡Disfruta de la nueva arquitectura modular! 🎵✨**