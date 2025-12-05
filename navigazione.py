import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from letturaExcel import letturaExcel
from modificaMacro import modificaMacro 
from modificaMacro import menoUnoMacro
from dataFrameHtml import dataFrameHtml
from cambiaPagina import cambiaPagina
from NuovaLetturaExcel import nuovaLetturaExcel
import re

def _norm_num(x):
    s = str(x).strip()
    s = re.sub(r'\.0+$', '', s)
    return s




# Migliorie da apportare: A ogni ricerca se il file si interrompe non fare modificaMacro() per sicurezza    
def primoLancio():
    try:
        ciclo_completato = False  

        lunghezzaRicerca = len(nuovaLetturaExcel("Ricerca"))
        print(f"navigazione.py/ ℹ️ Lunghezza della lista 'Ricerca': {lunghezzaRicerca}")


        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        )

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.alibaba.com")

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        time.sleep(3)
      
        for t in range(lunghezzaRicerca):
            print(f"navigazione.py/ 🔎 Avvio ricerca {t} / {lunghezzaRicerca}...")

            
            macroAttuale = int(letturaExcel("NumeroProcesso")[0])

            try:
                time.sleep(3)
                

                search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search Alibaba"]')
                time.sleep(2)
                search_box.send_keys(Keys.COMMAND + "a")  
                search_box.send_keys(Keys.BACKSPACE)      
                time.sleep(3)
                modificaMacro()  
                time.sleep(3) 
                search_box.send_keys(letturaExcel("Ricerca")[macroAttuale])
                time.sleep(1)
                search_box.send_keys(Keys.RETURN)

                time.sleep(5)
                ricerca = letturaExcel("Nome")[macroAttuale]
                numero_processo = _norm_num(letturaExcel("NumeroProcesso")[0])

          
                dataFrameHtml(driver, ricerca, numero_processo)
                time.sleep(5)
        
                cambiaPagina(driver, '//*[@id="sse-fluent-offerlist-ssr"]/div[3]/div/div/a[2]/span')
                time.sleep(5)
                dataFrameHtml(driver, ricerca, f"{numero_processo}-01")
                time.sleep(5)
                cambiaPagina(driver, '//*[@id="sse-fluent-offerlist-ssr"]/div[3]/div/div/a[3]/span')
                time.sleep(5)
                dataFrameHtml(driver, ricerca, f"{numero_processo}-02")

                print(f"✅ Ricerca {t+1}/{lunghezzaRicerca} completata")
                ciclo_completato = True  

            except Exception as e:
                print(f"navigazione.py/ ⚠️ Errore durante la ricerca {t+1}: {e}")
                ciclo_completato = False
                break  

        
        if ciclo_completato:
            modificaMacro()
            print("navigazione.py/ 🟢 Tutte le ricerche completate con successo!")
        else:
           
            print("navigazione.py/ 🔴 Ciclo interrotto: ultima modificaMacro() saltata per sicurezza.")

    except IndexError:
        print("navigazione.py/ ❌ Errore: indice fuori dai limiti della lista 'Ricerca' o 'NumeroProcesso'.")
    except FileNotFoundError:
        print("navigazione.py/ ❌ Errore: file Excel non trovato. Controlla il percorso.")
    except Exception as e:
        print(f"navigazione.py/ ⚠️ Errore imprevisto: {e}")
    finally:
        try:
            
            driver.quit()
            menoUnoMacro()
        except:
            pass
    return True

if __name__ == "__main__":
    primoLancio()

