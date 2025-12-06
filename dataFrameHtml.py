import os
import re
import pandas as pd
from bs4 import BeautifulSoup


class Prodotto:
    def __init__(self, blocco):
        # --- TITOLO ---
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
            fallback=lambda: self._regex_in_text(
                blocco, r"[\d\.,]+\s*(?:[-–]\s*[\d\.,]+)?\s*(?:€|USD)"
            ),
        )

        # --- ORDINE MINIMO ---
        self.ordineMinimo = self._get_text_by_selectors(
            blocco,
            [
                ".searchx-product-e-moQ",
                ".moq", ".min-order", ".minorder",
                ".elements-offer-price-normal__min-order",
            ],
            fallback=lambda: self._first_string_containing(blocco, "Ordine minimo"),
        )

        # --- AZIENDA / VENDITORE ---
        self.azienda = self._extract_company(blocco)

        # --- VALUTAZIONE (es. 4.8/5.0) ---
        self.valutazione = self._get_text_by_selectors(
            blocco,
            [
                ".searchx-product-e-rating-score",
                ".seb-star_rating__score",
                ".rating-score", ".review-value", ".star-rating",
            ],
            fallback=lambda: self._regex_in_text(
                blocco, r"\b(\d(?:\.\d)?)\s*/\s*5\.0\b", group=1
            ),
        )

        # pulizia finale
        self.titolo        = self._clean(self.titolo, ban_symbols=True)
        self.prezzo        = self._clean(self.prezzo)
        self.ordineMinimo  = self._clean(self.ordineMinimo)
        self.azienda       = self._clean(self.azienda, prefer_company=True)
        self.valutazione   = self._clean(self.valutazione)

    # ---------- Estrazione azienda robusta ----------
    def _extract_company(self, root):
        # 1) Selettori più comuni (ATTENZIONE: virgole corrette)
        selectors = [
            ".searchx-product-e-company",
            ".searchx-company-name",
            ".seb-supplier-name__name",
            ".fy26-supplier-name",
            ".company-name",
            "a.company-name",
            ".supplier-name",
            "a.supplier-name",
            ".ma-supplier-name",
            "[data-role='supplier-name']",
        ]
        for sel in selectors:
            el = root.select_one(sel)
            if el:
                txt = el.get_text(strip=True)
                cleaned = self._clean_company(txt)
                if cleaned:
                    return cleaned

        # 2) Link con href tipico del profilo fornitore
        for a in root.select("a[href]"):
            href = a.get("href", "")
            if any(k in href for k in ["/company_profile/", "/supplier", "/store/"]):
                txt = a.get_text(strip=True)
                cleaned = self._clean_company(txt)
                if cleaned:
                    return cleaned

        # 3) Microdata / itemprop
        el = root.select_one('[itemprop="name"]')
        if el:
            txt = el.get_text(strip=True) or el.get("content", "")
            cleaned = self._clean_company(txt)
            if cleaned:
                return cleaned

        # 4) Vicinanza al titolo (fratelli/padre)
        title_node = root.select_one("h2, h1")
        if title_node:
            candidates = []
            parent = title_node.parent
            scopes = [title_node, parent, parent.parent if parent else None]
            for scope in scopes:
                if not scope:
                    continue
                for a in scope.select("a, .seller, .vendor, .shop-name"):
                    txt = a.get_text(strip=True)
                    cleaned = self._clean_company(txt)
                    if cleaned:
                        candidates.append(cleaned)
            if candidates:
                return self._pick_most_company_like(candidates)

        # 5) Fallback: prima ancora "company-like" nell'intera card
        for a in root.select("a, .seller, .vendor, .shop-name"):
            txt = a.get_text(strip=True)
            cleaned = self._clean_company(txt)
            if cleaned:
                return cleaned

        return None

    def _clean_company(self, s: str):
        if not s:
            return None
        s = " ".join(s.split())
        bad_kw = [
            "Reso Facile", "più popolari", "più venduti", "Chatta ora",
            "Aggiungi e confronta", "Aggiungi al carrello",
            "Contact", "Compare", "Chat now", "Add to cart",
            "Ship", "MOQ", "Min Order", "Price", "€", "$", "USD",
        ]
        if any(k.lower() in s.lower() for k in bad_kw):
            return None
        if not any(ch.isalpha() for ch in s):
            return None
        if len(s.split()) > 10:
            return None
        return s

    def _pick_most_company_like(self, candidates):
        company_kw = re.compile(
            r"\b(co(\.|,)?\s*ltd\.?|limited|ltd|inc\.?|corp\.?|srl|s\.r\.l\.|spa|s\.p\.a\.|gmbh|bv|s\.a\.|sas|oy|ab|s\.r\.o\.|ug|kft|llc)\b",
            re.I,
        )
        with_kw = [c for c in candidates if company_kw.search(c)]
        if with_kw:
            return min(with_kw, key=len)
        return min(candidates, key=len)

    # ---------- Helpers generici ----------
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
        if ban_symbols and any(x in s for x in ["€", "#", "(", ")"]):
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
import traceback
from bs4 import BeautifulSoup

def dataFrameHtml(driver, nomeRicerca, numero_processo):
    try:
        file_name = f"{nomeRicerca}{numero_processo}.html"
        percorso_completo = os.path.join("PagineHtml", file_name)

        html = driver.execute_script("return document.documentElement.outerHTML;")

        # ⛔️ Se HTML è vuoto o quasi, blocco subito
        if not html or not str(html).strip():
            raise RuntimeError("HTML vuoto: impossibile procedere con il parsing.")

        soupInput = BeautifulSoup(html, "html.parser")

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
                key = (
                    (p.titolo or "").strip(),
                    (p.azienda or "").strip(),
                    (p.prezzo or "").strip(),
                )
                if key in seen:
                    continue
                seen.add(key)
                prodotti.append(p)

        colonne = ["titolo", "prezzo", "ordineMinimo", "azienda", "valutazione"]
        rows = [{col: getattr(p, col, None) for col in colonne} for p in prodotti]
        df = pd.DataFrame(rows, columns=colonne)

        os.makedirs("PagineHtml", exist_ok=True)
        df = df.fillna("").applymap(lambda x: " ".join(str(x).split()))
        output_path = os.path.join("PagineHtml", f"{(numero_processo)}-{nomeRicerca}.xlsx")
        df.to_excel(output_path, index=False, engine="openpyxl")

        print(f"dataFrameHtml.py/ ✅ Prodotti unici: {len(df)}")
        print(f"dataFrameHtml.py ✅ File Excel salvato in: {output_path}")
        return df

    except Exception as e:
        print(f"dataFrame.py/ ⚠️ Errore in dataFrameHtml: {e}")
        traceback.print_exc()
        # Rilancio l'errore per bloccare l'esecuzione a monte
        raise

if __name__ == "__main__":
    pass
