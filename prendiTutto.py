from pathlib import Path
import pandas as pd
import re

src_dir = Path("PagineHtml")
out_dir = Path("All")
out_dir.mkdir(parents=True, exist_ok=True)

files = sorted(src_dir.glob("*.xlsx"))

frames = []
base_cols = None

for f in files:
    try:
        df = pd.read_excel(f, sheet_name=0)

        # Mantieni lo schema del primo file
        if base_cols is None:
            base_cols = df.columns.tolist()
        else:
            df = df.reindex(columns=base_cols)

        # Estrai numero_processo e ricerca dal nome file "<numero>-<resto>.xlsx"
        name = f.stem
        m = re.match(r"^([^-\s]+)-(.*)$", name)
        if m:
            numero_processo, ricerca = m.group(1), m.group(2)
        else:
            numero_processo, ricerca = "", name

        # Colonne di tracciamento
        df.insert(0, "file", f.name)
        df.insert(1, "numero_processo", str(numero_processo))
        df.insert(2, "ricerca", ricerca)

        frames.append(df)
    except Exception as e:
        print(f"⚠️ Errore su {f.name}: {e}")

merged = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

# Salva in Excel
output_path = out_dir / "unione.xlsx"
merged.to_excel(output_path, index=False)
print(f"✅ File creato: {output_path}")
