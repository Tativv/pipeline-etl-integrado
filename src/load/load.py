from sqlalchemy import create_engine
from colorama import Fore, Style, init

init(autoreset=True)

def carregar_dados(df, df_tratado, df_gold):
    print(Fore.CYAN + '\nEtapa 3: Criação do Banco de Dados...\n')
    print( Fore.YELLOW + '\nCriando um banco SQLite (arquivo estilo_de_vida.db).........')

    # cria o banco
    engine = create_engine('sqlite:///estilo_de_vida.db')

    # salva todas as tabelas no banco criado
    df.to_sql('estilo_de_vida_bronze', con=engine, if_exists='replace', index=False)
    df_tratado.to_sql('estilo_de_vida_silver', con=engine, if_exists='replace', index=False)
    df_gold.to_sql('estilo_de_vida_gold', con=engine, if_exists='replace', index=False)
    print( Fore.YELLOW + '\nBanco de Dados criado.........')
