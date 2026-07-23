import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r'C:\Users\adith\Desktop\AI-ML-journey\libraries\salaries.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, py_salaries, color='#444444',
         linestyle='--', label='Python')

plt.plot(ages, js_salaries, label='JavaScript')

# overall_median = 57287

plt.fill_between(ages, js_salaries, py_salaries,
                 where=(js_salaries > py_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, js_salaries, py_salaries,
                 where=(js_salaries <= py_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()