import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException,
    StaleElementReferenceException, NoSuchElementException
)
from logger import log

def cambiaPagina(driver, XPATH, timeout=15, tries=3):
    last_err = None
    for attempt in range(1, tries + 1):
        try:
            wait = WebDriverWait(driver, timeout)

            # 1) presente a DOM
            btn = wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))

            # 2) visibile e cliccabile
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
            wait.until(EC.element_to_be_clickable((By.XPATH, XPATH)))

            # 3) click (normale -> fallback JS)
            try:
                btn.click()
            except Exception:
                driver.execute_script("arguments[0].click();", btn)

            # 4) attendi cambio contenuto (o navigazione)
            try:
                wait.until(EC.staleness_of(btn))  # la pagina/DOM è cambiata
            except TimeoutException:
                # In app SPA potrebbe non diventare 'stale': piccola attesa di sicurezza
                time.sleep(2)

            log("cambiaPagina.py/ ➡️ Pagina cambiata con successo.")
            return True

        except (TimeoutException, ElementClickInterceptedException,
                StaleElementReferenceException, NoSuchElementException) as e:
            last_err = e
            # micro scroll/pausa e riprova
            driver.execute_script("window.scrollBy(0, -120);")
            time.sleep(1)

    log(f"cambiaPagina.py/ ⚠️ Errore nel cambiare pagina dopo {tries} tentativi: {last_err}")
    return False
