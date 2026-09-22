# Instalación de Visual Studio Code

Visual Studio Code permite trabajar con los notebooks y seleccionar el entorno virtual del laboratorio como kernel de Python.

## Instalar Visual Studio Code

Descargar e instalar [Visual Studio Code desde el sitio oficial](https://code.visualstudio.com/download).

Durante la instalación en Windows, es conveniente habilitar las opciones para agregar VS Code al PATH y al menú contextual del Explorador de archivos.

## Instalar las extensiones

En VS Code, abrir la vista de extensiones con `Ctrl+Shift+X` y buscar e instalar:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), de Microsoft.
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), de Microsoft.
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), de Microsoft.

La extensión Python permite seleccionar el intérprete y trabajar con el entorno virtual. Pylance proporciona análisis y autocompletado de Python. Jupyter permite abrir y ejecutar los notebooks `.ipynb`.

## Seleccionar el entorno del laboratorio

1. Abrir esta carpeta en VS Code.
2. Ejecutar `Python: Select Interpreter` desde la paleta de comandos (`Ctrl+Shift+P`).
3. Seleccionar `\.venv\Scripts\python.exe` en Windows o `.venv/bin/python` en macOS/Linux.
4. Abrir un notebook y seleccionar el mismo entorno como kernel.