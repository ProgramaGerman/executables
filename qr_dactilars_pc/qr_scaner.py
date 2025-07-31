"""
Aplicación que se encarga de tomar huellas dactilares, y crea códigos QR de ejemplo para aprendizaje

Tutorial paso a paso para generar códigos QR en Python - VERSIÓN MEJORADA
"""

import qrcode
from PIL import Image
import os


def crear_directorio_si_no_existe(ruta_archivo):
    """
    Crea el directorio padre si no existe
    
    Args:
        ruta_archivo (str): Ruta completa del archivo
    """
    directorio = os.path.dirname(ruta_archivo)
    if directorio and not os.path.exists(directorio):
        try:
            os.makedirs(directorio, exist_ok=True)
            print(f"📁 Directorio creado: {directorio}")
        except OSError as e:
            print(f"❌ Error al crear directorio {directorio}: {e}")
            raise


def generar_qr_basico(texto, nombre_archivo="qr_basico.png"):
    """
    Función básica para generar un código QR simple

    Args:
        texto (str): El texto que quieres convertir en QR
        nombre_archivo (str): Nombre del archivo donde guardar el QR
    """
    print(f"📱 Generando código QR para: {texto}")

    try:
        # Crear directorio si no existe
        crear_directorio_si_no_existe(nombre_archivo)
        
        # Crear el objeto QR con configuración básica
        qr = qrcode.QRCode(
            version=1,  # Controla el tamaño (1 es el más pequeño)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
            box_size=10,  # Tamaño de cada "caja" del QR
            border=4,  # Grosor del borde
        )

        # Agregar los datos al QR
        qr.add_data(texto)
        qr.make(fit=True)

        # Crear la imagen
        imagen = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen con manejo de errores
        imagen.save(nombre_archivo)
        print(f"✅ Código QR guardado como: {nombre_archivo}")
        
        return imagen
        
    except Exception as e:
        print(f"❌ Error al generar QR: {e}")
        return None


def generar_qr_personalizado(
    texto,
    nombre_archivo="qr_personalizado.png",
    color_relleno="blue",
    color_fondo="yellow",
    tamaño=15,
):
    """
    Función para generar un código QR personalizado con colores y tamaño

    Args:
        texto (str): El texto para el QR
        nombre_archivo (str): Nombre del archivo
        color_relleno (str): Color del código QR
        color_fondo (str): Color de fondo
        tamaño (int): Tamaño de cada caja del QR
    """
    print(f"🎨 Generando código QR personalizado...")

    try:
        # Crear directorio si no existe
        crear_directorio_si_no_existe(nombre_archivo)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Mejor corrección de errores
            box_size=tamaño,
            border=4,
        )

        qr.add_data(texto)
        qr.make(fit=True)

        # Crear imagen con colores personalizados
        imagen = qr.make_image(fill_color=color_relleno, back_color=color_fondo)
        imagen.save(nombre_archivo)

        print(f"✅ QR personalizado guardado: {nombre_archivo}")
        return imagen
        
    except Exception as e:
        print(f"❌ Error al generar QR personalizado: {e}")
        return None


def generar_qr_url(url, nombre_archivo="qr_url.png"):
    """
    Función específica para generar QR de URLs

    Args:
        url (str): La URL que quieres convertir en QR
        nombre_archivo (str): Nombre del archivo
    """
    print(f"🌐 Generando código QR para URL: {url}")

    # Verificar que la URL tenga el formato correcto
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        print(f"📝 URL corregida a: {url}")

    return generar_qr_basico(url, nombre_archivo)


