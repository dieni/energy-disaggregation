# Load the Pandas libraries with alias 'pd'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from file 'fridge.csv'

# Control delimiters, rows, column names with read_csv (see later)
fridge_data = pd.read_csv("../data/fridge.csv", delimiter=';',
                          encoding='utf-8', header=0)

# remove the W from the consumption value
fridge_data = fridge_data.replace({'W': '', ',': '.'}, regex=True)

# split data based on the date in a list
timeseries_fridge = [fridge_data[fridge_data['date'] == date]
                     for date in np.unique(fridge_data['date'])]

# plot a timeserie
serie1 = timeseries_fridge[0][{'consumption', 'time'}]

plt.plot(serie1['time'], serie1['consumption'])
plt.ylabel('fridge day 1')
plt.show()
