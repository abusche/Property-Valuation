from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import time
from bs4 import BeautifulSoup

def get_soup(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    driver.get(url)

    try:
        time.sleep(2)
        wait = WebDriverWait(driver, 5)
        
        buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-qa-id='criteria_more']")
        if not buttons:
            print("Bouton non trouvé, récupération du HTML actuel.")
        else:
            button = buttons[0]
            #print("Bouton trouvé...")

            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
            time.sleep(1)

            #print("Affichage du bouton...")
            driver.execute_script("arguments[0].style.display = 'block'; arguments[0].disabled = false;", button)
            time.sleep(1)

            try:
                button.click()
                #print("Clic réussi")
            except Exception:
                print("Clic échoué, tentative avec ActionChains...")

            time.sleep(2)
    except Exception as e:
        print(f"Erreur lors du clic sur le bouton: {e}")
    finally:
        html = driver.page_source
        driver.quit()
    
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_links(url):
    soup = get_soup(url)
    codes = soup.find_all('a', class_='absolute inset-none')
    links = []
    for code in codes:
        links.append(f"https://www.leboncoin.fr" + code.get('href'))
    
    return links
