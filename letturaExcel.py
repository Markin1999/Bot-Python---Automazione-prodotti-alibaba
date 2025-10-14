import pandas as pd

def letturaExcel(campo):
    
    df = pd.read_excel('file/macro.xlsx')

    campo = df[campo]
    

    return campo

