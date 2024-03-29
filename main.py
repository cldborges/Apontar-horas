# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from funcoes import *

lista_negra = ler_lista_negra()
url = 'https://seniorx.myatos.net:8181/gestaoponto-frontend/login'
try:
    usuario, senha = ler_credenciais()
except:
    trocar_senha()
    usuario, senha = ler_credenciais()

driver = webdriver.Chrome()
driver.get(url)

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
time.sleep(0.5)
driver.find_element(By.ID, 'index-1500385519648').click()

#linha_hoje = driver.find_element(By.ID, 'linha-0')
dia = date.today()
# dia = '2023-01-27'
print(dia)

# time.sleep(5)
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, f'dia_{dia}_data'))
    )
    print('passou')
except:
    print('Não funcionou')
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
    
# print (situacoes.get_attribute('id'))

# print(len(linhas_tabela_dias))
# print(dias_apontar)

#dia-2023-01-27-situacao-0
#tbody
# //*[@id="dia-2023-01-27-situacao-0"]
#dia_2023-01-27_situacao_0 > a
# /html/body/div[2]/div[3]/div[2]/div/ui-view/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/ul/li/a/span
# /html/body/div[2]/div[3]/div[2]/div/ui-view/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/ul/li/a/span
# /html/body/div[2]/div[3]/div[2]/div/ui-view/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/span/a
#coluna-situacoes-1
#index-1500385520299 > div.right-column > div > div:nth-child(3) > dl > dd > span


# apontar_horas(driver, dia)

time.sleep(600)
