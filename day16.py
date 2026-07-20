import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

data = pd.read_csv('C:\\Users\\adith\\Desktop\\AI-ML-journey\\libraries\\data.csv')
ids = data['Responder_id']
lang_programming = data['LanguagesWorkedWith']

languages_counter = Counter()

for response in lang_programming:
    languages_counter.update(response.split(';'))

languages =[]
popularity = []

for item in languages_counter.most_common(13):
    languages.append(item[0])
    popularity.append(item[1])


languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.ylabel('Programming Languages')
plt.xlabel('Count') 
plt.title('Most Popular Programming Languages')
plt.show()
    




