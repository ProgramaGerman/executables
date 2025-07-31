# 🎯 Generador de Códigos QR - Versión Modular

Una aplicación moderna y elegante para generar códigos QR con interfaz gráfica usando CustomTkinter.

## 📁 Estructura del Proyecto

```
qr_dactilars_pc/
├── main_app.py          # Aplicación principal
├── qr_generator.py      # Lógica de generación de QR
├── ui_components.py     # Componentes de interfaz reutilizables
├── forms.py            # Formularios específicos para cada tipo de QR
├── file_manager.py     # Gestión de archivos y configuración
├── run.py              # Punto de entrada simple
├── __init__.py         # Configuración del paquete
├── README.md           # Este archivo
└── qr_scaner.py        # Archivo original (referencia)
```

## 🚀 Características

### **Tipos de QR Soportados:**
- 📝 **Texto Simple**: Cualquier texto plano
- 🌐 **URL/Página Web**: Enlaces con validación automática
- 👤 **Información de Contacto**: Formato vCard (nombre, teléfono, email)
- 📶 **Configuración WiFi**: SSID, contraseña y tipo de seguridad
- 🎨 **QR Personalizado**: Colores y tamaños personalizables
- 📚 **Ejemplos de Aprendizaje**: Genera ejemplos automáticamente

### **Interfaz Moderna:**
- ✨ Diseño elegante con CustomTkinter
- 🌙 Modo oscuro/claro intercambiable
- 📱 Interfaz responsive y intuitiva
- 🎨 Componentes reutilizables y modulares

### **Funcionalidades Avanzadas:**
- 💾 Diálogo "Guardar Como" nativo
- 📂 Creación automática de directorios
- ⚙️ Configuración persistente
- 🔄 Gestión de archivos recientes
- ✅ Validación de formularios

## 📦 Instalación

### Dependencias requeridas:
```bash
pip install customtkinter qrcode[pil]
```

### Dependencias opcionales para mejor rendimiento:
```bash
pip install pillow
```

## 🎮 Uso

### Ejecutar la aplicación:
```bash
# Opción 1: Usando el archivo principal
python main_app.py

# Opción 2: Usando el punto de entrada
python run.py

# Opción 3: Como módulo
python -m qr_dactilars_pc
```

### Flujo de uso:
1. **Seleccionar tipo de QR** en el menú principal
2. **Completar formulario** con los datos requeridos
3. **Generar QR** presionando el botón correspondiente
4. **Visualizar resultado** en pantalla
5. **Guardar archivo** usando "Guardar Como..."

## 🏗️ Arquitectura Modular

### **main_app.py**
- Aplicación principal y coordinador
- Manejo de eventos y navegación
- Configuración de la ventana principal

### **qr_generator.py**
- Lógica pura de generación de QR
- Funciones estáticas reutilizables
- Manejo de diferentes formatos (vCard, WiFi, etc.)

### **ui_components.py**
- Componentes de interfaz reutilizables
- Widgets personalizados
- Utilidades de validación

### **forms.py**
- Formularios específicos para cada tipo de QR
- Herencia de clase base común
- Validación específica por tipo

### **file_manager.py**
- Gestión de archivos y directorios
- Configuración persistente
- Diálogos de guardar/abrir

## ⚙️ Configuración

La aplicación guarda automáticamente la configuración en `qr_app_config.json`:

```json
{
  "theme": "dark",
  "default_save_location": "",
  "recent_files": [],
  "window_size": "800x600",
  "auto_save_examples": false
}
```

## 🎨 Personalización

### Agregar nuevos tipos de QR:
1. Crear nueva clase en `forms.py` heredando de `BaseForm`
2. Implementar métodos `create_form()` y `generate_qr()`
3. Agregar función en `qr_generator.py` si es necesario
4. Registrar en el menú principal en `main_app.py`

### Modificar la interfaz:
- Editar componentes en `ui_components.py`
- Cambiar colores y temas en la configuración de CustomTkinter
- Agregar nuevos widgets reutilizables

## 🐛 Solución de Problemas

### Error de dependencias:
```bash
pip install --upgrade customtkinter qrcode[pil] pillow
```

### Error de permisos al guardar:
- Verificar permisos de escritura en la carpeta destino
- Ejecutar como administrador si es necesario

### Problemas de visualización:
- Actualizar CustomTkinter a la última versión
- Verificar compatibilidad con tu versión de Python

## 📝 Ejemplos de Uso

### Generar QR programáticamente:
```python
from qr_generator import QRGenerator

# QR de texto
image = QRGenerator.generate_text_qr("Hola Mundo")

# QR de contacto
image = QRGenerator.generate_contact_qr(
    "Juan Pérez", 
    "+1234567890", 
    "juan@email.com"
)

# QR personalizado
image = QRGenerator.generate_custom_qr(
    "Texto colorido",
    fill_color="blue",
    back_color="yellow",
    box_size=15
)
```

### Usar componentes de UI:
```python
from ui_components import FormComponents

# Crear entrada con etiqueta
entry = FormComponents.create_labeled_entry(
    parent, 
    "Nombre:", 
    "Placeholder"
)

# Crear botones de acción
FormComponents.create_action_buttons(
    parent,
    back_callback,
    generate_callback
)
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) por la interfaz moderna
- [qrcode](https://github.com/lincolnloop/python-qrcode) por la generación de QR
- [Pillow](https://pillow.readthedocs.io/) por el manejo de imágenes