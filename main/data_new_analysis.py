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

# 2. Gráfico de Linha - Evolução de Vendas ao Longo do Tempo
vendas_por_dia = vendas_data.groupby('Data').agg({'Quantidade': 'sum', 'Valor': 'sum'}).reset_index()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=vendas_por_dia['Data'], y=vendas_por_dia['Valor'], 
                          mode='lines+markers', name='Valor das Vendas',
                          line=dict(color='blue', width=2), marker=dict(size=8)))
fig1.add_trace(go.Scatter(x=vendas_por_dia['Data'], y=vendas_por_dia['Quantidade'], 
                          mode='lines+markers', name='Quantidade Vendida',
                          line=dict(color='orange', dash='dash'), marker=dict(size=8)))
fig1.update_layout(title="Evolução de Vendas ao Longo do Tempo",
                   xaxis_title="Data da Venda",
                   yaxis_title="Quantidade / Valor",
                   legend_title="Legenda",
                   hovermode="x unified")
fig1.write_html(os.path.join(output_dir, "evolucao_vendas_interativo.html"))

# 3. Histograma - Distribuição dos Valores das Vendas
fig2 = px.histogram(vendas_data, x='Valor', nbins=25, 
                    title="Distribuição dos Valores das Vendas",
                    labels={'Valor': 'Faixas de Valor (em unidades monetárias)'},
                    color_discrete_sequence=['#636EFA'])
fig2.add_vline(x=vendas_data['Valor'].mean(), line_dash="dash", line_color="red",
               annotation_text=f"Média: {vendas_data['Valor'].mean():.2f}", annotation_position="top left")
fig2.add_vline(x=vendas_data['Valor'].median(), line_dash="dot", line_color="green",
               annotation_text=f"Mediana: {vendas_data['Valor'].median():.2f}", annotation_position="top right")
fig2.update_layout(yaxis_title="Frequência", hovermode="x unified")
fig2.write_html(os.path.join(output_dir, "distribuicao_valores_interativo.html"))

