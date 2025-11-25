from extraction import coletar_dados
from transformation import transformar_dados
from gold import gerar_gold
from load import carregar_dados
from colorama import Fore, Style, init

init(autoreset=True)

def pipeline_etl():
    print(Fore.CYAN + '\nETL iniciada...\n')

    estilo_de_vida_csv = 'estilo_de_vida.csv'
    bronze_path = 'estilo_de_vida_bronze.csv'
    silver_path = 'estilo_de_vida_silver.csv'
    gold_path = 'estilo_de_vida_gold.csv'

    df = coletar_dados(estilo_de_vida_csv, bronze_path)
    df_tratado = transformar_dados(bronze_path, silver_path)
    df_gold = gerar_gold(silver_path, gold_path)
    carregar_dados(df, df_tratado, df_gold)

if __name__ == "__main__":
    pipeline_etl()
