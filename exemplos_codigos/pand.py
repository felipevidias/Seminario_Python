import pandas as pd

# Criando um DataFrame com dados de vendas
dados_vendas = {
    "Produto": ["Laptop", "Teclado", "Mouse", "Monitor", "Teclado", "Mouse", "Monitor"],
    "Quantidade": [10, 50, 100, 20, 30, 50, 10],
    "Preco_Unitario": [3000, 100, 50, 800, 100, 50, 800],
    "Loja": ["Loja A", "Loja B", "Loja A", "Loja C", "Loja A", "Loja B", "Loja C"]
}

df_vendas = pd.DataFrame(dados_vendas)

# Exibe o DataFrame inicial
print("DataFrame de Vendas:\n", df_vendas, "\n")

# Calcula o valor total de cada venda
df_vendas["Valor_Total"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
print("DataFrame com Valor Total de cada venda:\n", df_vendas, "\n")

# Filtra produtos vendidos na "Loja A" com quantidade maior que 20
filtro = df_vendas[(df_vendas["Loja"] == "Loja A") & (df_vendas["Quantidade"] > 20)]
print("Vendas na Loja A com mais de 20 unidades:\n", filtro, "\n")

# Soma total de vendas por loja
total_por_loja = df_vendas.groupby("Loja")["Valor_Total"].sum()
print("Soma total de vendas por loja:\n", total_por_loja, "\n")

# Produto mais vendido por quantidade em cada loja
mais_vendido_por_loja = df_vendas.groupby("Loja").apply(lambda x: x.loc[x["Quantidade"].idxmax()])
print("Produto mais vendido em cada loja:\n", mais_vendido_por_loja)
