# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Configuración de rutas
project_dir = r"C:\Users\cfzzxxffsdfvxcv\Documents\Python\Practicas programas\qr_dactilars_pc"
icon_path = r"C:\Users\cfzzxxffsdfvxcv\Documents\Python\Practicas programas\qr_dactilars_pc\icons\codigo-qr.ico" if r"C:\Users\cfzzxxffsdfvxcv\Documents\Python\Practicas programas\qr_dactilars_pc\icons\codigo-qr.ico" else None

# Recopilar datos adicionales
datas = []

# Incluir archivos de iconos
icons_dir = os.path.join(project_dir, "icons")
if os.path.exists(icons_dir):
    for file in os.listdir(icons_dir):
        if file.endswith(('.ico', '.png', '.jpg', '.jpeg')):
            datas.append((os.path.join(icons_dir, file), 'icons'))

# Incluir archivos de configuración
config_files = ['qr_app_config.json']
for config_file in config_files:
    config_path = os.path.join(project_dir, config_file)
    if os.path.exists(config_path):
        datas.append((config_path, '.'))

# Módulos ocultos necesarios
hiddenimports = [
    'customtkinter',
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'tkinter.filedialog',
    'PIL',
    'PIL.Image',
    'PIL.ImageTk',
    'qrcode',
    'qrcode.image.pil',
    'qrcode.image.styledpil',
    'qrcode.constants',
    'json',
    'os',
    'sys',
    'datetime',
    'pathlib',
    're'
]

# Recopilar submódulos de customtkinter
try:
    hiddenimports.extend(collect_submodules('customtkinter'))
except:
    pass

# Recopilar submódulos de qrcode
try:
    hiddenimports.extend(collect_submodules('qrcode'))
except:
    pass

# Análisis principal
a = Analysis(
    ['run.py'],
    pathex=[project_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'jupyter',
        'IPython',
        'pytest',
        'setuptools',
        'distutils'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Filtrar archivos innecesarios
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Configuración del ejecutable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='QR_Generator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,  # Icono del ejecutable
    version_file=None,
)

# Información adicional para Windows
if sys.platform == 'win32':
    exe.version_info = {
        'FileVersion': (1, 0, 0, 0),
        'ProductVersion': (1, 0, 0, 0),
        'FileDescription': 'Generador de Códigos QR',
        'InternalName': 'QR_Generator',
        'OriginalFilename': 'QR_Generator.exe',
        'ProductName': 'QR Generator App',
        'CompanyName': 'QR Tools',
        'LegalCopyright': '© 2024 QR Tools',
    }
