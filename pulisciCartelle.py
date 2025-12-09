def pulisciCartelle(): 
    """
    Pulisce le cartelle di lavoro rimuovendo file temporanei e non necessari.
    """
    import os
    import shutil
    from pathlib import Path
    from utils import resource_path
    from logger import log

    # Definisci le cartelle da pulire
    cartelle_da_pulire = [
    Path(resource_path("PagineHtml")),
    Path(resource_path("All")),
    Path(resource_path("filePuliti"))
    ]

    for cartella in cartelle_da_pulire:
        if cartella.exists() and cartella.is_dir():
            log(f"PulisciCartelle.py/ 🧹 Pulizia della cartella: {cartella}")
            for item in cartella.iterdir():
                try:
                    if item.is_file():
                        item.unlink()  # Rimuovi il file
                    elif item.is_dir():
                        shutil.rmtree(item)  # Rimuovi la directory e tutto il suo contenuto
                except Exception as e:
                    log(f"PulisciCartelle.py/ ❌ Errore durante la rimozione di {item}: {e}")
        else:
            log(f"PulisciCartelle.py/ ⚠️ La cartella {cartella} non esiste o non è una directory.")
