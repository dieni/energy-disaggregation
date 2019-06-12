import pandas as pd


apartment_data = pd.read_csv(
    'Apt1_2016.csv', header=None, names=['time', 'consumption'])

print(apartment_data['time'])
