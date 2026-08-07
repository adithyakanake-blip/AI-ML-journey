import pandas as pd

biodata = pd.read_csv(r'C:\Users\adith\Desktop\AI-ML-journey\data cleaning\bios.csv')

biodata['name']=biodata['Used name'].replace("•"," ",regex=True)

biodata[['height_cm', 'weight_kg']] = biodata['Measurements'].str.split('/', expand=True)

useful_bio=['athlete_id', 'name', 'NOC', 'height_cm', 'weight_kg', ]

bio_needed = biodata[useful_bio]

print(bio_needed.head())