import pandas as pd

# Carregar o arquivo enviado para inspecionar os dados
file_path = "data/vendas-tratadas.csv"
vendas_data = pd.read_csv(file_path)

# Exibir as primeiras linhas e informações gerais para entender a estrutura do dataset
vendas_data.info(), vendas_data.head()