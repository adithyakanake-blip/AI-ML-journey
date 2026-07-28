import pandas as pd 
pkm =pd.read_csv(r'C:\Users\adith\Desktop\AI-ML-journey\libraries\pandas\Pokemon.csv')

# using column
# print (pkm['Name'])


# read each column 
# print(pkm[['Name','HP','Total']].head(11))
#'integer_location' = iloc[row_position,column_position]
# can be also used for specific location -->iloc[2,1]
# print(pkm.iloc[0:4])
# print(pkm[['Name','HP','Total']].iloc[1,0])


# read each row 
# for index, row in pkm.iterrows():
     # print(index, row['Name'])

# print (pkm.loc[pkm['Type 1'] == "Fire"])
# print(pkm.loc[pkm['Type 2'] == "Fighting"])


# print (pkm.loc[(pkm['Type 1'] == 'Fire') & (pkm['Type 2'] == 'Fighting')])

sort =pkm.sort_values(['Type 1', 'HP'], ascending=[0,1])

print (sort)