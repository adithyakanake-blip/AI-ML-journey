import pandas as pd
pkm = pd.read_csv(r'C:\Users\adith\Desktop\AI-ML-journey\libraries\pandas\Pokemon.csv') 
pkm['count'] = 1
print(pkm.groupby(['Type 1', 'Type 2']).count()['count'].reset_index().sort_values(by='count', ascending=True).head(10))  