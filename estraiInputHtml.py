from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
import traceback

def estrai_input_html(driver, numero_processo,):

    try:


    
        html = driver.execute_script("return document.documentElement.outerHTML;")
        if not isinstance(html, str) or not html.strip():
            raise ValueError("HTML vuoto o non valido restituito dal driver Selenium.")

        soup = BeautifulSoup(html, 'html.parser')

        tags = soup.find_all(class_="fy26-product-card-wrapper")
        nuovo_html = "".join(str(tag) for tag in tags)


        with open(percorso_completo, "w", encoding="utf-8") as f:
            f.write(nuovo_html)

        return percorso_completo

    except Exception as e:

        time.sleep(30)

        error_msg = (
            f"ERRORE: il processo si è fermato al n. {numero_processo}. "
            f"Errore nella funzione '{funzione}': {e.__class__.__name__}: {e}"
        )

        raise RuntimeError(error_msg) from e


estraiInputHtml(stringa, NumeroProcesso)
