import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Carregar os dados
file_path = "data/vendas-tratadas.csv"  # Substitua pelo caminho correto
vendas_data = pd.read_csv(file_path)

# Ajustar a coluna de data
vendas_data['Data'] = pd.to_datetime(vendas_data['Data da fatura'])

# Criar a pasta "graficos_interativos" se não existir
output_dir = "graficos_interativos"
os.makedirs(output_dir, exist_ok=True)

