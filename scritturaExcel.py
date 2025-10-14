from openpyxl import load_workbook, Workbook
import os

file_path = "file/macro.xlsx"

def scritturaExcel(wb, ws):
    ws["A1"] = "Numero processo"
    ws["C1"] = "Processi"
    ws["C2"] = "1"
    ws["D2"] = "Primo podotto cercato e salvato"
    ws["C3"] = "2"
    ws["D3"] = "Secondo prodotto cercato e salvato"
    ws["C4"] = "3"
    ws["D4"] = "Terzo prodotto cercato e salvato"
    wb.save(file_path)
    print("✅ Dati scritti correttamente in macro.xlsx")


# 🔹 Controlla se il file esiste
response = os.path.exists(file_path)
print(response)

if not response:
    wb = Workbook()
    ws = wb.active
    wb.save(file_path)
else:
    wb = load_workbook(file_path)
    ws = wb.active


scritturaExcel(wb, ws)
