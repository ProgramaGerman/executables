import google.generativeai as genai
import config  # Importación absoluta para compatibilidad
import sys

def analizar_codigo(codigo_usuario: str) -> str:
    """
    Envía el código de Python a la API de Gemini para ser analizado.

    Args:
        codigo_usuario: El string que contiene el código a analizar.

    Returns:
        La respuesta del modelo de IA en formato de texto.
    """
    try:
        # 1. Obtenemos la API Key de forma segura
        api_key = config.get_api_key()
        genai.configure(api_key=api_key)
        
        # 2. Creamos el modelo
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # 3. Creamos el prompt. Es la parte más importante.
        # Le damos a la IA un rol, instrucciones claras y el código.
        prompt = f"""
Eres un experto programador de Python y un asistente de revisión de código.
Tu tarea es analizar el siguiente código Python y proporcionar retroalimentación.

Por favor, identifica:
1.  **Errores de Sintaxis o Lógica:** Cualquier cosa que pueda causar que el programa falle o se comporte de manera inesperada.
2.  **Malas Prácticas:** Código que funciona pero que podría mejorarse en términos de legibilidad, eficiencia o mantenimiento.
3.  **Sugerencias de Estilo (PEP 8):** Desviaciones de las guías de estilo estándar de Python.
4.  **Recomendaciones Generales:** Cualquier otra sugerencia para mejorar la calidad del código.

Formatea tu respuesta de manera clara y estructurada, usando Markdown. Usa encabezados para cada sección.

Aquí está el código a analizar:
---
{codigo_usuario}
---
"""
        
        # 4. Generamos el contenido
        response = model.generate_content(prompt)
        
        # 5. Devolvemos la respuesta en formato de texto
        return response.text

    except Exception as e:
        print(f"Ocurrió un error al contactar la API de Gemini: {e}", file=sys.stderr)
        # Devolvemos el error como un string para que el programa principal lo maneje
        return f"Error: {e}"