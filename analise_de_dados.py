# =====================================================================
# MINICURSO: Mulheres na Tecnologia (23ª SNCT - IFTM)
# Script: Lendo uma planilha Excel/CSV por link web
# =====================================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Conectando com a base de dados real na nuvem (GitHub)
url_dados = "https://raw.githubusercontent.com/Sasagayo29/minicurso_python_snct/refs/heads/main/mercado_tecnologia.csv"
tabela_mercado = pd.read_csv(url_dados)

# 2. Exibindo os dados (O display cria uma tabela interativa no Colab!)
print("Panorama do Mercado de Tecnologia:")
display(tabela_mercado)

# 3. Criando o gráfico
# Vamos ordenar os salários para o gráfico ficar com formato de escada
tabela_mercado = tabela_mercado.sort_values(by='Salario_Medio')

tabela_mercado.plot(
    kind='barh', # barh = barras horizontais
    x='Cargo', 
    y='Salario_Medio', 
    color='teal', 
    title='Média Salarial por Cargo na Tecnologia (2026)',
    figsize=(8, 5) # Deixa o gráfico com um tamanho bom
)

plt.xlabel("Salário Médio (R$)")
plt.ylabel("Cargo")
plt.show()