from selenium import webdriver
import os

def copiaHtml(driver, NumeroProcesso):
    try:

        html = driver.execute_script("return document.documentElement.outerHTML;")
        estraiInputHtml(html,)

        file_name = f"pagina_{int(NumeroProcesso)}.html"
        percorso_completo = os.path.join("PagineHtml", file_name)

   
        with open(percorso_completo, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✅ Pagina HTML copiata correttamente in {file_name}")
    except Exception as e:
        print(f"⚠️ Errore durante la copia della pagina HTML: {e}")
