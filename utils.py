import os, sys

#legge le cartelle
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

def get_output_dir(name):
    # Dove scrivere i dati
    folder = os.path.join(os.getcwd(), name)
    os.makedirs(folder, exist_ok=True)
    return folder

    

