import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime,timedelta

plt.style.use('fivethirtyeight')

dates =[datetime(2020,4,21),
        datetime(2020,4,22),
        datetime(2020,4,23),
        datetime(2020,4,24),
        datetime(2020,4,25),
        datetime(2020,4,26),
        datetime(2020,4,27),
]

y = [0,1,3,5,2,6,4]

plt.plot(dates,y,linestyle='solid')

plt.gcf()

date_format = mpl_dates.DateFormatter('%b,%d %y')

plt.gca().xaxis.set_major_formatter(date_format)

plt.show()