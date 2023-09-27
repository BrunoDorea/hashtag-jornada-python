# Passo a passo do projeto
# Passo 1: Entrar no site da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login no sistema
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos
import pyautogui
import time
import pandas as pd
import numpy
import openpyxl

# Importar a base de dados de produtos
tabela = pd.read_csv('./aula_01-power_up/produtos.csv')

# time.sleep(500)

pyautogui.PAUSE = 0.3

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(5)

# Fazer login
pyautogui.click(x=575, y=370)
pyautogui.write('bruno@hashtagtreinamentos.com')
pyautogui.press('tab')
pyautogui.write('hashtag')
pyautogui.press('enter')

time.sleep(5)

for linha in tabela.index:
    
    pyautogui.click(x=570, y=245)
    # Cadastrar produto
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Enviar 
    pyautogui.press('enter')

    pyautogui.scroll(600)
    pyautogui.click()