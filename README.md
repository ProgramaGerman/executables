# 🛠️ Herramientas Automatizadas Python - Repositorio de Aprendizaje

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](CONTRIBUTING.md)
[![Learning](https://img.shields.io/badge/Purpose-Educational-purple.svg)](#)

> 🎓 **Repositorio educativo** dedicado al desarrollo de herramientas automatizadas en Python, creado con **entusiasmo** por el aprendizaje y la automatización de tareas cotidianas.

## 📋 Descripción General

Este repositorio contiene una colección de **herramientas automatizadas** desarrolladas en Python con fines educativos y prácticos. Cada proyecto está diseñado para resolver problemas específicos mientras se aprenden conceptos avanzados de programación, interfaces gráficas y distribución de software.

### 🎯 Objetivos del Repositorio

- **Aprendizaje práctico** de Python y sus librerías
- **Desarrollo de herramientas útiles** para automatización
- **Exploración de interfaces gráficas** modernas
- **Práctica de distribución** de aplicaciones ejecutables
- **Compartir conocimiento** con la comunidad

## 🗂️ Estructura del Repositorio

```
📁 Practicas programas/
├── 🎯 qr_dactilars_pc/              # Generador de Códigos QR (Proyecto Principal)
├── 🖼️ Convert_img_webp/             # Conversor de Imágenes a WebP
├── 🔐 security hash base64/         # Herramientas de Seguridad y Hashing
├── 📦 dist/                         # Ejecutables compilados
├── 🔧 build/                        # Archivos de construcción
├── 🌐 env/                          # Entorno virtual Python
└── 📄 README.md                     # Este archivo
```

## 🚀 Proyectos Incluidos

### 1. 🎯 **QR Generator - Generador de Códigos QR**
> **Aplicación principal del repositorio**

**Características:**
- ✨ **Interfaz moderna** con CustomTkinter
- 📝 **Múltiples tipos de QR**: Texto, URL, Contacto, WiFi, Personalizado
- 🌙 **Temas claro/oscuro** intercambiables
- 💾 **Guardado inteligente** con diálogos nativos
- 📱 **Diseño responsive** y modular
- 🔧 **Configuración persistente**
- 📦 **Ejecutable compilado** con PyInstaller

**Tecnologías:**
- `CustomTkinter` - Interfaz gráfica moderna
- `qrcode` - Generación de códigos QR
- `Pillow (PIL)` - Procesamiento de imágenes
- `PyInstaller` - Compilación a ejecutable

**Uso:**
```bash
cd qr_dactilars_pc/
python run.py
# O ejecutar: dist/QR_Generator.exe
```

### 2. 🖼️ **Image to WebP Converter**
> **Conversor masivo de imágenes a formato WebP**

**Características:**
- 🔄 **Conversión masiva** de carpetas completas
- 📁 **Múltiples formatos** soportados (JPG, PNG, BMP, GIF)
- 🖥️ **Interfaz gráfica** intuitiva
- ⚡ **Procesamiento eficiente** con Pillow
- 📦 **Versión ejecutable** disponible

**Formatos soportados:**
- **Entrada**: JPG, JPEG, PNG, BMP, GIF
- **Salida**: WebP (optimizado para web)

**Uso:**
```bash
cd Convert_img_webp/
python converter_img_webp.py
# O con interfaz: python interfazGUI.py
```

### 3. 🔐 **Security Tools - Herramientas de Seguridad**
> **Utilidades educativas para hashing y codificación**

**Características:**
- 🔒 **Hashing seguro** de contraseñas con PBKDF2
- 🧂 **Salt automático** para mayor seguridad
- 📊 **Codificación Base64** para datos
- ✅ **Verificación de contraseñas**
- 🎓 **Código educativo** bien documentado
- 🖥️ **Interfaz gráfica** disponible

**Funcionalidades:**
- Generación de hashes seguros
- Verificación de contraseñas
- Codificación/decodificación Base64
- Ejemplos prácticos de seguridad

**Uso:**
```bash
cd "security hash base64"/
python security.py
# O con interfaz: python interfaz_security.py
```

## 📦 Ejecutables Disponibles

Todos los proyectos principales han sido compilados a **ejecutables independientes**:

| Proyecto | Ejecutable | Tamaño | Descripción |
|----------|------------|--------|-------------|
| QR Generator | `QR_Generator.exe` | ~19.7 MB | Generador completo de códigos QR |
| Image Converter | `ImageConverter.exe` | ~15 MB | Conversor de imágenes a WebP |
| Security Tools | `SecurityTool.exe` | ~12 MB | Herramientas de hashing y codificación |

### 🎯 Características de los Ejecutables

- ✅ **Completamente portables** - No requieren Python instalado
- 🖼️ **Iconos personalizados** en barra de tareas
- 🚫 **Sin ventana de consola** - Aplicaciones GUI puras
- 📁 **Auto-contenidos** - Todas las dependencias incluidas
- 🔧 **Configuración persistente** - Guardan preferencias del usuario

## 🛠️ Tecnologías y Dependencias

### **Librerías Principales**
```python
# Interfaz Gráfica
customtkinter>=5.0.0    # Interfaces modernas
tkinter                 # GUI base de Python

# Procesamiento de Imágenes
Pillow>=9.0.0          # Manipulación de imágenes
qrcode[pil]>=7.0.0     # Generación de c��digos QR

# Seguridad
hashlib                # Hashing (built-in)
base64                 # Codificación (built-in)

# Distribución
pyinstaller>=5.0.0     # Compilación a ejecutables
```

### **Herramientas de Desarrollo**
- **Python 3.8+** - Lenguaje principal
- **PyInstaller** - Compilación de ejecutables
- **Git** - Control de versiones
- **VS Code** - Editor recomendado

## 🚀 Instalación y Configuración

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/herramientas-python.git
cd herramientas-python
```

### **2. Crear Entorno Virtual**
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

### **3. Instalar Dependencias**
```bash
# Dependencias básicas
pip install customtkinter qrcode[pil] pillow

# Para compilación (opcional)
pip install pyinstaller

# Todas las dependencias
pip install -r requirements.txt
```

### **4. Ejecutar Proyectos**
```bash
# QR Generator
cd qr_dactilars_pc && python run.py

# Image Converter
cd Convert_img_webp && python interfazGUI.py

# Security Tools
cd "security hash base64" && python interfaz_security.py
```

## 📚 Guías de Uso

### **QR Generator - Guía Rápida**
1. **Ejecutar** la aplicación
2. **Seleccionar** tipo de QR en el menú
3. **Completar** formulario con datos
4. **Generar** y visualizar el QR
5. **Guardar** usando "Guardar Como..."

### **Image Converter - Guía Rápida**
1. **Seleccionar** carpeta de imágenes origen
2. **Elegir** carpeta de destino
3. **Iniciar** conversión masiva
4. **Verificar** imágenes WebP generadas

### **Security Tools - Guía Rápida**
1. **Introducir** contraseña a hashear
2. **Generar** hash seguro con salt
3. **Verificar** contraseñas existentes
4. **Codificar/decodificar** datos en Base64

## 🎓 Aspectos Educativos

### **Conceptos Aprendidos**
- 🏗️ **Arquitectura modular** y separación de responsabilidades
- 🎨 **Interfaces gráficas** modernas con CustomTkinter
- 📦 **Distribución de software** con PyInstaller
- 🔐 **Seguridad básica** y hashing de contraseñas
- 🖼️ **Procesamiento de imágenes** con Pillow
- 📁 **Gestión de archivos** y configuración persistente

### **Patrones de Diseño Implementados**
- **MVC (Model-View-Controller)** - Separación de lógica y UI
- **Factory Pattern** - Creación de formularios dinámicos
- **Observer Pattern** - Manejo de eventos de UI
- **Singleton Pattern** - Gestión de configuración global

### **Buenas Prácticas Aplicadas**
- ✅ **Código limpio** y bien documentado
- ✅ **Manejo de errores** robusto
- ✅ **Validación de entrada** de usuario
- ✅ **Configuración externa** en JSON
- ✅ **Logging** para debugging
- ✅ **Modularidad** y reutilización

## 🤝 Contribuciones y Feedback

### **¡Tu Feedback es Bienvenido!**

Este repositorio está **abierto a contribuciones** y feedback de la comunidad. Todas las sugerencias, mejoras y correcciones son **altamente valoradas**.

### **Formas de Contribuir**
- 🐛 **Reportar bugs** o problemas encontrados
- 💡 **Sugerir nuevas características** o mejoras
- 📝 **Mejorar documentación** existente
- 🔧 **Contribuir con código** y nuevas funcionalidades
- 🎨 **Mejorar interfaces** y experiencia de usuario
- 📚 **Compartir casos de uso** y ejemplos

### **Cómo Contribuir**
1. **Fork** el repositorio
2. **Crear** una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. **Commit** tus cambios (`git commit -m 'Agregar nueva característica'`)
4. **Push** a la rama (`git push origin feature/nueva-caracteristica`)
5. **Abrir** un Pull Request

### **Reportar Issues**
- Usa las **plantillas de issues** disponibles
- Incluye **pasos para reproducir** el problema
- Adjunta **capturas de pantalla** si es relevante
- Especifica tu **entorno** (OS, Python version, etc.)

## 📈 Roadmap y Futuras Mejoras

### **Próximas Características**
- 🌐 **Aplicación web** con Flask/FastAPI
- 📱 **Versión móvil** con Kivy
- 🔄 **Sincronización en la nube** para configuraciones
- 🎨 **Más temas** y personalización visual
- 📊 **Analytics** de uso de las herramientas
- 🔌 **Sistema de plugins** extensible

### **Mejoras Técnicas Planificadas**
- 🧪 **Tests automatizados** con pytest
- 📦 **CI/CD pipeline** con GitHub Actions
- 📚 **Documentación** con Sphinx
- 🐳 **Containerización** con Docker
- 🔍 **Code quality** con linters y formatters

## 📄 Licencia y Términos

### **Licencia MIT**
Este proyecto está bajo la **Licencia MIT**, lo que significa que puedes:
- ✅ **Usar** el código para cualquier propósito
- ✅ **Modificar** y adaptar según tus necesidades
- ✅ **Distribuir** copias del software
- ✅ **Incluir** en proyectos comerciales

### **Términos de Uso Educativo**
- 🎓 **Fines educativos** - Diseñado para aprendizaje
- 📚 **Código abierto** - Transparente y auditable
- 🤝 **Colaborativo** - Fomenta la participación
- 🔄 **Evolutivo** - Mejora continua con feedback

## 🙏 Agradecimientos

### **Comunidad y Recursos**
- 🐍 **Python Community** - Por el lenguaje y ecosistema
- 🎨 **CustomTkinter** - Por la interfaz moderna
- 📷 **Pillow Team** - Por el procesamiento de imágenes
- 🔗 **QRCode Library** - Por la generación de códigos QR
- 📦 **PyInstaller** - Por la compilación de ejecutables

### **Inspiración y Aprendizaje**
- 📚 **Documentación oficial** de Python
- 🎥 **Tutoriales de YouTube** y cursos online
- 💬 **Stack Overflow** y foros de programación
- 🤝 **Comunidad de desarrolladores** en GitHub

## 📞 Contacto y Soporte

### **Información del Desarrollador**
- 👨‍💻 **Desarrollador**: @GermanGonzalez
- 📧 **Email**: [tu-email@ejemplo.com]
- 🐙 **GitHub**: [tu-perfil-github]
- 💼 **LinkedIn**: [tu-perfil-linkedin]

### **Canales de Soporte**
- 🐛 **Issues**: Para reportar bugs y solicitar features
- 💬 **Discussions**: Para preguntas generales y feedback
- 📧 **Email**: Para consultas privadas o colaboraciones
- 🌐 **Wiki**: Para documentación extendida

---

## 🎯 Mensaje Final

> **"Este repositorio nace del entusiasmo por crear herramientas útiles y compartir conocimiento con la comunidad. Cada línea de código representa aprendizaje, cada feature una nueva habilidad adquirida, y cada contribución una oportunidad de crecer juntos."**

### **¿Por qué este repositorio?**
- 🚀 **Automatizar** tareas repetitivas del día a día
- 🎓 **Aprender** tecnologías modernas de Python
- 🤝 **Compartir** conocimiento con otros desarrolladores
- 🔧 **Crear** herramientas realmente útiles
- 💡 **Inspirar** a otros a programar y automatizar

### **¡Únete al Proyecto!**
Si te gusta lo que ves, **no dudes en contribuir**. Ya sea con código, ideas, feedback o simplemente usando las herramientas, **tu participación hace la diferencia**.

**¡Hagamos juntos herramientas increíbles! 🚀**

---

<div align="center">

**⭐ Si este repositorio te ha sido útil, considera darle una estrella ⭐**

[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/herramientas-python.svg?style=social&label=Star)](https://github.com/tu-usuario/herramientas-python)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/herramientas-python.svg?style=social&label=Fork)](https://github.com/tu-usuario/herramientas-python/fork)

</div>