from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date

from funcoes import calcular_horas, ler_credenciais, trocar_senha

url = 'https://seniorx.myatos.net:8181/gestaoponto-frontend/login'
try:
    usuario, senha = ler_credenciais()
except:
    trocar_senha()
    usuario, senha = ler_credenciais()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#Efetuar login
login = driver.find_element(By.ID, 'index-vm-username')
login.send_keys(usuario)
password = driver.find_element(By.ID, 'index-vm-password')
password.send_keys(senha)
try:
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, 'index-vm-password'))
    )
except:
    print('Não funcionou')
    driver.quit()
driver.find_element(By.ID, 'index-1500385519648').click()

#Apontar horas
#linha_hoje = driver.find_element(By.ID, 'linha-0')
hoje = date.today()
hora_inicio, hora_fim = calcular_horas()
try:
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, f'dia_{hoje}_InserirMarcacao'))
    )
except:
    print('Não funcionou')
    driver.quit()
driver.find_element(By.ID, f'dia_{hoje}_InserirMarcacao').click()
driver.find_element(By.ID, 'addMarcacao').click()
marcacao0 = driver.find_element(By.ID, 'marcacaoTime-0')
marcacao0.send_keys(hora_inicio)
driver.find_element(By.ID, 'selectJustificative-0').click()
try:
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, 'ui-select-choices-row-1-3'))
    )
except:
    print('Não funcionou')
    driver.quit()
driver.find_element(By.ID, 'ui-select-choices-row-1-3').click()
driver.find_element(By.ID, 'addMarcacao').click()
marcacao1 = driver.find_element(By.ID, 'marcacaoTime-1')
marcacao1.send_keys(hora_fim)
driver.find_element(By.ID, 'selectJustificative-1').click()
try:
    element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, 'ui-select-choices-row-3-3'))
    )
except:
    print('Não funcionou')
    driver.quit()
driver.find_element(By.ID, 'ui-select-choices-row-3-3').click()
driver.find_element(By.ID, 'saveAppointment').click()

time.sleep(100)
