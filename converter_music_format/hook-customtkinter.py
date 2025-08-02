"""
Hook personalizado para PyInstaller para incluir customtkinter correctamente
"""

from PyInstaller.utils.hooks import collect_all, collect_submodules, collect_data_files

# Recopilar todos los módulos de customtkinter
datas, binaries, hiddenimports = collect_all('customtkinter')

# Recopilar archivos de datos (temas, fuentes, etc.)
datas += collect_data_files('customtkinter')

# Agregar submódulos específicos
additional_imports = [
    'customtkinter.windows',
    'customtkinter.windows.widgets',
    'customtkinter.appearance_mode',
    'customtkinter.theme_manager',
    'customtkinter.settings',
    'customtkinter.draw_engine',
    'customtkinter.font_manager'
]

# Agregar todos los submódulos
hiddenimports.extend(collect_submodules('customtkinter'))
hiddenimports.extend(additional_imports)

# Eliminar duplicados
hiddenimports = list(set(hiddenimports))