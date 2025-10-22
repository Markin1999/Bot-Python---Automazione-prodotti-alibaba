#funzione per cercare il testo in una stringa 
#gli passo il titolo e qui cerco la parola chiave
#deve ritornare un oggetto con parola chiave, piu le volte in cui appare.

import re
from letturaExcel import letturaExcel   

def ricercaTitolo(titolo):
    parole_chiave = letturaExcel("ParoleChiave")
    trovate = []

    for parola in parole_chiave:
        pattern = re.compile(r'\b' + re.escape(parola) + r'\b', re.IGNORECASE)
        if pattern.search(titolo):
            if parola not in trovate:
                trovate.append(parola)
        else:
            continue

    return trovate
