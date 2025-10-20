from openpyxl import Workbook, load_workbook
import os

file_path = "file/macro.xlsx"

def scritturaExcel(wb, ws):

    ws["A1"] = "NumeroProcesso"
    ws["B1"] = "Processi"
    ws["C1"] = "Ricerca"


    prodotti = [

        "Carta A4 per stampanti 80 g m² all'ingrosso | A4 copy paper supplier bulk office printing paper manufacturer",
        "Carta igienica 3 veli 50 m ecologica all'ingrosso | toilet paper 3 ply 50m eco-friendly bulk supplier manufacturer",
        "Rotoli jumbo e mini-jumbo carta tissue industriale all'ingrosso | jumbo mini jumbo tissue paper rolls manufacturer supplier",
        "Asciugamani monouso in rotolo o piegati per bagno e hotel | disposable hand towels roll folded paper towel bulk supplier",
        "Fazzoletti per il naso morbidi e confezionati all'ingrosso | soft facial tissues pocket pack manufacturer supplier",
        "Rotoli industriali grandi carta per pulizia officina | large industrial cleaning paper rolls bulk supplier manufacturer",
        "Quaderni, block-notes e agende personalizzabili all'ingrosso | notebooks journals planners custom logo wholesale manufacturer",
        "Carta da cucina riutilizzabile e assorbente ecologica | reusable kitchen paper towels eco-friendly cleaning rolls supplier",
        "Panni per la pulizia in bambù biodegradabili | bamboo cleaning cloths reusable eco-friendly wipes manufacturer supplier",
        "Tovaglioli, tovagliette e scatole in carta di bambù compostabili | bamboo napkins placemats packaging eco compostable supplier",
        "Etichette compostabili e buste per spedizioni ecologiche | compostable shipping labels and packaging mailers manufacturer"
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
