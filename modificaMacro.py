from letturaExcel import letturaExcel   
from modificaExcel import modificaExcel 
from logger import log

def modificaMacro():
    numeroProcesso = letturaExcel("NumeroProcesso")[0]
    
    try:
        numeroProcesso = int(numeroProcesso)
    except (TypeError, ValueError):
        numeroProcesso = 0

    # Leggi processi e rimuovi NaN
    processi_raw = letturaExcel("Processi")
    
    if processi_raw is None:
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ❌ Errore: 'Processi' è None")
        return None
    
    try:
        processi = processi_raw.dropna()
        lunghezzaProcesso = len(processi)
    except (TypeError, AttributeError):
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ❌ Errore nel leggere 'Processi'")
        return None

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ℹ️ Nessun processo valido: valore impostato a 1 in macro.xlsx")
        return None

    # Valida che numeroProcesso sia nell'intervallo corretto
    if numeroProcesso >= lunghezzaProcesso:
        log(f"modificaMacro.py/ ⚠️ numeroProcesso ({numeroProcesso}) >= lunghezza ({lunghezzaProcesso}), resetto a 1")
        numeroProcesso = 0
        modificaExcel("A2", "1")
        return numeroProcesso

    # Incrementa con wrap-around
    if numeroProcesso < lunghezzaProcesso:
        numeroProcesso += 1
        modificaExcel("A2", str(numeroProcesso))
        log(f"modificaMacro.py/ ✅ Processo aumentato: {numeroProcesso}")
    else:
        numeroProcesso = 0
        modificaExcel("A2", str(numeroProcesso))
        log("modificaMacro.py/ ✅ Processo resettato a 0")

    log(f"modificaMacro.py/ 🔄 Nuovo numeroProcesso: {numeroProcesso}")
    
    return numeroProcesso


def menoUnoMacro():
    numeroProcesso = letturaExcel("NumeroProcesso")[0]
    
    try:
        numeroProcesso = int(numeroProcesso)
    except (TypeError, ValueError):
        numeroProcesso = 0

    # Leggi processi e rimuovi NaN
    processi_raw = letturaExcel("Processi")
    
    if processi_raw is None:
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ❌ Errore: 'Processi' è None")
        return None
    
    try:
        processi = processi_raw.dropna()
        lunghezzaProcesso = len(processi)
    except (TypeError, AttributeError):
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ❌ Errore nel leggere 'Processi'")
        return None

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "1")
        log("modificaMacro.py/ ℹ️ Nessun processo valido: valore impostato a 1 in macro.xlsx")
        return None

    # Valida che numeroProcesso sia nell'intervallo corretto
    if numeroProcesso >= lunghezzaProcesso:
        log(f"modificaMacro.py/ ⚠️ numeroProcesso ({numeroProcesso}) >= lunghezza ({lunghezzaProcesso}), resetto all'ultimo")
        numeroProcesso = lunghezzaProcesso - 1
        modificaExcel("A2", str(numeroProcesso))
        return numeroProcesso

    # Decrementa con wrap-around
    if numeroProcesso > 0:
        numeroProcesso -= 1
        modificaExcel("A2", "1")
        log(f"modificaMacro.py/ ✅ Processo diminuito: {numeroProcesso}")
    else:
        numeroProcesso = lunghezzaProcesso - 1
        modificaExcel("A2", str(numeroProcesso))
        log(f"modificaMacro.py/ ✅ Processo riportato all'ultimo: {numeroProcesso}")
    
    return numeroProcesso


if __name__ == "__main__":
    log("modificaMacro.py/ === Test modificaMacro ===")
    risultato = modificaMacro()
    log(f"modificaMacro.py/ Risultato: {risultato}\n")
    
    log("modificaMacro.py/ === Test menoUnoMacro ===")
    risultato = menoUnoMacro()
    log(f"modificaMacro.py/ Risultato: {risultato}")