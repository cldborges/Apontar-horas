from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from funcoes import *
import easygui

lista_negra = ler_lista_negra()
url = 'https://seniorx.myatos.net:8181/gestaoponto-frontend/login'
try:
    usuario, senha = ler_credenciais()
except:
    trocar_senha()
    usuario, senha = ler_credenciais()

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#Efetuar login
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'index-vm-password'))
    )
except:
    print('Não funcionou')
    driver.quit()
login = driver.find_element(By.ID, 'index-vm-username')
login.send_keys(usuario)
password = driver.find_element(By.ID, 'index-vm-password')
password.send_keys(senha)
time.sleep(1)
driver.find_element(By.ID, 'index-1500385519648').click()

#linha_hoje = driver.find_element(By.ID, 'linha-0')
dia = date.today()
# dia = '2023-01-27'
print(dia)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, f'dia_{dia}_data'))
    )
    print('passou')
except:
    print('Não funcionou')
    erro = driver.find_element(By.CSS_SELECTOR, '#index-1500385519855')
    easygui.msgbox(erro.text)
    driver.quit()

tabela_dias = driver.find_element(By.CSS_SELECTOR, '#tbody')
linhas_tabela_dias = tabela_dias.find_elements(By.CSS_SELECTOR, 'tr')
dias_apontar = []
for linha in linhas_tabela_dias:
    situacoes = linha.find_element(By.XPATH, 'td[4]')
    if '08:00 - 902 Débito Banco de Horas' in situacoes.text:
        dia_apontar = situacoes.find_element(By.CSS_SELECTOR, 'span').get_attribute('id')[4:14] # acha o atributo id do elemento e pega do 4o ao 14o caracter
        if dia_apontar not in lista_negra:
            dias_apontar.append(dia_apontar)
        # dia_apontar = dia_apontar
print(dias_apontar)

for dia in dias_apontar:
    apontar_horas(driver, dia)
    
time.sleep(600)
