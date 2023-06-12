import pandas as pd
import random

dados = pd.read_csv('postes.csv')  # Ler os dados

def calcular_consumo_medido(row):
    if random.random() < 0.995:
        variacao = row['consumo_esperado'] * random.uniform(-0.05, 0.05)
    else:
        variacao = row['consumo_esperado'] * random.uniform(-1.0, 1.0)
    return row['consumo_esperado'] + variacao

dados['consumo_medido'] = dados.apply(calcular_consumo_medido, axis=1)  # Acrescentar essas informações em uma coluna

dados['variacao_percentual'] = (dados['consumo_medido'] - dados['consumo_esperado']) / dados[
    'consumo_esperado'] * 100  # Transformar dados em percentual

dados_fora_do_intervalo = dados[(dados['variacao_percentual'] < -10) | (dados['variacao_percentual'] > 10)]
dados_fora_do_intervalo['alerta'] = ''

for index, row in dados_fora_do_intervalo.iterrows():
    if -100 <= row['variacao_percentual'] <= -50:
        dados_fora_do_intervalo.at[index, 'alerta'] = 'Alerta de lâmpada com defeito'

    elif row['variacao_percentual'] > 50:
        dados_fora_do_intervalo.at[index, 'alerta'] = 'Alerta de possível roubo de energia'
        
    else:
        dados_fora_do_intervalo.at[index, 'alerta'] = 'Alerta'

dados_fora_do_intervalo.to_csv('postes_fora_do_intervalo.csv', index=False)