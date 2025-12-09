"""
import pandas as pd
from bs4 import BeautifulSoup

def letturaExcel(campo):
    df = pd.read_excel('file/macro.xlsx')
    campo = df[campo]
    return campo

"""
import pandas as pd
from bs4 import BeautifulSoup
from utils import resource_path
from logger import log

def letturaExcel(campo):
    # percorso corretto al file macro.xlsx
    macro_path = resource_path("file/macro.xlsx")
    print(f"letturaExcel.py/ Percorso del file macro.xlsx: {macro_path}")
    log(f"letturaExcel.py/ Percorso del file macro.xlsx: {macro_path}")

    df = pd.read_excel(macro_path)
    
    if campo not in df.columns:
        raise KeyError(f"letturaExcel.py/ Campo '{campo}' non trovato in macro.xlsx")
        log(f"letturaExcel.py/ ⚠️ Campo '{campo}' non trovato in macro.xlsx")
    
    return df[campo]
