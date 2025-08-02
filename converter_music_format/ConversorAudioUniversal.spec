# -*- mode: python ; coding: utf-8 -*-

import os
import sys

# Obtener el directorio actual
current_dir = os.path.dirname(os.path.abspath(SPEC))

# Definir todos los módulos locales que deben incluirse
local_modules = [
    'main_app',
    'config',
    'audio_converter',
    'ffmpeg_manager',
    'ui_components',
    'conversion_handlers'
]

# Módulos específicos de pydub que deben incluirse
pydub_modules = [
    'pydub',
    'pydub.audio_segment',
    'pydub.utils',
    'pydub.effects',
    'pydub.silence',
    'pydub.playback',
    'pydub.generators',
    'pydub.exceptions'
]

# Módulos de customtkinter
customtkinter_modules = [
    'customtkinter',
    'customtkinter.windows',
    'customtkinter.windows.widgets',
    'customtkinter.appearance_mode',
    'customtkinter.theme_manager',
    'customtkinter.settings',
    'customtkinter.draw_engine',
    'customtkinter.font_manager'
]

# Módulos de PIL/Pillow
pil_modules = [
    'PIL',
    'PIL.Image',
    'PIL.ImageTk',
    'PIL._tkinter_finder',
    'PIL.ImageDraw',
    'PIL.ImageFont',
    'PIL.ImageFilter'
]

# Módulos de tkinter
tkinter_modules = [
    'tkinter',
    'tkinter.filedialog',
    'tkinter.messagebox',
    'tkinter.ttk',
    'tkinter.font',
    'tkinter.constants'
]

# Módulos estándar de Python
standard_modules = [
    'threading',
    'urllib',
    'urllib.request',
    'urllib.parse',
    'zipfile',
    'shutil',
    'pathlib',
    'subprocess',
    'webbrowser',
    'warnings',
    'json',
    'tempfile',
    'wave',
    'audioop',
    'struct',
    'array',
    'io',
    'os',
    'sys',
    'platform'
]

# Crear lista completa de imports ocultos
hidden_imports = (
    local_modules + 
    pydub_modules + 
    customtkinter_modules + 
    pil_modules + 
    tkinter_modules + 
    standard_modules
)

# Datos adicionales (archivos que deben incluirse)
datas = [
    (os.path.join(current_dir, 'icons'), 'icons'),
]

# Intentar incluir pydub como paquete completo
try:
    import pydub
    pydub_path = os.path.dirname(pydub.__file__)
    datas.append((pydub_path, 'pydub'))
    print(f"Incluyendo pydub desde: {pydub_path}")
except ImportError:
    print("Advertencia: No se pudo encontrar pydub")

# Intentar incluir customtkinter como paquete completo
try:
    import customtkinter
    ctk_path = os.path.dirname(customtkinter.__file__)
    datas.append((ctk_path, 'customtkinter'))
    print(f"Incluyendo customtkinter desde: {ctk_path}")
except ImportError:
    print("Advertencia: No se pudo encontrar customtkinter")

a = Analysis(
    ['launcher.py'],
    pathex=[current_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[current_dir],  # Usar hooks personalizados
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ConversorAudioUniversal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(current_dir, 'icons', 'musica.ico'),
)