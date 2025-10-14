import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import pandas as pd
from letturaExcel import letturaExcel   

def primoLancio():


    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.alibaba.com")


    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    time.sleep(3)

    search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search Alibaba"]')

    search_box.clear()
    search_box.send_keys(letturaExcel("Ricerca")[0])
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)
    input("Premi INVIO per chiudere il browser...")
    driver.quit()


primoLancio()