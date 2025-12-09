import os, sys
from pathlib import Path
from logger import log

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # In EXE: leggi dalla cartella dove si trova l'EXE, non da _MEIPASS
        exe_dir = os.path.dirname(sys.executable)
        return os.path.join(exe_dir, relative_path)
    # In sviluppo, usa la cartella del progetto
    return os.path.join(os.path.dirname(__file__), relative_path)

def get_output_dir(name):
    if getattr(sys, 'frozen', False):  
        # Siamo in EXECUTABLE (PyInstaller)
        base_dir = Path(sys._MEIPASS)  # cartella stabilita da PyInstaller
        log(f"utils.py/ ⚙️ MODALITA' EXE - base_dir: {base_dir}")

        # Le cartelle scrivibili NON possono stare dentro _MEIPASS (solo lettura!)
        # quindi usiamo la directory dell’eseguibile:
        exe_dir = Path(sys.executable).parent
        folder = exe_dir / name

    else:
        # Siamo in sviluppo
        base_dir = Path(os.path.dirname(__file__))
        folder = base_dir / name
        log(f"utils.py/ ⚙️ MODALITA' SVILUPPO - base_dir: {base_dir}")

    log(f"utils.py/ ⚙️ Creando cartella: {folder}")
    folder.mkdir(parents=True, exist_ok=True)
    log(f"utils.py/ ✅ Cartella creata/verificata: {folder}")

    return folder