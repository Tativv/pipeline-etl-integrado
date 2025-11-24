# Pipeline de ETL Integrado – Análise de Fatores de Sucesso para Redução de Gordura Corporal

Este projeto desenvolve um **pipeline ETL completo** utilizando **Python**, **banco de dados relacional** (SQLite) e **Power BI**, com o objetivo de identificar quais fatores de estilo de vida contribuem para a redução do percentual de gordura corporal.

---

## 🎯 Objetivo do Projeto

Uma consultoria fitness deseja compreender quais combinações entre **dieta**, **treino** e **hábitos** têm maior impacto na redução de gordura corporal. A partir de uma base de dados de estilo de vida contendo informações como tipo de dieta, tipo de treino, frequência de exercícios, IMC e percentual de gordura, foi construído um fluxo completo para análise e tomada de decisão.

---

## ❓ Perguntas de Negócio Respondidas

- Qual tipo de dieta apresenta menor média de percentual de gordura?  
- Qual tipo de treino está associado a níveis menores de gordura corporal?  
- A frequência semanal de treino realmente influencia a redução de gordura?  
- Qual é a relação entre IMC (BMI) e percentual de gordura?

As respostas para essas perguntas podem ser exploradas no dashboard desenvolvido no **Power BI**.

---

## 🧱 Arquitetura do Pipeline

O fluxo ETL é dividido em três etapas principais:

1. **Extração**  
   - Leitura dos dados brutos a partir de arquivos CSV (origem: Kaggle).  
   - Os dados brutos são armazenados na pasta `raw`.

2. **Transformação**  
   - Limpeza e padronização dos dados (remoção de nulos, duplicados).  
   - Padronização de campos.  
   - Criação de novas variáveis ou métricas (por exemplo: taxas, médias).  
   - Geração de estatísticas descritivas usando `pandas` e `numpy`.

3. **Carga**  
   - Os dados transformados são carregados em um banco **SQLite**.  
   - Estrutura relacional simples para permitir conexão direta com o Power BI.

---

## 📊 Dashboard Power BI

O dashboard foi construído conectando o Power BI ao banco SQLite criado pelo pipeline. A interface permite:

- Comparar tipos de dieta;  
- Comparar tipos de treino;  
- Ver a evolução da gordura conforme a frequência de treino;  
- Analisar a relação entre IMC e percentual de gordura.

A documentação detalhada do dashboard está no diretório `powerbi/` (ou equivalente) do projeto.

---

## 🚀 Como Executar o Pipeline

1. Instale as dependências:

    ```bash
   pip install -r requirements.txt

2.  Execute o pipeline:

python src/main.py

👥 Equipe

Planejamento - Luana

Desenvolvimento - Pamela, Ingrid e Gisela;

Visualização - Vanelle, Vanessa;

Documentação - Francielle;

Github - Tatiana


📚 Tecnologias Utilizadas

Python (pandas, numpy)

SQLite

Power BI

Git / GitHub


🎁 Agradecimentos

Kaggle, pela base de dados utilizada

Comunidade Python pela quantidade enorme de recursos



   ```bash
   pip install -r requirements.txt
