from navigazione import primoLancio
from prendiTutto import prendiTutto
from pulizia import pulisciStringa
from cercaTopAziende import TopAziende
from pulisciCartelle import pulisciCartelle
from logger import log
import os
import sys
import traceback

def tuttoCompreso():

    log("tuttoCompreso.py/ 🚀 Avvio pulisciCartelle()...")
    try:
        pulisciCartelle()
    except Exception as e:
        log(f"❌ Errore in pulisciCartelle(): {e}")
        traceback.print_exc()
        exit(1)

        log("tuttoCompreso.py/ ❌ Errore in pulisciCartelle(), interrompo il flusso.")
    
    log("tuttoCompreso.py/ ✅ pulisciCartelle completato!\n")
    
    log("tuttoCompreso.py/ 🚀 Avvio primoLancio()...")
    completato = primoLancio()
    if not completato:
        log("tuttoCompreso.py/ ❌ Primo lancio non completato, interrompo il flusso.")
        return
    log("tuttoCompreso.py/ ✅ primoLancio completato!\n")
    
    
    log("tuttoCompreso.py/ 🚀 Avvio prendiTutto()...")
    completato = prendiTutto()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in prendiTutto(), interrompo il flusso.")
        return
    log("tuttoCompreso.py/ ✅ prendiTutto completato!\n")

    log("tuttoCompreso.py/ 🚀 Avvio pulisciStringa()...")
    completato = pulisciStringa()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in pulisciStringa(), interrompo il flusso.")
        return
    log("tuttoCompreso.py/ ✅ pulisciStringa completato!\n")

    log("tuttoCompreso.py/ 🚀 Avvio TopAziende()...")
    completato = TopAziende()
    if not completato:
        print("tuttoCompreso.py/ ❌ Errore in TopAziende(), interrompo il flusso.")
        return
    log("tuttoCompreso.py/ ✅ Tutto il processo completato con successo! 🎉")


if __name__ == "__main__":
    tuttoCompreso()
