import pandas as pd
import numpy as np
import re
import os
path = os.getcwd()


# BASE PRODUCTOS POTENCIALES
base2 = pd.read_csv("{}/files3/Base prod potenciales.zip".format(path),
                    sep="|", encoding="utf-8", dtype={"Pais": str, "Posición": str, 'Descripcion': str})

base=pd.read_csv("{}/files4/Base paises potenciales.zip".format(path),
    sep="|",encoding="utf-8")

dtype={
    "Exportaciones Colombianas en 2021 (miles USD)":int,
    "Valor Importaciones 2021 (miles USD)":int,
    "PIB USD 2022":int,
    "Exportaciones promedio 2017-2021 (miles USD)":int,
    "Importaciones promedio 2017-2021 (miles USD)":int,
    "Ranking LPI":int,
    "Población 2022 (millones)":int,
    "Promedio Desempleo (2018-2022)":float,
    "Crecimiento PIB (2018-2022)":float,
    "Diferencia Promedio exportaciones 2017-2021 (miles USD)":int,
    "Diferencia Promedio importaciones 2017-2021 (miles USD)":int}

base = base.astype(dtype2)

# Types
dtype2 = {
    "Exportaciones Colombianas en 2021 (miles USD)": int,
    "Valor Importaciones 2021 (miles USD)": int,
    "Exportaciones promedio 2017-2021 (miles USD)": int,
    "Importaciones promedio 2017-2021 (miles USD)": int,
    "Diferencia Promedio exportaciones 2017-2021 (miles USD)": int,
    "Diferencia Promedio importaciones 2017-2021 (miles USD)": int}

base2 = base2.astype(dtype2)


filt = base2[["Cadena", "Subsector"]].groupby(
    ["Cadena", "Subsector"]).sum().reset_index("Cadena")

final_dict = {}

for cadena in filt["Cadena"].unique():
    final_dict[cadena] = filt[filt["Cadena"] == cadena].index.to_list()


print(final_dict)