def generar_qr_contacto(nombre, telefono, email, nombre_archivo="qr_contacto.png"):
    """
    Función para generar un QR con información de contacto (formato vCard)

    Args:
        nombre (str): Nombre del contacto
        telefono (str): Número de teléfono
        email (str): Correo electrónico
        nombre_archivo (str): Nombre del archivo
    """
    print(f"👤 Generando código QR de contacto para: {nombre}")

    # Formato vCard para información de contacto
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{nombre}
TEL:{telefono}
EMAIL:{email}
END:VCARD"""

    return generar_qr_basico(vcard, nombre_archivo)


def generar_qr_wifi(ssid, password, seguridad="WPA", nombre_archivo="qr_wifi.png"):
    """
    Función para generar un QR que conecte automáticamente a WiFi

    Args:
        ssid (str): Nombre de la red WiFi
        password (str): Contraseña de la red
        seguridad (str): Tipo de seguridad (WPA, WEP, nopass)
        nombre_archivo (str): Nombre del archivo
    """
    print(f"📶 Generando código QR para WiFi: {ssid}")

    # Formato especial para WiFi
    wifi_config = f"WIFI:T:{seguridad};S:{ssid};P:{password};;"

    return generar_qr_basico(wifi_config, nombre_archivo)


def obtener_nombre_archivo_seguro():
    """
    Función para obtener un nombre de archivo válido del usuario
    """
    while True:
        nombre = input("📁 Nombre del archivo (ej: mi_qr.png o carpeta/mi_qr.png): ").strip()
        
        if not nombre:
            nombre = "qr_generado.png"
            print(f"📝 Usando nombre por defecto: {nombre}")
            
        # Agregar extensión .png si no la tiene
        if not nombre.lower().endswith('.png'):
            nombre += '.png'
            print(f"📝 Extensión agregada: {nombre}")
            
        return nombre


def menu_interactivo():
    """
    Menú interactivo para que el usuario elija qué tipo de QR generar
    """
    print("\n" + "=" * 50)
    print("🎯 GENERADOR DE CÓDIGOS QR - TUTORIAL MEJORADO")
    print("=" * 50)

    while True:
        print("\n¿Qué tipo de código QR quieres generar?")
        print("1. 📝 Texto simple")
        print("2. 🌐 URL/Página web")
        print("3. 👤 Información de contacto")
        print("4. 📶 Configuración WiFi")
        print("5. 🎨 QR personalizado (con colores)")
        print("6. 📚 Generar ejemplos de aprendizaje")
        print("7. 🚪 Salir")

        opcion = input("\nElige una opción (1-7): ").strip()

        try:
            if opcion == "1":
                texto = input("📝 Escribe el texto para el QR: ")
                nombre_archivo = obtener_nombre_archivo_seguro()
                generar_qr_basico(texto, nombre_archivo)

            elif opcion == "2":
                url = input("🌐 Escribe la URL: ")
                nombre_archivo = obtener_nombre_archivo_seguro()
                generar_qr_url(url, nombre_archivo)

            elif opcion == "3":
                nombre = input("👤 Nombre del contacto: ")
                telefono = input("📞 Teléfono: ")
                email = input("📧 Email: ")
                nombre_archivo = obtener_nombre_archivo_seguro()
                generar_qr_contacto(nombre, telefono, email, nombre_archivo)

            elif opcion == "4":
                ssid = input("📶 Nombre de la red WiFi: ")
                password = input("🔒 Contraseña: ")
                nombre_archivo = obtener_nombre_archivo_seguro()
                generar_qr_wifi(ssid, password, "WPA", nombre_archivo)

            elif opcion == "5":
                texto = input("📝 Texto para el QR: ")
                color1 = input("🎨 Color del QR (ej: red, blue, green): ") or "black"
                color2 = input("🎨 Color de fondo (ej: white, yellow, pink): ") or "white"
                nombre_archivo = obtener_nombre_archivo_seguro()
                generar_qr_personalizado(texto, nombre_archivo, color1, color2)

            elif opcion == "6":
                ejemplos_de_aprendizaje()

            elif opcion == "7":
                print("👋 ¡Hasta luego! Gracias por usar el generador de QR")
                break

            else:
                print("❌ Opción no válida. Por favor elige entre 1-7")

        except KeyboardInterrupt:
            print("\n\n⏹️ Operación cancelada por el usuario")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

        input("\n⏸️  Presiona Enter para continuar...")


def ejemplos_de_aprendizaje():
    """
    Función que genera varios ejemplos para aprender
    """
    print("📚 Generando ejemplos de códigos QR para aprendizaje...")

    try:
        # Crear carpeta para ejemplos si no existe (ahora es más seguro)
        carpeta_ejemplos = "ejemplos_qr"
        if not os.path.exists(carpeta_ejemplos):
            os.makedirs(carpeta_ejemplos, exist_ok=True)
            print(f"📁 Carpeta creada: {carpeta_ejemplos}")

        # Ejemplo 1: Texto simple
        generar_qr_basico(
            "¡Hola! Este es mi primer código QR", 
            f"{carpeta_ejemplos}/ejemplo1_texto.png"
        )

        # Ejemplo 2: URL
        generar_qr_url(
            "https://www.python.org", 
            f"{carpeta_ejemplos}/ejemplo2_url.png"
        )

        # Ejemplo 3: Contacto
        generar_qr_contacto(
            "Juan Pérez",
            "+1234567890",
            "juan@email.com",
            f"{carpeta_ejemplos}/ejemplo3_contacto.png",
        )

        # Ejemplo 4: WiFi
        generar_qr_wifi(
            "MiWiFi", 
            "contraseña123", 
            "WPA", 
            f"{carpeta_ejemplos}/ejemplo4_wifi.png"
        )

        # Ejemplo 5: QR personalizado
        generar_qr_personalizado(
            "Código QR Colorido!",
            f"{carpeta_ejemplos}/ejemplo5_colores.png",
            "purple",
            "lightblue",
            12,
        )

        print(f"✅ ¡Todos los ejemplos generados en la carpeta '{carpeta_ejemplos}'!")
        
    except Exception as e:
        print(f"❌ Error al generar ejemplos: {e}")


def verificar_dependencias():
    """
    Verifica que las librerías necesarias estén instaladas
    """
    try:

        print("✅ Todas las dependencias están instaladas")
        return True
    except ImportError as e:
        print(f"❌ Falta instalar dependencias: {e}")
        print("💡 Ejecuta: pip install qrcode[pil]")
        return False


if __name__ == "__main__":
    print("🚀 Iniciando el generador de códigos QR...")
    
    # Verificar dependencias antes de empezar
    if not verificar_dependencias():
        print("⚠️ Por favor instala las dependencias antes de continuar")
        exit(1)
    
    # Iniciar el menú interactivo
    menu_interactivo()