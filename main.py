from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = 'https://seniorx.myatos.net:8181/gestaoponto-frontend/login'
with open('conf.txt', 'r', encoding='utf-8') as arquivo:
    usuario, senha = arquivo.readlines()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
login = driver.find_element(By.ID, 'index-vm-username')
login.send_keys(usuario)
password = driver.find_element(By.ID, 'index-vm-password')
password.send_keys(senha)
driver.find_element(By.ID, 'index-1500385519648').click()

time.sleep(5)

#linha_hoje = driver.find_element(By.ID, 'linha-0')
driver.find_element(By.ID, 'dia_2022-07-26_InserirMarcacao').click()
driver.find_element(By.ID, 'addMarcacao').click()
marcacao0 = driver.find_element(By.ID, 'marcacaoTime-0')
marcacao0.send_keys('08:01')
driver.find_element(By.ID, 'selectJustificative-0').click()
time.sleep(10)
driver.find_element(By.ID, 'ui-select-choices-row-1-3').click()
driver.find_element(By.ID, 'addMarcacao').click()
marcacao1 = driver.find_element(By.ID, 'marcacaoTime-1')
marcacao1.send_keys('17:01')
driver.find_element(By.ID, 'selectJustificative-1').click()
time.sleep(10)
driver.find_element(By.ID, 'ui-select-choices-row-3-3').click()

time.sleep(100)
#ui-select-choices-row-1-3
#ui-select-choices-row-3-3