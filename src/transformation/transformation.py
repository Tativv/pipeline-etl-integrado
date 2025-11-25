import pandas as pd
from colorama import Fore, Style, init
import os

init(autoreset=True)

def transformar_dados(bronze_path, silver_path = 'estilo_de_vida_silver.csv'):
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

    print(Fore.CYAN + f'Etapa Gold inciada\n')
    print(Fore.CYAN + f'Criando a função de classificação do índice de massa corporal\n')

    return df_tratado
