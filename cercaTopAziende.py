

from pathlib import Path
import pandas as pd
import re

def TopAziende():

    out_dir = Path("All")
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(out_dir.glob("*.xlsx"))
    if not files:
        raise FileNotFoundError("Nessun file .xlsx trovato in 'All'")

    for f in files:
        df = pd.read_excel(f, sheet_name=0)

        if 'azienda' not in df.columns:
            print(f"⚠️ Colonna 'azienda' non trovata in {f.name}")
            continue

        conteggi = {}

        for nome, ricerca_corrente, prezzo_corrente in zip(df['azienda'], df['ricerca'], df['prezzo']):
            if pd.isna(nome) or pd.isna(ricerca_corrente) or pd.isna(prezzo_corrente):
                continue  # salta celle vuote

            if nome not in conteggi:
                conteggi[nome] = {"volte": 1, "ricerche": [ricerca_corrente], "prezzo_medio": prezzo_corrente}
            else:
                conteggi[nome]["volte"] += 1
                conteggi[nome]["prezzo_medio"] = (conteggi[nome]["prezzo_medio"] + prezzo_corrente) / 2
                if ricerca_corrente not in conteggi[nome]["ricerche"]:
                    conteggi[nome]["ricerche"].append(ricerca_corrente)

        tutteLeAziende = [
            {
                "azienda": k,
                "volte in cui appare": v["volte"],
                "ricerche": ", ".join(v["ricerche"]),
                "prezzo": v["prezzo_medio"]  
            }
            for k, v in conteggi.items()
        ]

        
        top = pd.DataFrame(tutteLeAziende)
        top.sort_values(by="volte in cui appare", ascending=False, inplace=True)



        output_file = out_dir / "topAziende.xlsx"
        top.to_excel(output_file, index=False)
        print(f"✅ File salvato: {output_file}")
    return "Pulizia completata e file salvati."

TopAziende()
