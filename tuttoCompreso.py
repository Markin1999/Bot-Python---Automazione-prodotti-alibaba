from navigazione import primoLancio
from prendiTutto import prendiTutto
from pulizia import pulisciStringa
from cercaTopAziende import TopAziende

import os
import sys


def tuttoCompreso():
    
    print("tuttoCompreso.py/ 🚀 Avvio primoLancio()...")
    completato = primoLancio()
    if not completato:
        print("tuttoCompreso.py/ ❌ Primo lancio non completato, interrompo il flusso.")
        return
    print("tuttoCompreso.py/ ✅ primoLancio completato!\n")
    
    
    print("tuttoCompreso.py/ 🚀 Avvio prendiTutto()...")
    completato = prendiTutto()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in prendiTutto(), interrompo il flusso.")
        return
    print("tuttoCompreso.py/ ✅ prendiTutto completato!\n")

    print("tuttoCompreso.py/ 🚀 Avvio pulisciStringa()...")
    completato = pulisciStringa()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in pulisciStringa(), interrompo il flusso.")
        return
    print("tuttoCompreso.py/ ✅ pulisciStringa completato!\n")

    print("tuttoCompreso.py/ 🚀 Avvio TopAziende()...")
    completato = TopAziende()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in TopAziende(), interrompo il flusso.")
        return
    print("tuttoCompreso.py/ ✅ Tutto il processo completato con successo! 🎉")


if __name__ == "__main__":
    tuttoCompreso()
