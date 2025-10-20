from letturaExcel import letturaExcel   
from modificaExcel import modificaExcel 

def modificaMacro():
    numeroProcesso = letturaExcel("NumeroProcesso")[0]
    try:
        numeroProcesso = int(numeroProcesso)
    except (TypeError, ValueError):
        numeroProcesso = 0

    processi = letturaExcel("Processi")          # può essere list o pandas.Series
    if processi is None:
        lunghezzaProcesso = 0
    else:
        try:
            lunghezzaProcesso = len(processi)
        except TypeError:
            lunghezzaProcesso = 0

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "0")
        print("ℹ️ Nessun processo: valore impostato a 0 in macro.xlsx")
        return

    if numeroProcesso < lunghezzaProcesso - 1:
        numeroProcesso += 1
        modificaExcel("A2", str(numeroProcesso))
        print(f"✅ Il processo è stato aumentato di 1 in macro.xlsx: {numeroProcesso}")
    else:
        numeroProcesso = 0
        modificaExcel("A2", str(numeroProcesso))
        print("✅ Il processo è stato resettato a 0 in macro.xlsx")

def menoUnoMacro():
    numeroProcesso = letturaExcel("NumeroProcesso")[0]
    try:
        numeroProcesso = int(numeroProcesso)
    except (TypeError, ValueError):
        numeroProcesso = 0

    processi = letturaExcel("Processi")          # evita 'or []' e 'if processi'
    if processi is None:
        lunghezzaProcesso = 0
    else:
        try:
            lunghezzaProcesso = len(processi)
        except TypeError:
            lunghezzaProcesso = 0

    if lunghezzaProcesso == 0:
        modificaExcel("A2", "0")
        print("ℹ️ Nessun processo: valore impostato a 0 in macro.xlsx")
        return

    if numeroProcesso > 0:
        numeroProcesso -= 1
        modificaExcel("A2", str(numeroProcesso))
        print(f"✅ Il processo è stato diminuito di 1 in macro.xlsx: {numeroProcesso}")
    else:
        # wrap all’ultimo indice valido
        numeroProcesso = lunghezzaProcesso - 1
        modificaExcel("A2", str(numeroProcesso))
        print("✅ Il processo è riportato all'ultimo valore in macro.xlsx")
