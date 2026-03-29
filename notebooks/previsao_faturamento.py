import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import os

# 1. Caminhos das abas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_excel = os.path.join(BASE_DIR, "..", "data", "Dados_Dashboard_Agro.xlsx")

try:
    # 2. Carregar as duas abas necessárias
    df_vendas = pd.read_excel(caminho_excel, sheet_name='fVendas')
    df_produtos = pd.read_excel(caminho_excel, sheet_name='dProdutos') # Ou o nome da sua aba de produtos
    
    # 3. Trazer o Preço para a tabela de Vendas (Igual ao RELATED do Power BI)
    # Vamos unir as tabelas pelo 'ID_Produto'
    df = pd.merge(df_vendas, df_produtos[['ID_Produto', 'Preço_Saca']], on='ID_Produto')
    
    # 4. Calcular o faturamento no Python
    df['Total Faturamento'] = df['Quantidade'] * df['Preço_Saca']
    
    print("--- Dados processados com sucesso! ---")
    print(f"Total de registros para treino: {len(df)}")

    # 5. Preparar as variáveis para o Modelo
    X = df[['Quantidade']] 
    y = df['Total Faturamento']

    # 6. Dividir, Criar e Treinar o Modelo
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # 7. Avaliar o Modelo
    previsoes = modelo.predict(X_test)
    print(f"Precisao do Modelo (R2): {r2_score(y_test, previsoes):.2f}")
    print(f"Erro Medio Absoluto: R$ {mean_absolute_error(y_test, previsoes):.2f}")

    # 8. Visualizar o Gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='green', alpha=0.5, label='Dados Reais')
    plt.plot(X, modelo.predict(X), color='red', linewidth=2, label='Reta de Previsao')
    plt.title('Machine Learning: Predicao de Faturamento vs Quantidade')
    plt.xlabel('Quantidade de Sacas')
    plt.ylabel('Faturamento (R$)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 9. Teste Prático
    qtd = 1500
    print(f"\nPrevisao para {qtd} sacas: R$ {modelo.predict([[qtd]])[0]:.2f}")

except Exception as e:
    print(f"Erro: {e}")
    print("Dica: Verifique se o nome da aba de produtos e 'dProdutos' e se tem a coluna 'Preço_Saca'")