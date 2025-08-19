# Debugger IA 🐛🤖

Un analizador de código Python inteligente que utiliza Google Gemini AI para encontrar errores, sugerir mejoras y verificar el cumplimiento de las mejores prácticas de programación.

## ✨ Características

- 🔍 **Análisis Inteligente**: Detecta errores de sintaxis, lógica y malas prácticas
- 🎨 **Interfaz Moderna**: Disponible en línea de comandos y GUI con Flet
- 📝 **Sugerencias PEP 8**: Verifica el cumplimiento del estilo de código Python
- 🚀 **IA Avanzada**: Powered by Google Gemini 1.5 Flash
- 📁 **Carga de Archivos**: Analiza archivos existentes o código en tiempo real

## 🛠️ Instalación

1. **Clona o descarga el proyecto**
2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configura tu API Key de Google**:
   - Obtén una API key de [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Asegúrate de que el archivo `.env` contenga:
     ```
     GOOGLE_API_KEY=tu_api_key_aqui
     ```

## 🚀 Uso

### Interfaz Gráfica (Recomendado)
```bash
python run_gui.py
```

**Características de la GUI:**
- ✅ Interfaz moderna y intuitiva
- ✅ Editor de código integrado
- ✅ Carga de archivos con explorador
- ✅ Código de ejemplo incluido
- ✅ Resultados formateados y fáciles de leer
- ✅ Indicadores de progreso

### Línea de Comandos
```bash
# Desde la raíz del proyecto
python run.py archivo_a_analizar.py

# O desde src/
cd src
python main.py ../test_code.py
```

## 📁 Estructura del Proyecto

```
debugger_ia/
├── .env                 # API key de Google
├── requirements.txt     # Dependencias
├── run.py              # CLI runner
├── run_gui.py          # GUI runner
├── test_code.py        # Código de ejemplo
└── src/
    ├── main.py         # Punto de entrada CLI
    ├── gui.py          # Interfaz gráfica
    ├── cli.py          # Lógica de línea de comandos
    ├── config.py       # Configuración y API key
    └── analizador.py   # Motor de análisis con IA
```

## 🎯 Qué Analiza

1. **Errores de Sintaxis y Lógica**
   - Errores que pueden causar fallos
   - Comportamientos inesperados

2. **Malas Prácticas**
   - Código ineficiente
   - Problemas de legibilidad
   - Dificultades de mantenimiento

3. **Estilo PEP 8**
   - Convenciones de nomenclatura
   - Espaciado y formato
   - Estructura del código

4. **Recomendaciones Generales**
   - Optimizaciones
   - Mejores patrones de diseño
   - Sugerencias de refactoring

## 🖥️ Capturas de Pantalla

### Interfaz Gráfica
- Diseño moderno con Material Design
- Editor de código con syntax highlighting
- Resultados formateados y organizados
- Carga de archivos intuitiva

### Línea de Comandos
- Análisis rápido y directo
- Perfecto para integración en workflows
- Salida detallada y estructurada

## 🔧 Requisitos

- Python 3.7+
- Conexión a Internet (para API de Google)
- API Key de Google Gemini

## 📝 Ejemplo de Uso

1. **Ejecuta la GUI**: `python run_gui.py`
2. **Carga código** usando el botón "Ejemplo" o "Cargar Archivo"
3. **Haz clic en "Analizar Código"**
4. **Revisa las sugerencias** en el panel de resultados

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras bugs o tienes ideas para mejoras, no dudes en crear un issue o pull request.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.