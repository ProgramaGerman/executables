"""
Módulo para la generación de códigos QR
Contiene todas las funciones de generación de QR del proyecto original
"""

import qrcode
from PIL import Image
import os


class QRGenerator:
    """Clase para generar diferentes tipos de códigos QR"""
    
    @staticmethod
    def create_directory_if_not_exists(file_path):
        """
        Crea el directorio padre si no existe
        
        Args:
            file_path (str): Ruta completa del archivo
        """
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
                return True
            except OSError as e:
                raise Exception(f"Error al crear directorio {directory}: {e}")
        return True

    @staticmethod
    def generate_basic_qr(data, fill_color="black", back_color="white", box_size=10):
        """
        Genera un código QR básico
        
        Args:
            data (str): Datos para el QR
            fill_color (str): Color del QR
            back_color (str): Color de fondo
            box_size (int): Tamaño de cada caja del QR
            
        Returns:
            PIL.Image: Imagen del QR generado
        """
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=box_size,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            image = qr.make_image(fill_color=fill_color, back_color=back_color)
            return image
            
        except Exception as e:
            raise Exception(f"Error al generar QR: {e}")

    @staticmethod
    def generate_text_qr(text, filename=None):
        """
        Genera QR de texto simple
        
        Args:
            text (str): Texto para el QR
            filename (str, optional): Nombre del archivo para guardar
            
        Returns:
            PIL.Image: Imagen del QR
        """
        image = QRGenerator.generate_basic_qr(text)
        
        if filename:
            QRGenerator.create_directory_if_not_exists(filename)
            image.save(filename)
            
        return image

    @staticmethod
    def generate_url_qr(url, filename=None):
        """
        Genera QR de URL
        
        Args:
            url (str): URL para el QR
            filename (str, optional): Nombre del archivo para guardar
            
        Returns:
            PIL.Image: Imagen del QR
        """
        # Verificar que la URL tenga el formato correcto
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            
        image = QRGenerator.generate_basic_qr(url)
        
        if filename:
            QRGenerator.create_directory_if_not_exists(filename)
            image.save(filename)
            
        return image

    @staticmethod
    def generate_contact_qr(name, phone, email, filename=None):
        """
        Genera QR de contacto en formato vCard
        
        Args:
            name (str): Nombre del contacto
            phone (str): Teléfono
            email (str): Email
            filename (str, optional): Nombre del archivo para guardar
            
        Returns:
            PIL.Image: Imagen del QR
        """
        vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
        
        image = QRGenerator.generate_basic_qr(vcard)
        
        if filename:
            QRGenerator.create_directory_if_not_exists(filename)
            image.save(filename)
            
        return image

    @staticmethod
    def generate_wifi_qr(ssid, password, security="WPA", filename=None):
        """
        Genera QR de configuración WiFi
        
        Args:
            ssid (str): Nombre de la red WiFi
            password (str): Contraseña
            security (str): Tipo de seguridad (WPA, WEP, nopass)
            filename (str, optional): Nombre del archivo para guardar
            
        Returns:
            PIL.Image: Imagen del QR
        """
        wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"
        
        image = QRGenerator.generate_basic_qr(wifi_config)
        
        if filename:
            QRGenerator.create_directory_if_not_exists(filename)
            image.save(filename)
            
        return image

    @staticmethod
    def generate_custom_qr(text, fill_color="black", back_color="white", box_size=10, filename=None):
        """
        Genera QR personalizado con colores y tamaño específicos
        
        Args:
            text (str): Texto para el QR
            fill_color (str): Color del QR
            back_color (str): Color de fondo
            box_size (int): Tamaño de cada caja
            filename (str, optional): Nombre del archivo para guardar
            
        Returns:
            PIL.Image: Imagen del QR
        """
        image = QRGenerator.generate_basic_qr(text, fill_color, back_color, box_size)
        
        if filename:
            QRGenerator.create_directory_if_not_exists(filename)
            image.save(filename)
            
        return image

    @staticmethod
    def generate_examples(output_folder="ejemplos_qr"):
        """
        Genera ejemplos de códigos QR para aprendizaje
        
        Args:
            output_folder (str): Carpeta donde guardar los ejemplos
            
        Returns:
            list: Lista de archivos generados
        """
        try:
            # Crear carpeta si no existe
            if not os.path.exists(output_folder):
                os.makedirs(output_folder, exist_ok=True)
                
            generated_files = []
            
            # Ejemplo 1: Texto simple
            filename1 = os.path.join(output_folder, "ejemplo1_texto.png")
            QRGenerator.generate_text_qr("¡Hola! Este es mi primer código QR", filename1)
            generated_files.append(filename1)
            
            # Ejemplo 2: URL
            filename2 = os.path.join(output_folder, "ejemplo2_url.png")
            QRGenerator.generate_url_qr("https://www.python.org", filename2)
            generated_files.append(filename2)
            
            # Ejemplo 3: Contacto
            filename3 = os.path.join(output_folder, "ejemplo3_contacto.png")
            QRGenerator.generate_contact_qr("Juan Pérez", "+1234567890", "juan@email.com", filename3)
            generated_files.append(filename3)
            
            # Ejemplo 4: WiFi
            filename4 = os.path.join(output_folder, "ejemplo4_wifi.png")
            QRGenerator.generate_wifi_qr("MiWiFi", "contraseña123", "WPA", filename4)
            generated_files.append(filename4)
            
            # Ejemplo 5: QR personalizado
            filename5 = os.path.join(output_folder, "ejemplo5_colores.png")
            QRGenerator.generate_custom_qr("Código QR Colorido!", "purple", "lightblue", 12, filename5)
            generated_files.append(filename5)
            
            return generated_files
            
        except Exception as e:
            raise Exception(f"Error al generar ejemplos: {e}")