from openpyxl import Workbook, load_workbook
import os

file_path = "file/macro.xlsx"

def scritturaExcel(wb, ws):

    ws["A1"] = "Numero processo"
    ws["C1"] = "Processi"


    prodotti = [
        "Carta A4 per stampanti (80 g/m²)",
        "Carta igienica (3 veli, 50 m)",
        "Rotoli jumbo e mini-jumbo",
        "Asciugamani monouso in rotolo o piegati",
        "Fazzoletti per il naso",
        "Rotoli industriali grandi",
        "Quaderni, block-notes, agende",
        "Carta da cucina riutilizzabile",
        "Panni per la pulizia in bambù",
        "Tovaglioli, tovagliette e scatole in carta di bambù",
        "Etichette compostabili e buste per spedizioni"
    ]

    # Inserisce tutti i prodotti in modo dinamico
    for i, prodotto in enumerate(prodotti, start=2):
        ws[f"C{i}"] = str(i - 1)
        ws[f"D{i}"] = prodotto


    wb.save(file_path)
    print("✅ Tutti i prodotti sono stati scritti correttamente in macro.xlsx")


if not os.path.exists(file_path):
    wb = Workbook()
    ws = wb.active
    wb.save(file_path)
else:
    wb = load_workbook(file_path)
    ws = wb.active

scritturaExcel(wb, ws)
