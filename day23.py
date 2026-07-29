import pandas as pd
pkm = pd.read_csv(r'C:\Users\adith\Desktop\AI-ML-journey\libraries\pandas\Pokemon.csv') 
pkm['Damage'] = pkm['Attack'] - pkm['Defense']
# pkm = pkm.drop(columns=['Damage'], axis=1)

pkm['Total'] = pkm.iloc[:, 4:10].sum(axis=1)
cols = list(pkm.columns)
pkm = pkm[cols[0:4] + [cols[-1]]+cols[4:12]]

    
print (pkm.head(10))
