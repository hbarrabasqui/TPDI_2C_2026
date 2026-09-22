# Instalación de uv

`uv` es el gestor de proyectos y dependencias de Python utilizado por este laboratorio.

## Windows

Abrir PowerShell y ejecutar el instalador oficial:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cerrar y volver a abrir la terminal. Comprobar la instalación:

```powershell
uv --version
```

También se puede consultar la [documentación oficial de instalación de uv](https://docs.astral.sh/uv/getting-started/installation/).

## macOS y Linux

Abrir una terminal y ejecutar:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reabrir la terminal y comprobar la instalación:

```bash
uv --version
```

## Uso en este laboratorio

Desde la carpeta que contiene este archivo:

```powershell
uv venv .venv --python 3.12
uv sync
```

El archivo `uv.lock` fija las versiones exactas para que todas las instalaciones sean reproducibles.

### Registrar el kernel con nombre propio

Si vas a usar varios entornos virtuales a la vez (uno por carpeta del laboratorio), registrá el kernel de este con un nombre identificable en vez del genérico "Python 3 (ipykernel)":

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-003-fundamentos --display-name "PDI 003 - Librerías Fundamentos"
```

Así aparece en el selector de kernel de VS Code/Jupyter como **"PDI 003 - Librerías Fundamentos"**, distinguible de los kernels de las otras carpetas.