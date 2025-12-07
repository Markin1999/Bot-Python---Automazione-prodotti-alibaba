import os, sys
from pathlib import Path

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # In EXE: leggi dalla cartella dove si trova l'EXE, non da _MEIPASS
        exe_dir = os.path.dirname(sys.executable)
        return os.path.join(exe_dir, relative_path)
    # In sviluppo, usa la cartella del progetto
    return os.path.join(os.path.dirname(__file__), relative_path)

def get_output_dir(name):
    # In EXE: cartelle nella directory dell'EXE
    # In sviluppo: cartelle nella root del progetto
    if hasattr(sys, '_MEIPASS'):
        exe_dir = os.path.dirname(sys.executable)
        folder = Path(exe_dir) / name
        print(f"utils.py/ ⚙️ MODALITA' EXE - exe_dir: {exe_dir}")
    else:
        folder = Path(os.path.dirname(__file__)) / name
        print(f"utils.py/ ⚙️ MODALITA' SVILUPPO - script_dir: {os.path.dirname(__file__)}")
    
    print(f"utils.py/ ⚙️ Creando cartella: {folder}")
    folder.mkdir(parents=True, exist_ok=True)
    print(f"utils.py/ ✅ Cartella creata/verificata: {folder}")
    return str(folder)