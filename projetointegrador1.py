#importa a biblioteca pandas para manipulação de dados
import pandas as pd

#le arquivo csv (exemplo da márcia)
df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver (1).csv')

#salva o dataframe como um arquivo excel / index = False evita que o índice seja salvo como uma coluna
df.to_excel('Projeto-Integrador.xlsx', index=False)

#printa df
print(df)