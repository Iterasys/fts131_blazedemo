import time
from selenium import webdriver      # Referencia ao Selenium WebDriver
import pytest                       # Referencia ao Framework de Testes Unitário


def testar_blazedemo():
    # Definindo que controlará o Chrome e apontando onde está o ChromeDriver
    driver = webdriver.Chrome(executable_path='../drivers/chrome/96/chromedriver.exe')

    driver.get("https://www.blazedemo.com")
    time.sleep(30) # pausa de 30 segundos - precisa remover depois - "Alfinete"
    driver.get_screenshot_as_file('../prints/home.png')
    time.sleep(3)  # pausa de 3 segundos - precisa remover depois - "Alfinete"
    # oi