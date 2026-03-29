# 🌾 Dashboard de Performance Comercial - Safra 2024

Este repositório contém um dashboard interativo desenvolvido no **Power BI** para análise de indicadores de vendas e faturamento no setor de agronegócio. O projeto simula a gestão de vendas de commodities e insumos agrícolas (Soja, Milho, Fertilizantes, etc.).

---

## 🖼️ Visualização do Projeto

### Visão Geral do Dashboard
![Dashboard Principal](screenshots/Captura%20de%20tela%202026-03-29%20165418.png)

> [!TIP]
> **[📄 Clique aqui para abrir o Relatório em PDF (Visualização Rápida)](docs/Relatorio_Performance_Agro.pdf)**

### Detalhes e Filtros
<p align="center">
  <img src="screenshots/Captura%20de%20tela%202026-03-29%20165739.png" width="48%" />
  <img src="screenshots/Captura%20de%20tela%202026-03-29%20165619.png" width="48%" />
  <img src="screenshots/Captura%20de%20tela%202026-03-29%20165825.png" width="48%" />
  <img src="screenshots/Captura%20de%20tela%202026-03-29%20165851.png" width="48%" />
</p>

---

## 🚀 Objetivo do Projeto

Transformar dados brutos de vendas provenientes de arquivos Excel em insights estratégicos. A ferramenta permite que gestores identifiquem rapidamente quais produtos são mais rentáveis e acompanhem a evolução das vendas por região e período temporal.

## 🛠️ Tecnologias e Ferramentas

* **Power BI Desktop**: Construção do dashboard e visualizações.
* **Linguagem DAX**: Criação de medidas calculadas para faturamento e performance.
* **Modelagem de Dados**: Estrutura em *Star Schema* (Esquema Estrela).
* **Excel**: Fonte de dados para as tabelas Fato e Dimensões.

## 📊 Principais Funcionalidades

* **KPI de Faturamento Total**: Indicador principal com o valor total convertido em R$.
* **Análise por Categoria de Produto**: Gráfico de barras comparativo (ex: Fertilizante vs Soja).
* **Sazonalidade (Timeline)**: Gráfico de linhas mostrando os picos de venda ao longo de 2024.
* **Segmentação Regional**: Filtros interativos por Estado (BA, GO, MG, MT).

## 🧠 Desafios Técnicos Superados

* **Modelagem Star Schema**: Relacionamento eficiente entre a tabela fato (`fVendas`) e as dimensões (`dProdutos`, `dClientes` e `dVendedores`).
* **Medidas DAX**: Uso da função `SUMX` combinada com `RELATED` para cálculo de faturamento dinâmico:
  
  $$Total Faturamento = SUMX(fVendas, fVendas[Quantidade] * RELATED(dProdutos[Preço_Saca]))$$

* **Design UI/UX**: Interface profissional com aplicação de sombras, cantos arredondados e paleta de cores personalizada para o setor agrícola.

## 📁 Estrutura do Repositório

* **/data**: Base de dados em Excel utilizada no projeto.
* **/docs**: Relatório de visualização rápida em PDF.
* **/screenshots**: Capturas de tela do dashboard.
* **Dashboard_Performance_Agro_2024.pbix**: Arquivo fonte do Power BI.

## 📥 Como visualizar este projeto

1. Baixe o arquivo `Dashboard_Performance_Agro_2024.pbix` deste repositório.
2. Certifique-se de ter o **Power BI Desktop** instalado.
3. Abra o arquivo para interagir com os filtros e gráficos.

---
**Desenvolvido por Vítor Hugo Sátiro** 🚀