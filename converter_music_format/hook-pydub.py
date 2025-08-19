"""
Hook personalizado para PyInstaller para incluir pydub correctamente
"""

from PyInstaller.utils.hooks import collect_all, collect_submodules

# Recopilar todos los módulos de pydub
datas, binaries, hiddenimports = collect_all('pydub')

# Agregar módulos específicos que podrían no detectarse automáticamente
additional_imports = [
    'pydub.audio_segment',
    'pydub.utils',
    'pydub.effects',
    'pydub.silence',
    'pydub.playback',
    'pydub.generators',
    'pydub.exceptions'
]

# Agregar submódulos
hiddenimports.extend(collect_submodules('pydub'))
hiddenimports.extend(additional_imports)

# Eliminar duplicados
hiddenimports = list(set(hiddenimports))