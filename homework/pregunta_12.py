"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_12():
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    df = df.sort_values(["c0", "c5a"])  # Ordena solo por la letra
    rta = df.groupby("c0")["c5"].apply(lambda x: ",".join(x)).reset_index()
    return rta