# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['c:/Users/cfzzxxffsdfvxcv/Documents/Python/Practicas programas/generator_password_services/app_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('c:/Users/cfzzxxffsdfvxcv/Documents/Python/Practicas programas/generator_password_services/icons', 'icons')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app_gui',
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
    icon='c:/Users/cfzzxxffsdfvxcv/Documents/Python/Practicas programas/generator_password_services/icons/candado.ico'
)