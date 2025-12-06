from letturaExcel import letturaExcel   
from modificaExcel import modificaExcel 

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
        print("modificaMacro.py/ ❌ Errore: 'Processi' è None")
        return None
    
    try:
        processi = processi_raw.dropna()
        lunghezzaProcesso = len(processi)
    except (TypeError, AttributeError):
        modificaExcel("A2", "1")
        print("modificaMacro.py/ ❌ Errore nel leggere 'Processi'")
        return None

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "1")
        print("modificaMacro.py/ ℹ️ Nessun processo valido: valore impostato a 1 in macro.xlsx")
        return None

    # Valida che numeroProcesso sia nell'intervallo corretto
    if numeroProcesso >= lunghezzaProcesso:
        print(f"modificaMacro.py/ ⚠️ numeroProcesso ({numeroProcesso}) >= lunghezza ({lunghezzaProcesso}), resetto a 1")
        numeroProcesso = 0
        modificaExcel("A2", "1")
        return numeroProcesso

    # Incrementa con wrap-around
    if numeroProcesso < lunghezzaProcesso - 1:
        numeroProcesso += 1
        modificaExcel("A2", str(numeroProcesso))
        print(f"modificaMacro.py/ ✅ Processo aumentato: {numeroProcesso}")
    else:
        numeroProcesso = 0
        modificaExcel("A2", str(numeroProcesso))
        print("modificaMacro.py/ ✅ Processo resettato a 1")
    
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
        print("modificaMacro.py/ ❌ Errore: 'Processi' è None")
        return None
    
    try:
        processi = processi_raw.dropna()
        lunghezzaProcesso = len(processi)
    except (TypeError, AttributeError):
        modificaExcel("A2", "1")
        print("modificaMacro.py/ ❌ Errore nel leggere 'Processi'")
        return None

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "1")
        print("modificaMacro.py/ ℹ️ Nessun processo valido: valore impostato a 1 in macro.xlsx")
        return None

    # Valida che numeroProcesso sia nell'intervallo corretto
    if numeroProcesso >= lunghezzaProcesso:
        print(f"modificaMacro.py/ ⚠️ numeroProcesso ({numeroProcesso}) >= lunghezza ({lunghezzaProcesso}), resetto all'ultimo")
        numeroProcesso = lunghezzaProcesso - 1
        modificaExcel("A2", str(numeroProcesso))
        return numeroProcesso

    # Decrementa con wrap-around
    if numeroProcesso > 0:
        numeroProcesso -= 1
        modificaExcel("A2", str(numeroProcesso))
        print(f"modificaMacro.py/ ✅ Processo diminuito: {numeroProcesso}")
    else:
        numeroProcesso = lunghezzaProcesso - 1
        modificaExcel("A2", str(numeroProcesso))
        print(f"modificaMacro.py/ ✅ Processo riportato all'ultimo: {numeroProcesso}")
    
    return numeroProcesso


if __name__ == "__main__":
    print("modificaMacro.py/ === Test modificaMacro ===")
    risultato = modificaMacro()
    print(f"modificaMacro.py/ Risultato: {risultato}\n")
    
    print("modificaMacro.py/ === Test menoUnoMacro ===")
    risultato = menoUnoMacro()
    print(f"modificaMacro.py/ Risultato: {risultato}")