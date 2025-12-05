from pathlib import Path
import re
import pandas as pd

def pulisciStringa():

    out_dir = Path("filePuliti")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    files = sorted(out_dir.glob("*.xlsx"))
    if not files:
        raise FileNotFoundError("Nessun file .xlsx trovato in 'filePuliti'")

    for f in files:
        df = pd.read_excel(f, sheet_name=0)

        if 'prezzo' not in df.columns:
            print(f"⚠️ Colonna 'prezzo' non trovata durante la\ pulizia")
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

        output_file = out_dir / f"All_Pulito.xlsx"
        df.to_excel(output_file, index=False)
    return "Pulizia completata e file salvati."


if __name__ == "__main__":
    pulisciStringa()

