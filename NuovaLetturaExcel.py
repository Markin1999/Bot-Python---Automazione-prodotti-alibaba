import pandas as pd


def nuovaLetturaExcel(campo: str):
    df = pd.read_excel('file/macro.xlsx')
    if campo not in df.columns:
        raise KeyError(f"Campo '{campo}' assente in macro.xlsx")
    col_values = df[campo]
    return [value for value in col_values if pd.notna(value)]
