from pathlib import Path

import gradio as gr
import numpy as np
from PIL import Image


def ajustar_brillo(imagen, cambio):
    if imagen is None:
        return None

    datos = np.asarray(imagen.convert("RGB"), dtype=np.int16)
    ajustada = np.clip(datos + int(cambio), 0, 255).astype(np.uint8)
    return Image.fromarray(ajustada)


ruta_ejemplo = Path("imagenes") / "escena_urbana.png"
ejemplos = [[str(ruta_ejemplo), 35]] if ruta_ejemplo.exists() else None

demo = gr.Interface(
    fn=ajustar_brillo,
    inputs=[
        gr.Image(type="pil", label="Imagen"),
        gr.Slider(-100, 100, value=0, step=1, label="Cambio de brillo"),
    ],
    outputs=gr.Image(type="pil", label="Resultado"),
    examples=ejemplos,
    title="Laboratorio local de brillo",
)


if __name__ == "__main__":
    demo.launch()
