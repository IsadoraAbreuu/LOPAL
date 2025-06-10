import csv
import time
from time import sleep

import pyautogui
import pyperclip

#le e printa a segunda linha do arquivo csv
with open("LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv", "r") as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    segunda_linha = next(reader)
    print(segunda_linha)

#guarda em variaveis os valores do arquivo csv de acordo com o índice
data = segunda_linha[0]
valor_esteira1 = int(segunda_linha[2])
valor_esteira2 = int(segunda_linha[3])
valor_esteira3 = int(segunda_linha[4])
print(valor_esteira2)

#define variaveis do estado das esteiras com emoji
verde = "🟢"
vermelho = "🔴"
amarelo = "🟡"

#condições de acordo com o estado da esteira1
if valor_esteira1 == 1 or valor_esteira1 == 0:
    esteira1 = vermelho
elif valor_esteira1 == 2:
    esteira1 = amarelo
else:
    esteira1 = verde

#condições de acordo com o estado da esteira2
if valor_esteira2 == 1 or valor_esteira2 == 0:
    esteira2 = vermelho
elif valor_esteira2 == 2:
    esteira2 = amarelo
else:
    esteira2 = verde

#condições de acordo com o estado da esteira3
if valor_esteira3 == 1 or valor_esteira3 == 0:
    esteira3 = vermelho
elif valor_esteira3 == 2:
    esteira3 = amarelo
else:
    esteira3 = verde

#mensagem que será enviada pelo WhatsApp
mensagem = f'ESTOQUE NO DIA {data} - Esteira 1: {esteira1} | Esteira 2: {esteira2} | Esteira 3: {esteira3}'

#dá 'ctrl c' na mensagem para copiar os emojis
pyperclip.copy(mensagem)

#início da automação
pyautogui.alert(' ⚠️ Não mexa em nada até o próximo aviso!!!')
pyautogui.press('winleft')
time.sleep(2)

pyautogui.write('chrome')
time.sleep(2)

pyautogui.press('enter')
time.sleep(3)

pyautogui.write('https://web.whatsapp.com/')
time.sleep(3)

pyautogui.press('enter')
time.sleep(10)

pyautogui.position(x=450, y=191)
time.sleep(1)

pyautogui.click(x=450, y=191)
time.sleep(3)

pyautogui.write('victor')
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

pyautogui.position(x=821, y=984)
time.sleep(1)

pyautogui.click(x=821, y=984)
time.sleep(3)

pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')
time.sleep(2)

pyautogui.alert('Seu código finalizou e as mensagens foram enviadas com sucesso! 😉 ')
