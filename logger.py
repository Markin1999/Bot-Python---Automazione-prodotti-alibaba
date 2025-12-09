from pathlib import Path
import csv
from datetime import datetime
import sys
import os

from pathlib import Path
import sys
import os

def get_output_dir(name):
    if getattr(sys, 'frozen', False):
        # Modalità EXE
        exe_dir = Path(sys.executable).parent
        folder = exe_dir / name

    else:
        # Modalità sviluppo
        base_dir = Path(os.path.dirname(__file__))
        folder = base_dir / name

    folder.mkdir(parents=True, exist_ok=True)
    return folder


# Timestamp fisso per questa esecuzione del programma
_run_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def log(testo):
    log_dir = Path(get_output_dir("log"))
    
    # Usa il timestamp fisso della run, non uno nuovo ogni volta
    file_path = log_dir / f"{_run_timestamp}_log.csv"
    
    # Controlla se il file esiste per sapere se scrivere intestazione
    file_exists = file_path.exists()
    
    # Apri in modalità "a" (append) per aggiungere righe senza sovrascrivere
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Scrivi intestazione solo se il file è nuovo
        if not file_exists:
            writer.writerow(["Orario", "Log"])
        
        # Scrivi il log con timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, testo])