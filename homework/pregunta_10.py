"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_10():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df = df.sort_values(["c1", "c2"])
    rta = df.groupby("c1")["c2"].apply(lambda x: ":".join(map(str, x)))
    return rta.to_frame()
