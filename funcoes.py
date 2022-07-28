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