from bs4 import BeautifulSoup
import os

def estraiInputHtml():
    file_name = "pagina_2.html"
    percorso_completo = os.path.join("PagineHtml", file_name)

    with open(percorso_completo, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Prendi i tag e concatena, senza trasformarli in lista-stringa
    tags = soup.find_all(class_="fy26-product-card-wrapper")
    nuovo_html = "".join(str(tag) for tag in tags)

    # Scrive SOLO i blocchi richiesti
    with open(percorso_completo, "w", encoding="utf-8") as f:
        f.write(nuovo_html)

estraiInputHtml()
