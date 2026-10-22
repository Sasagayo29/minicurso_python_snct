# =====================================================================
# MINICURSO: Mulheres na Tecnologia (23ª SNCT - IFTM)
# Script: Lendo uma planilha Excel/CSV do seu próprio computador
# =====================================================================

# Passo 1: Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

print("Importando a base de dados local...")

# ---------------------------------------------------------------------
# 💡 DICA PARA O GOOGLE COLAB:
# Antes de rodar este código, você precisa fazer o "Upload" do arquivo:
# 1. Clique no ícone de "Pasta" (Arquivos) no menu esquerdo do Colab.
# 2. Clique no ícone de "Upload" (uma folha com uma seta para cima).
# 3. Envie o arquivo 'mercado_tecnologia.csv' do seu computador.
# ---------------------------------------------------------------------

# O Pandas vai procurar o arquivo na pasta atual do Colab
nome_do_arquivo = "mercado_tecnologia.csv"

try:
    # Lendo o arquivo CSV (Se fosse Excel, usaríamos pd.read_excel('arquivo.xlsx'))
    tabela_local = pd.read_csv(nome_do_arquivo)
    
    print("\n✅ Arquivo lido com sucesso! Veja os primeiros dados:")
    print(tabela_local.head()) # .head() mostra só as 5 primeiras linhas para não poluir a tela
    
    # Criando um gráfico simples de Vagas Abertas
    print("\nGerando gráfico de vagas...")
    
    # Ordenando a tabela do maior número de vagas para o menor
    tabela_local = tabela_local.sort_values(by="Vagas_Abertas", ascending=True)
    
    # Montando o visual do gráfico
    tabela_local.plot(
        kind='barh', 
        x='Cargo', 
        y='Vagas_Abertas', 
        color='#ec4899', # Rosa bonitão
        title='Vagas Abertas por Cargo - Arquivo Local',
        figsize=(10, 6)
    )
    
    plt.xlabel("Quantidade de Vagas")
    plt.ylabel("Cargo")
    plt.show()

except FileNotFoundError:
    # Se o aluno esquecer de fazer o upload do arquivo, o Python avisa com carinho!
    print(f"❌ Erro: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    print("Lembre-se de clicar na pastinha à esquerda e fazer o upload do arquivo no Colab primeiro!")