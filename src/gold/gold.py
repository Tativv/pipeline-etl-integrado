import pandas as pd
from colorama import Fore, Style, init
import os

init(autoreset=True)

# Função de Classificação do Índice de Massa Corporal
def classificar_imc(imc):    
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso Normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"
    
def gerar_gold(silver_path='estilo_de_vida_silver.csv', gold_path='estilo_de_vida_gold.csv'):
    # Lendo o arquivo silver
    df_gold = pd.read_csv(silver_path)

    # Aplica o classificador de forma segura
    df_gold["classificacao_imc"] = df_gold["imc"].apply(classificar_imc)

    # mover para a 6ª posição (índice 5)
    colunas = list(df_gold.columns)
    colunas.insert(5, colunas.pop(colunas.index("classificacao_imc")))
    df_gold = df_gold[colunas]

    # Salva GOLD
    df_gold.to_csv(gold_path, index=False, sep=";", decimal=",")
    print(Fore.CYAN + f'Etapa Gold concluída e salva em: {os.path.abspath(gold_path)}\n')
    print(df_gold.head())
    return df_gold
