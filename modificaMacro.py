from letturaExcel import letturaExcel   
from modificaExcel import modificaExcel 

def modificaMacro():
    numeroProcesso = letturaExcel("NumeroProcesso")[0]
    numeroProcesso = int(numeroProcesso)
    lunghezzaProcesso = len(letturaExcel("Processi")) - 1   

    if numeroProcesso < lunghezzaProcesso:
            numeroProcesso += 1
            modificaExcel("A2", str(numeroProcesso))
            print(f"✅ Il processo è stato aumentato di 1 in macro.xlsx: {numeroProcesso}")
     
    else:
            numeroProcesso = 0
            modificaExcel("A2", str(numeroProcesso))
            print("✅ Il processo è stato resettato a 0 in macro.xlsx")