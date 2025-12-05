from navigazione import primoLancio
from prendiTutto import prendiTutto
from pulizia import pulisciStringa
from cercaTopAziende import TopAziende


def tuttoCompreso():
    print("🚀 Avvio primoLancio()...")
    completato = primoLancio()
    if not completato:
        print("❌ Primo lancio non completato, interrompo il flusso.")
        return
    print("✅ primoLancio completato!\n")

    print("🚀 Avvio prendiTutto()...")
    completato = prendiTutto()
    if not completato:
        print("❌ Errore in prendiTutto(), interrompo il flusso.")
        return
    print("✅ prendiTutto completato!\n")

    print("🚀 Avvio pulisciStringa()...")
    completato = pulisciStringa()
    if not completato:
        print("❌ Errore in pulisciStringa(), interrompo il flusso.")
        return
    print("✅ pulisciStringa completato!\n")

    print("🚀 Avvio TopAziende()...")
    completato = TopAziende()
    if not completato:
        print("❌ Errore in TopAziende(), interrompo il flusso.")
        return
    print("✅ Tutto il processo completato con successo! 🎉")


if __name__ == "__main__":
    tuttoCompreso()
