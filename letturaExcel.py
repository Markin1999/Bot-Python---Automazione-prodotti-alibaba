import pandas as pd
from bs4 import BeautifulSoup

def letturaExcel(campo):
    df = pd.read_excel('file/macro.xlsx')
    campo = df[campo]
    return campo

