# 🚀 Executables - Colección de Herramientas Python

Una colección de aplicaciones Python con interfaces gráficas compiladas como ejecutables para uso práctico y educativo.

## 📋 Descripción General

Este proyecto contiene múltiples herramientas desarrolladas en Python que han sido compiladas como ejecutables independientes usando PyInstaller. Cada herramienta está diseñada para resolver problemas específicos de manera eficiente y con interfaces gráficas intuitivas.

## 🛠️ Herramientas Incluidas

### 1. 🎯 Generador de Códigos QR (`qr_dactilars_pc/`)
**Aplicación principal del proyecto** - Una herramienta moderna y completa para generar códigos QR con múltiples funcionalidades.

#### Características:
- **Tipos de QR Soportados:**
  - 📝 Texto Simple
  - 🌐 URL/Página Web con validación
  - 👤 Información de Contacto (vCard)
  - 📶 Configuración WiFi
  - 🎨 QR Personalizado con colores
  - 📚 Ejemplos de Aprendizaje

- **Interfaz Moderna:**
  - ✨ Diseño elegante con CustomTkinter
  - 🌙 Modo oscuro/claro intercambiable
  - 📱 Interfaz responsive
  - 🎨 Componentes modulares reutilizables

- **Funcionalidades Avanzadas:**
  - 💾 Diálogo "Guardar Como" nativo
  - 📂 Creación automática de directorios
  - ⚙️ Configuración persistente
  - 🔄 Gestión de archivos recientes

#### Archivos principales:
- `main_app.py` - Aplicación principal
- `qr_generator.py` - Lógica de generación
- `ui_components.py` - Componentes de interfaz
- `forms.py` - Formularios específicos
- `file_manager.py` - Gestión de archivos

### 2. 🖼️ Convertidor de Imágenes a WebP (`Convert_img_webp/`)
Herramienta para conversión masiva de imágenes a formato WebP para optimización web.

#### Características:
- Conversión de múltiples formatos: JPG, JPEG, PNG, BMP, GIF
- Procesamiento por lotes de carpetas completas
- Interfaz gráfica intuitiva
- Creación automática de carpetas de destino

#### Archivos principales:
- `converter_img_webp.py` - Lógica de conversión
- `interfazGUI.py` - Interfaz gráfica
- `interfazGUI.spec` - Configuración de compilación

### 3. 🔐 Herramienta de Seguridad (`security hash base64/`)
Aplicación educativa para demostrar conceptos de seguridad en programación.

#### Características:
- **Hashing de Contraseñas:**
  - Uso de PBKDF2 con SHA-256
  - Generación automática de salt
  - Verificación segura de contraseñas
  
- **Codificación Base64:**
  - Codificación y decodificación de datos
  - Ejemplos educativos
  
- **Interfaz Gráfica:**
  - Herramientas interactivas
  - Ejemplos prácticos

#### Archivos principales:
- `security.py` - Lógica de seguridad
- `interfaz_security.py` - Interfaz gráfica
- `SecurityTool.spec` - Configuración de compilación

## 📁 Estructura del Proyecto

```
executables/
├── 📂 qr_dactilars_pc/           # Generador de QR (Proyecto Principal)
│   ├── main_app.py               # Aplicación principal
│   ├── qr_generator.py           # Lógica de generación
│   ├── ui_components.py          # Componentes UI
│   ├── forms.py                  # Formularios
│   ├── file_manager.py           # Gestión de archivos
│   ├── qr_scaner.py             # Scanner QR
│   ├── run.py                    # Punto de entrada
│   ├── 📂 icons/                 # Iconos de la aplicación
│   ├── 📂 ejemplos_qr/           # Ejemplos generados
│   └── README.md                 # Documentación detallada
│
├── 📂 Convert_img_webp/          # Convertidor de imágenes
│   ├── converter_img_webp.py     # Lógica de conversión
│   ├── interfazGUI.py            # Interfaz gráfica
│   └── interfazGUI.spec          # Config compilación
│
├── 📂 security hash base64/      # Herramientas de seguridad
│   ├── security.py               # Funciones de seguridad
│   ├── interfaz_security.py      # Interfaz gráfica
│   └── SecurityTool.spec         # Config compilación
│
├── 📂 qr_generated/              # QRs generados
│   ├── qr_contact.png
│   ├── qr_wifi.png
│   └── ...
│
├── 📂 build/                     # Archivos de compilación
├── 📂 dist/                      # Ejecutables compilados
│   ├── interfazGUI.exe           # Convertidor WebP
│   └── SecurityTool.exe          # Herramienta Seguridad
│
├── qr_app_config.json            # Configuración global
└── README.md                     # Este archivo
```

## 🚀 Instalación y Uso

### Dependencias Requeridas:
```bash
pip install customtkinter qrcode[pil] pillow
```

### Ejecutar las Aplicaciones:

#### Generador de QR:
```bash
cd qr_dactilars_pc
python main_app.py
# o
python run.py
```

#### Convertidor WebP:
```bash
cd Convert_img_webp
python interfazGUI.py
```

#### Herramienta de Seguridad:
```bash
cd "security hash base64"
python interfaz_security.py
```

### Ejecutables Compilados:
Los ejecutables están disponibles en la carpeta `dist/`:
- `interfazGUI.exe` - Convertidor de imágenes
- `SecurityTool.exe` - Herramienta de seguridad

## 🔧 Compilación

Para compilar las aplicaciones como ejecutables:

```bash
# Instalar PyInstaller
pip install pyinstaller

# Compilar usando archivos .spec existentes
pyinstaller interfazGUI.spec
pyinstaller SecurityTool.spec
```

## ⚙️ Configuración

### Configuración Global (`qr_app_config.json`):
```json
{
  "theme": "dark",
  "default_save_location": "",
  "recent_files": [],
  "window_size": "800x600",
  "auto_save_examples": false
}
```

## 🎯 Casos de Uso

### Para Desarrolladores:
- Generar QRs para testing de aplicaciones móviles
- Convertir imágenes para optimización web
- Aprender conceptos de seguridad en programación

### Para Usuarios Finales:
- Crear QRs para compartir información de contacto
- Generar QRs para configuración WiFi
- Convertir imágenes a formato WebP para web
- Hashear contraseñas de forma segura

## 🛡️ Características de Seguridad

- **Hashing Seguro**: Uso de PBKDF2 con 100,000 iteraciones
- **Salt Aleatorio**: Generación automática para cada contraseña
- **Validación de Entrada**: Verificación de datos en todas las aplicaciones
- **Gestión Segura de Archivos**: Validación de rutas y permisos

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📝 Notas del Desarrollador

- **Autor**: @GermanGonzalez
- **Fecha de Creación**: Julio 2024 - Julio 2025
- **Lenguaje Principal**: Python 3.x
- **Framework GUI**: CustomTkinter, Tkinter
- **Herramientas de Compilación**: PyInstaller

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Interfaz moderna
- [qrcode](https://github.com/lincolnloop/python-qrcode) - Generación de códigos QR
- [Pillow](https://pillow.readthedocs.io/) - Procesamiento de imágenes
- [PyInstaller](https://pyinstaller.org/) - Compilación de ejecutables

---

**¡Explora cada herramienta y descubre cómo pueden mejorar tu flujo de trabajo!** 🚀