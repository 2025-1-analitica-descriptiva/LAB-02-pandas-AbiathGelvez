"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_09():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Reemplazamos la fecha inválida (1999-02-29 → 1999-02-28)
    df["c3"] = df["c3"].replace("1999-02-29", "1999-02-28")

    df["year"] = pd.to_datetime(df["c3"]).dt.year.astype(str)
    return df
