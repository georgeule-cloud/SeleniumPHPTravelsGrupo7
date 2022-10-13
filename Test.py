# Programa de Python
# Importamos  el web driver de selenium
from selenium import webdriver

driver = webdriver.Chrome()
# Le decimos al driver que abra la url de Google.
driver.get("https://phptravels.com/demo")