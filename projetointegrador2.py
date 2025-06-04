import csv
import time
from time import sleep

import pyautogui
import pyperclip


with open("LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv", "r") as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    segunda_linha = next(reader)
    print(segunda_linha)

data = segunda_linha[0]
valor_esteira1 = segunda_linha[2]
valor_esteira2 = segunda_linha[3]
valor_esteira3 = segunda_linha[4]
print(valor_esteira3)

verde = '🟢'
vermelho = '🔴'
amarelo = '🟡'

if valor_esteira1 == 1:
    esteira1 = vermelho
elif valor_esteira1 == 2:
    esteira1 = amarelo
else:
    esteira1 = verde

if valor_esteira2 == 1:
    esteira2 = vermelho
elif valor_esteira2 == 2:
    esteira2 = amarelo
else:
    esteira2 = verde

if valor_esteira3 == 1:
    esteira3 = vermelho
elif valor_esteira3 == 2:
    esteira3 = amarelo
else:
    esteira3 = verde

mensagem = f'ESTOQUE NO DIA {data}\nEsteira 1: {esteira1}\nEsteira 2: {esteira2}\nEsteira 3: {esteira3}'

print(mensagem)

pyautogui.press('winleft')
time.sleep(2)

pyautogui.write('chrome')
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)

pyautogui.write('https://web.whatsapp.com/')
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)