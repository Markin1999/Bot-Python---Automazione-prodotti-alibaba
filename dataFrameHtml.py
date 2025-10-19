import pandas as pd
from bs4 import BeautifulSoup

import os


import re

class Prodotto:
    def __init__(self, blocco):
        # --- TITolo ---
        self.titolo = self._get_text_by_selectors(
            blocco,
            [
                "h2.searchx-product-e-title span",
                "h2.searchx-product-e-title a span",
                "h2.searchx-product-e-title",
                "h2 .elements-title-normal__content",
                "h2 a span",
            ],
        )

        # --- PREZZO (range o singolo) ---
        self.prezzo = self._get_text_by_selectors(
            blocco,
            [
                ".searchx-product-e-price",                 # nuove card
                ".searchx-product-e-price__current",
                ".elements-offer-price-normal__price",      # vecchie card
                ".price", ".product-price", ".ma-price",
            ],
            fallback=lambda: self._regex_in_text(blocco, r"[\d\.,]+\s*(?:[-–]\s*[\d\.,]+)?\s*(?:€|USD)")
        )

        # --- ORDINE MINIMO ---
        self.ordineMinimo = self._get_text_by_selectors(
            blocco,
            [
                ".searchx-product-e-moQ",
                ".moq", ".min-order", ".minorder",
                ".elements-offer-price-normal__min-order",
            ],
            fallback=lambda: self._first_string_containing(blocco, "Ordine minimo")
        )

        # --- AZIENDA / VENDITORE ---
        self.azienda = self._get_text_by_selectors(
            blocco,
            [
                ".fy26-supplier-name",                      # nuove card
                ".searchx-company-name",
                ".seb-supplier-name__name",
                ".company-name", ".supplier-name",
                "a.company-name", "a.supplier-name",
            ],
            fallback=lambda: self._first_anchor_company_like(blocco)
        )

        # --- VALUTAZIONE (es. 4.8/5.0) ---
        self.valutazione = self._get_text_by_selectors(
            blocco,
            [
                ".searchx-product-e-rating-score",
                ".seb-star_rating__score",
                ".rating-score", ".review-value", ".star-rating",
            ],
            fallback=lambda: self._regex_in_text(blocco, r"\b(\d(?:\.\d)?)\s*/\s*5\.0\b", group=1)
        )

        # pulizia finale
        self.titolo        = self._clean(self.titolo, ban_symbols=True)
        self.prezzo        = self._clean(self.prezzo)
        self.ordineMinimo  = self._clean(self.ordineMinimo)
        self.azienda       = self._clean(self.azienda, prefer_company=True)
        self.valutazione   = self._clean(self.valutazione)

    # ---------- Helpers robusti ----------
    def _get_text_by_selectors(self, root, selectors, fallback=None):
        for sel in selectors:
            el = root.select_one(sel)
            if el:
                txt = el.get_text(strip=True)
                if txt:
                    return txt
        return fallback() if callable(fallback) else None

    def _regex_in_text(self, root, pattern, group=0):
        m = re.search(pattern, root.get_text(" ", strip=True))
        return m.group(group) if m else None

    def _first_string_containing(self, root, needle):
        s = root.find(string=lambda t: t and needle.lower() in t.lower())
        return s.strip() if s else None

    def _first_anchor_company_like(self, root):
        bad_kw = ["Reso Facile", "più popolari", "più venduti", "Chatta ora",
                  "Aggiungi e confronta", "Aggiungi al carrello"]
        for a in root.select("a"):
            txt = a.get_text(strip=True)
            if not txt: 
                continue
            if any(k.lower() in txt.lower() for k in bad_kw):
                continue
            if any(sym in txt for sym in ["€", "/", "(", ")", "#"]):
                continue
            if not any(ch.isalpha() for ch in txt):
                continue
            return txt
        return None

    def _clean(self, s, ban_symbols=False, prefer_company=False):
        if not s:
            return None
        s = " ".join(str(s).split())
        if s.lower() in {"none", "nan"}:
            return None
        if ban_symbols and any(x in s for x in ["€","#","(",")"]):
          
            return None
        if prefer_company:

            s = s.replace("  ", " ")
        return s

    def __repr__(self):
        return (f"Prodotto(titolo={self.titolo!r}, prezzo={self.prezzo!r}, "
                f"ordineMinimo={self.ordineMinimo!r}, azienda={self.azienda!r}, "
                f"valutazione={self.valutazione!r})")

import os
import pandas as pd

def dataFrameHtml(driver, numero_processo):

    file_name = f"pagina_{numero_processo}.html"
    percorso_completo = os.path.join("PagineHtml", file_name)

    html = driver.execute_script("return document.documentElement.outerHTML;")

    soupInput = BeautifulSoup(html, 'html.parser')

    wrappers = soupInput.select(".fy26-product-card-wrapper")
    if not wrappers:
        wrappers = soupInput.select(".searchx-offer-item, .list-card, .searchx-product-card")
    if not wrappers:
        wrappers = soupInput.find_all("div", attrs={"data-ctrdot": True})

    prodotti = []
    seen = set()
    for w in wrappers:
        p = Prodotto(w)
        if any([p.titolo, p.prezzo, p.azienda, p.ordineMinimo, p.valutazione]):
            key = ((p.titolo or "").strip(), (p.azienda or "").strip(), (p.prezzo or "").strip())
            if key in seen:
                continue
            seen.add(key)
            prodotti.append(p)


    colonne = ["titolo", "prezzo", "ordineMinimo", "azienda", "valutazione"]
    rows = [{col: getattr(p, col, None) for col in colonne} for p in prodotti]
    df = pd.DataFrame(rows, columns=colonne)


    os.makedirs("PagineHtml", exist_ok=True)
    df = df.fillna("").applymap(lambda x: " ".join(str(x).split()))
    output_path = os.path.join("PagineHtml", f"prodotti{numero_processo}.xlsx")
    df.to_excel(output_path, index=False, engine="openpyxl")

    print(f"✅ Prodotti unici: {len(df)}")
    print(f"✅ File Excel salvato in: {output_path}")
    return df


    if __name__ == "__main__":
        pass