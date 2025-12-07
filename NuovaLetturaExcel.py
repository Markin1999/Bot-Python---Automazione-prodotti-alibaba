"""
import pandas as pd
from utils import resource_path



def nuovaLetturaExcel(campo: str):
    df = pd.read_excel('file/macro.xlsx')
    if campo not in df.columns:
        raise KeyError(f"nuovaLetturaExcel.py/ Campo '{campo}' assente in macro.xlsx")
    col_values = df[campo]
    return [value for value in col_values if pd.notna(value)]
"""

import pandas as pd
from utils import resource_path


def nuovaLetturaExcel(campo: str):
    # Percorso corretto al file macro.xlsx sia in exe che in sviluppo
    macro_path = resource_path("file/macro.xlsx")
    print(f"nuovaLetturaExcel.py/ Percorso del file macro.xlsx: {macro_path}")

    df = pd.read_excel(macro_path)

    if campo not in df.columns:
        raise KeyError(f"nuovaLetturaExcel.py/ Campo '{campo}' assente in macro.xlsx")

    col_values = df[campo]
    return [value for value in col_values if pd.notna(value)]
