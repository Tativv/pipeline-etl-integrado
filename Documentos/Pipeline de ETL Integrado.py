import pandas as pd
import sqlite3
from colorama import Fore, Style, init
import os
import numpy as np
import re
from sqlalchemy import create_engine

init(autoreset=True)

# ==============================
# EXTRAÇÃO DE DADOS
# ==============================

def coletar_dados(estilo_de_vida_csv, bronze_path = 'estilo_de_vida_bronze.csv' ):
    print(Fore.CYAN + '\nEtapa 1: Extraindo dados...\n')
    df = pd.read_csv(estilo_de_vida_csv)
    print('Dados originais:')
    print(df, '\n')
    # salvando bronze
    df.to_csv(bronze_path, index = False)
    print(Fore.CYAN + f'Etapa 1: Arquivo salvo em: {os.path.abspath(bronze_path)}\n')
    return df
 

# ==============================
# TRANFORMAÇÃO DOS DADOS
# ==============================

def transformar_dados(bronze_path, silver_path: 'estilo_de_vida_silver.csv'):
    # Escolhendo as colunas a serem trabalhadas
    print(Fore.CYAN + '\nEtapa 2: Transformando dados...\n')
    print(Fore.CYAN + '\nEscolhendo as colunas a serem trabalhadas...\n')
    df_tratado = pd.read_csv(bronze_path)
    df_tratado = df_tratado[['Gender', 'Age', 'Weight (kg)', 'Fat_Percentage', 'BMI', 'diet_type', 'Workout_Type', 
                             'Workout_Frequency (days/week)', 'Experience_Level']]
 
    # Renomeando as colunas
    print(Fore.CYAN + '\nRenomeando as colunas...\n')
    df_tratado = df_tratado.rename(columns={
    "Gender" : "genero",
    "Age" : "idade",
    "Weight (kg)" : "peso",
    "Fat_Percentage" : "percentual_de_gordura",
    "BMI" : "imc",
    "diet_type" : "tipo_de_dieta",
     "Workout_Type" : "tipo_de_treino",
     "Workout_Frequency (days/week)" : "frequencia_de_treino_semanal",
    "Experience_Level" : "nivel_de_experiencia"
    })
    print(df_tratado.head())

    # Criando listas
    print(Fore.CYAN + '\nCriando listas...\n')
    df_tratado["genero"].unique().tolist()
    df_tratado["tipo_de_dieta"].unique().tolist()
    df_tratado["tipo_de_treino"].unique().tolist()
    df_tratado["nivel_de_experiencia"].unique().tolist()

    # Traduzindo 
    print(Fore.CYAN + '\nTraduzindo para português...\n')
    df_tratado["genero"] = df_tratado["genero"].map({
    "Male": "Masculino",
    "Female": "Feminino"
    })
    df_tratado["tipo_de_dieta"] = df_tratado["tipo_de_dieta"].map({
    "Vegan": "Vegana",
    "Vegetarian": "Vegetariana",
    "Paleo": "Paleolítica",
    "Keto": "Cetogênica",
    "Low-Carb": "Baixo Carboidrato",
    "Balanced": "Balanceada"
    })
    df_tratado["tipo_de_treino"] = df_tratado["tipo_de_treino"].map({
    "Strength": "Força",
    "HIIT": "HIIT",
    "Cardio": "Cardio",
    "Yoga": "Yoga"
    })

    # Arredondamento para 1 Casa Decimal
    print(Fore.CYAN + '\nArredondando número para uma casa decimal...\n')
    df_tratado["percentual_de_gordura"] = df_tratado["percentual_de_gordura"].round(1)
    df_tratado["peso"] = df_tratado["peso"].round(1)

    # Transformando colunas para int
    print(Fore.CYAN + '\nTransformando colunas para int...\n')
    colunas = ['frequencia_de_treino_semanal', 'idade', 'nivel_de_experiencia']
    df_tratado[colunas] = df_tratado[colunas].astype(int)

    # Substituição dos Códigos de Experiência por Categorias
    print(Fore.CYAN + '\nSubstituindo códigos de experiência por categorias...\n')
    df_tratado["nivel_de_experiencia"] = df_tratado["nivel_de_experiencia"].map({
        1: "Iniciante",
        2: "Intermediário",
        3: "Avançado"
    })
    print(df_tratado.head())
    # salvando a camada Silver
    df_tratado.to_csv(silver_path, index = False)
    print(Fore.CYAN + f'Etapa 2: Arquivo salvo em: {os.path.abspath(silver_path)}\n')


# ==============================
# ETAPA GOLD
# ==============================

    print(Fore.CYAN + f'Etapa Gold inciada\n')
    print(Fore.CYAN + f'Criando a função de classificação do índice de massa corporal\n')
    return df_tratado
   
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
    df_gold.to_csv(gold_path, index=False)
    print(Fore.CYAN + f'Etapa Gold concluída e salva em: {os.path.abspath(gold_path)}\n')
    print(df_gold.head())
    return df_gold


# ==============================
# CRIAÇÃO DO BANCO DE DADOS
# ==============================
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



def pipeline_etl():
    print(Fore.CYAN + '\nETL iniciada...\n')
    estilo_de_vida_csv= 'estilo_de_vida.csv'
    bronze_path = 'estilo_de_vida_bronze.csv'
    silver_path = 'estilo_de_vida_silver.csv'
    gold_path = 'estilo_de_vida_gold.csv'

    # 1) Extração
    df = coletar_dados(estilo_de_vida_csv, bronze_path)
    # 2) Transformação (gera silver)
    df_tratado = transformar_dados(bronze_path, silver_path)
     # 3) GOLD
    df_gold = gerar_gold(silver_path, gold_path)
    # 4) Carregamento
    carregar_dados(df, df_tratado, df_gold)
    
pipeline_etl()   
