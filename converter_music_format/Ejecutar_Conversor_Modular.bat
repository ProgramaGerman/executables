@echo off
title Conversor de Audio Universal - Modular
cd /d "%~dp0"

echo.
echo ========================================
echo   Conversor de Audio Universal
echo   Version Modular
echo ========================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor instala Python desde https://python.org
    pause
    exit /b 1
)

REM Ejecutar la aplicacion modular
echo Iniciando aplicacion...
python audio_converter_gui_modular.py

REM Si hay error, mostrar mensaje
if errorlevel 1 (
    echo.
    echo ERROR: Hubo un problema al ejecutar la aplicacion
    echo Verifica que todas las dependencias esten instaladas
    echo Ejecuta: pip install -r requirements.txt
    echo.
)

pause