# Título: Análise de Fatores de Sucesso para Redução de Gordura Corporal

## Problema 
Uma empresa de consultoria fitness e nutrição quer criar planos mais eficazes para seus clientes. Atualmente, os clientes recebem sugestões genéricas, mas a empresa não sabe quais combinações de dieta e exercício trazem os melhores resultados para diminuir o 
percentual de gordura corporal. 

## Desafio 
Identificar quais fatores e hábitos, como o tipo de dieta, modalidade de treino, frequência semanal, tem maior impacto na redução do percentual de gordura e como eles se relacionam entre si para diferentes perfis de pessoas.

## Fonte de dados 
Base de dados com 20.000 registros sobre saúde e es lo de vida, extraída do Kaggle. 

Contendo informações sobre:  
Características pessoais: Age (idade), Gender (gênero).   
Métricas corporais: Weight (Peso), BMI (IMC), Fat_Percentage (Percentual de Gordura).     
Métricas de hábitos: diet_type (Tipo de Dieta), Workout_Type (Tipo de Treino),   
Workout_Frequency (Frequência Semanal),   Experience_Level (Nível de Experiência).  

## Objetivo
Construir um pipeline ETL (extração do CSV, transformação dos dados e carga no DBeaver), seguindo a arquitetura medalhão, para alimentar um dashboard no Power BI que permita à equipe de nutricionistas e treinadores responder perguntas-chave:
 
1. Qual po de dieta (diet_type) apresenta a menor média de percentual de gordura (Fat_Percentage)?  
Gráfico de barras (eixo x: dietas / eixo y: média de gordura) 
2. Qual po de treino (Workout_Type) está associado a um percentual de gordura mais baixo?   
Gráfico de barras por modalidade de treino. 
3. A frequência semanal (Workout_Frequency) realmente faz diferença na redução de gordura?  
Gráfico de linhas (eixo x: frequência / eixo y: média de gordura) 
4.  Qual a relação entre o IMC (BMI) e percentual de gordura (Fat_Percentage)? 
Gráfico de dispersão + gráfico de barras por classificação do IMC.

## Colunas Essenciais para o Desafio 
As variáveis foram organizadas em três categorias para facilitar entendimento e uso no 
dashboard: 
1. Métricas de Resultado (KPIs principais): 
* Fat_percentage (percentual de gordura): métrica mais importante do projeto. 
*BMI (IMC): necessário para analisar a relação entre IMC e gordura. 
2. Fatores de hábito (variáveis explica vas): 
* diet_type ( po de dieta): responde à pergunta 1. 
* Workout_Type ( po de treino): responde à pergunta 2. 
* Workout_Frequency (days/week) (frequência de treino): responde à pergunta 3. 
3. Colunas de Segmentação (filtros do dashboard): 
* Age (idade): segmentar por faixa etária. 
* Gender (gênero): comparar homens e mulheres. 
* Experience_Level (nível de experiência): comparar iniciantes, intermediários e 
avançados.
 
## Resumo das colunas mantidas: 
1. Fat_Percentage 
2. Weight  
3. BMI 
4. diet_type 
5. Workout_Type 
6. Workout_Frequency (days/week) 
7. Age 
8. Gender 
9. Experience_Level 
Com essas 9 colunas é possível construir um dashboard completo e focado em responder 
as perguntas definidas. 