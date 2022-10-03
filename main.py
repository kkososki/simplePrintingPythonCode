import pyautogui as pyag
import time
import pandas as pd
import numpy as np
import clipboard

pyag.alert("Before pressing ok to start the code, open the pdf file")
pyag.PAUSE = 2.5

df = pd.read_csv('dados.csv', sep=';')
nome = np.array(df.filter(items=['NOME']))
curso = np.array(df.filter(items=['CURSO']))
dup = np.array(df.duplicated())

for i in range(0, len(nome)):
    time.sleep(2)
    if dup[i]:
        pyag.press('pagedown')
        continue
    titulo = str(curso[i] + ' - ' + nome[i])
    titulo = titulo[2:-2]
    clipboard.copy(str(titulo))
    pyag.hotkey('ctrl', 'p') #imprimir certificado
    time.sleep(1)
    pyag.hotkey('alt', 'l') #imprimir página atual
    pyag.press('enter')
    pyag.hotkey('ctrl', 'v') #colar em salvar
    time.sleep(1)
    pyag.press('enter') #salvar
    time.sleep(3)
    pyag.hotkey('ctrl', 'f4') #fechar aba de novo certificado e voltar para arquivo original
    pyag.press('pagedown') #ir para próximo certificado
    

pyag.alert("The code ended")