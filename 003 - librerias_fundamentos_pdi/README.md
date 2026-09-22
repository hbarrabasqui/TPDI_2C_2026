# Fundamentos de Procesamiento Digital de Imágenes

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Material de laboratorio sobre librerías fundamentales para el procesamiento digital de imágenes. Esta carpeta puede compartirse de manera independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `001 - entorno y librerias.ipynb`: configuración y reconocimiento del entorno.
- `002 - imagenes en color y canales.ipynb`: imágenes en color y sus canales.
- `003 - operaciones basicas con opencv.ipynb`: operaciones iniciales con OpenCV.
- `004 - muestreo y cuantizacion.ipynb`: muestreo y cuantización.
- `005 - practica guiada de procesamiento de imagenes.ipynb`: práctica guiada.
- `006 - laboratorio 2 - segmentacion simple por color.ipynb`: segmentación simple por color.
- `007 - recuperacion y preprocesamiento de imagenes propias.ipynb`: recuperación y preprocesamiento.
- `008 - actividad integradora - segmentacion por color.ipynb`: actividad integradora.

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, opencv-python, pillow, scikit-image, matplotlib) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-003-fundamentos --display-name "PDI 003 - Librerías Fundamentos"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 003 - Librerías Fundamentos"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

También se puede ejecutar código sin activar el entorno:

```powershell
uv run python -c "import cv2, numpy; print('OpenCV y NumPy instalados correctamente')"
```

## Abrir los notebooks

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv\Scripts\python.exe` (Windows) o `.venv/bin/python` (macOS/Linux) como intérprete/kernel.

Si preferís Jupyter Lab en el navegador, se puede levantar sin agregarlo como dependencia permanente del proyecto:

```powershell
uv run --with jupyter jupyter lab
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
uv lock --upgrade
uv sync
```

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```
