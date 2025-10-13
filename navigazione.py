import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

# Opzioni Chrome (user-agent realistico)
options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

driver.get("https://www.alibaba.com")

# Nascondiamo l'automazione
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

time.sleep(2)

input("Premi INVIO per chiudere il browser...")
driver.quit()
