from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def ler_lista_negra():
    with open('lista_negra.txt', 'r', encoding='utf-8') as arquivo:
        lista_negra = arquivo.read().strip()
        lista_negra_datas = lista_negra.split(', ')
    return lista_negra_datas


def trocar_senha(usuario='', senha=''):
    if usuario =='':
        usuario = input('Qual o usuário?')
    if senha == '':
        senha = input('Qual a senha?')
    with open('conf.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'{usuario}\n{senha}')
    print('Usuário e senha atualizados!')


def ler_credenciais():
    with open('conf.txt', 'r', encoding='utf-8') as arquivo:
        usuario, senha = arquivo.readlines()
    return usuario, senha


def calcular_horas():
    from datetime import datetime, timedelta
    import random

    hora_inicial_minima = '07:55'
    hora_final_minima = '16:55'
    horas = []
    for hora in hora_inicial_minima, hora_final_minima:
        x = random.randint(0,10)
        hora1 = datetime.strptime(hora, '%H:%M')
        hora2 = hora1 + timedelta(minutes=x)
        Tempofinal_str = hora2.strftime('%H:%M')
        horas.append(Tempofinal_str)
    print(horas)
    return horas


def apontar_horas(driver, dia):
    hora_inicio, hora_fim = calcular_horas()
    try:
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, f'dia_{dia}_InserirMarcacao'))
        )
    except:
        print('Não funcionou')
        driver.quit()

    element = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, f'dia_{dia}_InserirMarcacao')))

    driver.find_element(By.ID, f'dia_{dia}_InserirMarcacao').click() #Inserir Marcação
    driver.find_element(By.ID, 'addMarcacao').click() #Adicionar
    time.sleep(3)
    marcacao0 = driver.find_element(By.ID, 'marcacaoTime-0')
    marcacao0.send_keys(hora_inicio)
    driver.find_element(By.ID, 'selectJustificative-0').click() #Justificativa
    try:
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, 'justificative_5'))) 
    except:
        print('Não funcionou')
        driver.quit()
    driver.find_element(By.ID, 'justificative_5').click()
    driver.find_element(By.ID, 'addMarcacao').click()
    marcacao1 = driver.find_element(By.ID, 'marcacaoTime-1')
    marcacao1.send_keys(hora_fim)
    driver.find_element(By.ID, 'selectJustificative-1').click()
    try:
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, 'justificative_5')))
    except:
        print('Não funcionou')
        driver.quit()
    driver.find_element(By.ID, 'justificative_5').click()
    driver.find_element(By.ID, 'saveAppointment').click()
    time.sleep(5)

