import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Categoria': ['Alimentação', 'Aluguel', 'Transporte', 'Lazer', 'Outros'],
    'Valor': [500, 1200, 300, 150, 200]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(5, 5))
plt.pie(df['Valor'], labels=df['Categoria'], autopct='%1.1f%%', startangle=140)
plt.title('Despesas Mensais')
# plt.axis('equal')

plt.show()