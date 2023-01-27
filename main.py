from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date

from funcoes import *

url = 'https://seniorx.myatos.net:8181/gestaoponto-frontend/login'
try:
    usuario, senha = ler_credenciais()
except:
    trocar_senha()
    usuario, senha = ler_credenciais()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#Efetuar login
try:
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, 'index-vm-password'))
    )
except:
    print('Não funcionou')
    driver.quit()
login = driver.find_element(By.ID, 'index-vm-username')
login.send_keys(usuario)
password = driver.find_element(By.ID, 'index-vm-password')
password.send_keys(senha)
time.sleep(0.5)
driver.find_element(By.ID, 'index-1500385519648').click()

#Apontar horas
#linha_hoje = driver.find_element(By.ID, 'linha-0')
hoje = date.today()
dia = '2023-01-23'
print(hoje)

apontar_horas(driver,dia)

time.sleep(60)
