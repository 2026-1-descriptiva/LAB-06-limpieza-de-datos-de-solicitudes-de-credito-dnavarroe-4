"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    tabla = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")

    if "Unnamed: 0" in tabla.columns:
        tabla = tabla.drop(["Unnamed: 0"], axis=1)

    tabla = tabla.dropna().drop_duplicates()

    str_cols = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    tabla[str_cols] = tabla[str_cols].apply(
        lambda x: x.str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    tabla["monto_del_credito"] = (
        tabla["monto_del_credito"]
        .str.replace("[$ ,]", "", regex=True)
        .astype(float)
    )

    tabla["fecha_de_beneficio"] = tabla["fecha_de_beneficio"].apply(
        lambda x: "/".join(reversed(str(x).split("/")))
        if pd.notnull(x) and len(str(x).split("/")[0]) == 4
        else x
    )

    tabla = tabla.dropna().drop_duplicates()

    os.makedirs("files/output", exist_ok=True)

    tabla.to_csv("files/output/solicitudes_de_credito.csv",sep=";",index=False,)

    return tabla
