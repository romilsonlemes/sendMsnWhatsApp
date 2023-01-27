import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

linkWhatsApp = "https://web.whatapp.com"
navegador = webdriver.Chrome()
navegador.get(linkWhatsApp)

# Esperar a tela do WhatsApp Carregar
while len(navegador.find_elements(By.ID, 'side')) < 1: # -> Se a lista for vazia, significa que o  elemento  não existe ainda
    time.sleep(1)
time.sleep(2) # Só uma garantia de  espera

