import pandas as pd
from colorama import Fore, Style, init
import os

init(autoreset=True)

def coletar_dados(estilo_de_vida_csv, bronze_path='estilo_de_vida_bronze.csv'):
    print(Fore.CYAN + '\nEtapa 1: Extraindo dados...\n')
    df = pd.read_csv(estilo_de_vida_csv)

    print('Dados originais:')
    print(df, '\n')

    df.to_csv(bronze_path, index=False)
    print(Fore.CYAN + f'Etapa 1: Arquivo salvo em: {os.path.abspath(bronze_path)}\n')

    return df
