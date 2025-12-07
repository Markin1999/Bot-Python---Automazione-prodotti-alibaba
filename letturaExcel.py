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
from utils import resource_path  # importa la funzione dal tuo utils.py

def letturaExcel(campo):
    # percorso corretto al file macro.xlsx
    macro_path = resource_path("file/macro.xlsx")

    df = pd.read_excel(macro_path)
    
    if campo not in df.columns:
        raise KeyError(f"letturaExcel.py/ Campo '{campo}' non trovato in macro.xlsx")
    
    return df[campo]
