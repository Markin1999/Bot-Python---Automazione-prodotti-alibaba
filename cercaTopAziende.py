import os
from letturaExcel import letturaExcel
import pandas as pd

def TopAziende():
    campi = letturaExcel("Ricerca")
    numero_processo = letturaExcel("NumeroProcesso")[0]
    utenti_unici = []
    for c in campi:
        fileExcel = os.path.join("file", f"{int(numero_processo)}-{c}.xlsx")
        xls = pd.ExcelFile(fileExcel)
        print(xls.sheet_names)

TopAziende()
