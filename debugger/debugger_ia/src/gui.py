import flet as ft
import os
from pathlib import Path
import analizador

class DebuggerApp:
    def __init__(self):
        self.page = None
        self.code_input = None
        self.result_output = None
        self.file_picker = None
        self.analyze_button = None
        self.progress_ring = None
        self.status_text = None
        self.theme_button = None
        
    def main(self, page: ft.Page):
        self.page = page
        page.title = "Debugger IA - Analizador de Código Python"
        page.theme_mode = ft.ThemeMode.DARK
        page.window_width = 1200
        page.window_height = 800
        page.window_min_width = 800
        page.window_min_height = 600
        page.padding = 20
        page.scroll = ft.ScrollMode.AUTO  # Habilitar scroll en toda la página
        
        # Configurar icono de la aplicación
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "icons", "bug.ico")
            if os.path.exists(icon_path):
                page.window_icon = icon_path
        except Exception as e:
            # Silenciosamente continuar si no se puede cargar el icono
            pass
        
        # Configurar el FilePicker
        self.file_picker = ft.FilePicker(
            on_result=self.on_file_picked
        )
        page.overlay.append(self.file_picker)
        
        # Crear componentes de la interfaz
        self.create_components()
        
        # Layout principal con scroll
        main_content = ft.Column([
            # Header con botón de tema
            ft.Container(
                content=ft.Row([
                    ft.Row([
                        ft.Icon(ft.Icons.BUG_REPORT, size=40, color=ft.Colors.LIME_600),
                        ft.Text(
                            "Debugger IA",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.LIME_600
                        ),
                        ft.Text(
                            "Analizador de Código Python con IA",
                            size=16,
                            color=ft.Colors.GREY_400
                        )
                    ], alignment=ft.MainAxisAlignment.START),
                    
                    # Botón para cambiar tema
                    self.theme_button
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                margin=ft.margin.only(bottom=20)
            ),
            
            # Área de entrada de código
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Código Python", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Row([
                            ft.ElevatedButton(
                                "Cargar Archivo",
                                icon=ft.Icons.FOLDER_OPEN,
                                on_click=self.pick_file,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.LIME_700,
                                    color=ft.Colors.WHITE
                                )
                            ),
                            ft.ElevatedButton(
                                "Ejemplo",
                                icon=ft.Icons.CODE,
                                on_click=self.load_example,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.LIME_800,
                                    color=ft.Colors.WHITE
                                )
                            )
                        ])
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    self.code_input
                ]),
                bgcolor=ft.Colors.GREY_900,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.LIME_600),
                margin=ft.margin.only(bottom=20)
            ),
            
            # Botón de análisis y estado
            ft.Container(
                content=ft.Row([
                    self.analyze_button,
                    self.progress_ring,
                    self.status_text
                ], alignment=ft.MainAxisAlignment.CENTER),
                margin=ft.margin.only(bottom=20)
            ),
            
            # Área de resultados con scroll mejorado
            ft.Container(
                content=ft.Column([
                    ft.Text("Resultado del Análisis", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    self.result_output
                ]),
                bgcolor=ft.Colors.GREY_900,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.LIME_600),
                height=400,  # Altura fija para el área de resultados
                expand=False
            )
        ], 
        scroll=ft.ScrollMode.AUTO,  # Scroll en la columna principal
        spacing=0
        )
        
        page.add(main_content)
    
    def create_components(self):
        # Botón para cambiar tema
        self.theme_button = ft.IconButton(
            icon=ft.Icons.LIGHT_MODE,
            tooltip="Cambiar a tema claro",
            on_click=self.toggle_theme,
            icon_color=ft.Colors.LIME_600
        )
        
        # Campo de entrada de código
        self.code_input = ft.TextField(
            multiline=True,
            min_lines=12,
            max_lines=15,
            hint_text="Pega tu código Python aquí o carga un archivo...",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
            border_color=ft.Colors.LIME_700,
            focused_border_color=ft.Colors.LIME_500,
            text_style=ft.TextStyle(
                font_family="Consolas, Monaco, monospace",
                color=ft.Colors.WHITE
            ),
            bgcolor=ft.Colors.GREY_800,
            color=ft.Colors.WHITE
        )
        
        # Área de resultados con scroll
        self.result_output = ft.Container(
            content=ft.Column([
                ft.Text(
                    "Los resultados del análisis aparecerán aquí...",
                    color=ft.Colors.GREY_500,
                    italic=True
                )
            ], 
            scroll=ft.ScrollMode.ALWAYS,  # Siempre mostrar scroll
            spacing=10
            ),
            height=320,  # Altura fija
            padding=15,
            bgcolor=ft.Colors.GREY_800,
            border_radius=8,
            border=ft.border.all(1, ft.Colors.GREY_700)
        )
        
        # Botón de análisis
        self.analyze_button = ft.ElevatedButton(
            "🔍 Analizar Código",
            icon=ft.Icons.ANALYTICS,
            on_click=self.analyze_code,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.LIME_600,
                color=ft.Colors.BLACK,
                padding=ft.padding.symmetric(horizontal=40, vertical=20),
                text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)
            ),
            height=60
        )
        
        # Indicador de progreso
        self.progress_ring = ft.ProgressRing(
            width=35,
            height=35,
            visible=False,
            color=ft.Colors.LIME_600
        )
        
        # Texto de estado
        self.status_text = ft.Text(
            "",
            color=ft.Colors.GREY_400,
            visible=False,
            size=14
        )
    
    def toggle_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_button.icon = ft.Icons.DARK_MODE
            self.theme_button.tooltip = "Cambiar a tema oscuro"
            # Actualizar colores para tema claro
            self.update_theme_colors(True)
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_button.icon = ft.Icons.LIGHT_MODE
            self.theme_button.tooltip = "Cambiar a tema claro"
            # Actualizar colores para tema oscuro
            self.update_theme_colors(False)
        
        self.page.update()
    
    def update_theme_colors(self, is_light):
        # Esta función actualizaría los colores dinámicamente
        # Por simplicidad, mantenemos el tema oscuro como principal
        pass
    
    def pick_file(self, e):
        self.file_picker.pick_files(
            dialog_title="Seleccionar archivo Python",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["py"]
        )
    
    def on_file_picked(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.code_input.value = content
                self.page.update()
                self.show_status(f"✅ Archivo cargado: {os.path.basename(file_path)}", ft.Colors.LIME_500)
            except Exception as ex:
                self.show_status(f"❌ Error al cargar archivo: {str(ex)}", ft.Colors.RED_500)
    
    def load_example(self, e):
        example_code = '''# Archivo de ejemplo para ser analizado.

def add(a: int,b: int):
  # Esta función suma dos números
  result = a+b
  return result

x = 10
y = 5
print('The sum is', add(x,y))

# Esta es una variable no utilizada
unused = 'hello'

class myclass:
    def __init__(self):
        print("Clase creada")'''
        
        self.code_input.value = example_code
        self.page.update()
        self.show_status("✅ Código de ejemplo cargado", ft.Colors.LIME_500)
    
    def show_status(self, message, color=ft.Colors.GREY_400):
        self.status_text.value = message
        self.status_text.color = color
        self.status_text.visible = True
        self.page.update()
        
        # Ocultar el mensaje después de 4 segundos
        import threading
        def hide_status():
            import time
            time.sleep(4)
            if self.status_text.visible:
                self.status_text.visible = False
                self.page.update()
        
        threading.Thread(target=hide_status, daemon=True).start()
    
    def analyze_code(self, e):
        if not self.code_input.value or not self.code_input.value.strip():
            self.show_status("⚠️ Por favor, ingresa código para analizar", ft.Colors.ORANGE_500)
            return
        
        # Mostrar indicador de carga
        self.analyze_button.disabled = True
        self.analyze_button.text = "🔄 Analizando..."
        self.progress_ring.visible = True
        self.status_text.value = "🤖 Analizando código con IA..."
        self.status_text.color = ft.Colors.LIME_500
        self.status_text.visible = True
        self.page.update()
        
        try:
            # Realizar análisis
            resultado = analizador.analizar_codigo(self.code_input.value)
            
            # Mostrar resultado
            self.display_result(resultado)
            self.show_status("✅ Análisis completado exitosamente", ft.Colors.LIME_500)
            
        except Exception as ex:
            error_msg = f"❌ Error durante el análisis: {str(ex)}"
            self.display_result(error_msg)
            self.show_status("❌ Error en el análisis", ft.Colors.RED_500)
        
        finally:
            # Restaurar botón
            self.analyze_button.disabled = False
            self.analyze_button.text = "🔍 Analizar Código"
            self.progress_ring.visible = False
            self.page.update()
    
    def display_result(self, result_text):
        # Limpiar resultado anterior
        self.result_output.content = ft.Column([], 
                                             scroll=ft.ScrollMode.ALWAYS,
                                             spacing=8)
        
        # Dividir el resultado en líneas para mejor formato
        lines = result_text.split('\n')
        formatted_content = []
        
        for line in lines:
            if line.startswith('# ') or line.startswith('## '):
                # Encabezados
                level = 1 if line.startswith('# ') else 2
                formatted_content.append(
                    ft.Container(
                        content=ft.Text(
                            line.replace('#', '').strip(),
                            size=20 if level == 1 else 16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.LIME_400
                        ),
                        margin=ft.margin.only(top=15 if level == 1 else 10, bottom=5),
                        padding=ft.padding.only(left=5),
                        border=ft.border.only(left=ft.BorderSide(3, ft.Colors.LIME_600))
                    )
                )
            elif line.startswith('**') and line.endswith('**'):
                # Texto en negrita
                formatted_content.append(
                    ft.Text(
                        line.replace('**', ''),
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        size=15
                    )
                )
            elif line.strip().startswith('-') or line.strip().startswith('*'):
                # Lista
                formatted_content.append(
                    ft.Container(
                        content=ft.Text(
                            line,
                            color=ft.Colors.GREY_300,
                            size=14
                        ),
                        margin=ft.margin.only(left=10)
                    )
                )
            elif line.strip().startswith('```'):
                # Código (ignorar marcadores)
                continue
            elif line.strip():
                # Texto normal
                formatted_content.append(
                    ft.Text(
                        line,
                        color=ft.Colors.GREY_200,
                        size=14,
                        selectable=True
                    )
                )
            else:
                # Línea vacía
                formatted_content.append(ft.Container(height=8))
        
        self.result_output.content.controls = formatted_content
        self.page.update()

def main():
    app = DebuggerApp()
    ft.app(target=app.main)