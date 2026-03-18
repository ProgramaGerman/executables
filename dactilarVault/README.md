# DactilarVault

Bóveda digital segura con autenticación biométrica.

## Características

- Autenticación biométrica por huella dactilar
- Almacenamiento seguro de archivos y contraseñas
- Interfaz moderna con CustomTkinter
- Arquitectura MVP (Model-View-Presenter)

## Requisitos

- Python 3.13+
- Lector de huella dactilar compatible (opcional para demo)

## Instalación

```powershell
uv sync
```

## Uso

```powershell
uv run python dactilarVault/main.py
```

## Desarrollo

```powershell
# Instalar dependencias de desarrollo
uv sync --group dev

# Linting
ruff check .

# Formateo
black .

# Type checking
mypy .

# Tests
pytest tests/
```
