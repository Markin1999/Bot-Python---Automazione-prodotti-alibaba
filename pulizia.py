from pathlib import Path
import re
import pandas as pd
from utils import get_output_dir
from logger import log

def pulisciStringa():

     # input: All
    out_dir = Path(get_output_dir("All"))
    # output: filePuliti
    filepuliti = Path(get_output_dir("filePuliti"))
    out_dir.mkdir(parents=True, exist_ok=True)
    
    files = sorted(out_dir.glob("*.xlsx"))
    if not files:
        raise FileNotFoundError("pulizia.py/ Nessun file .xlsx trovato in 'All'.")
        log("pulizia.py/ Nessun file .xlsx trovato in 'All'.")

    for f in files:
        df = pd.read_excel(f, sheet_name=0)

        if 'prezzo' not in df.columns:
            log(f"pulizia.py/ ⚠️ Colonna 'prezzo' non trovata durante la\ pulizia")
            continue

        prezzi = df['prezzo'].dropna()

        nuovi_prezzi = []

        for prezzo in prezzi:
            prezzo = str(prezzo).lower()
            prezzo = re.sub(r"[-€]", " ", prezzo)  
            prezzo = re.sub(r"\s+", " ", prezzo).strip()  
            prezzo = prezzo.replace(".", "").replace(",", ".")
            numeri = [float(x.replace(",", ".")) for x in prezzo.split()]
            if len(numeri) == 2:
                prezzo_pulito = numeri[0] + numeri[1] / 2
                prezzo_pulito = round(prezzo_pulito, 2)
                nuovi_prezzi.append(prezzo_pulito)
            elif len(numeri) == 1:
                prezzo_pulito = numeri[0] * 1
                prezzo_pulito = round(prezzo_pulito, 2)
                nuovi_prezzi.append(prezzo_pulito)
            else:
                nuovi_prezzi.append(None)
            
        df.loc[df['prezzo'].notna(), 'prezzo'] = nuovi_prezzi

        output_file = filepuliti / f"All_Pulito.xlsx"
        df.to_excel(output_file, index=False)
    return "pulizia.py/ Pulizia completata e file salvati."


if __name__ == "__main__":
    pulisciStringa()

