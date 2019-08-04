import pandas as pd
import numpy as np
from sklearn.decomposition import FastICA


def load_Data_Set(filename):
    raw_data = pd.read_csv(filename, header=None, names=[
                           'date', 'value'], parse_dates=['date'])

    data = raw_data.loc[:, ['value']]
    data = data.set_index(raw_data.date)
    data['value'] = pd.to_numeric(
        data['value'], downcast='float', errors='coerce')

    return data


def split_Year_to_Days(data):
    data['date'] = pd.to_datetime(data.index)
    data['dayofyear'] = data['date'].dt.dayofyear
    data['heure'] = data['date'].dt.time
    data_2014 = data.loc[:, [
        'heure', 'dayofyear', 'value']]
    temp = data.loc[:, ['dayofyear', 'value']]
    data_2014['value'] = pd.to_numeric(
        data_2014['value'], errors='coerce')
    temp = temp.set_index(data_2014.heure)
    temp = data_2014.pivot_table(index=['heure'], columns=['dayofyear'], values=[
                                 'value'], fill_value=0)
    return temp


def split_consumption(consumption_table, itemsets_per_day):
    return np.array_split(consumption_table, itemsets_per_day, axis=0)


def get_specific_day(consumtion_table, day):
    # day_consumption = {'time': consumption_table.index,
    #                    'value': consumption_table['value'][day]}
    # df = pd.DataFrame(day_consumption)
    df = pd.DataFrame(consumption_table['value'][day])
    df.reset_index(inplace=True)
    return df


def ica(consumption):
    ica = FastICA(n_components=5, random_state=0)
    S_ = ica.fit_transform(consumption)  # Reconstruct signals
    # A_ = ica.mixing_  # Get estimated mixing matrix
    print(S_.shape)


INTERVAL = 'T'
ITEMSETS_PER_DAY = 10
if __name__ == '__main__':

    data = load_Data_Set('Apt1_2016.csv')

    data_interval = data.resample(INTERVAL).sum()

    consumption_table = split_Year_to_Days(data_interval)

    # print(consumption_table.head())

    # consumption_table_split = split_consumption(
    #     consumption_table, ITEMSETS_PER_DAY)

    # ica_table = data_interval[:1000]['value']

    specific_day = get_specific_day(consumption_table, 1)
    specific_day['heure'] = specific_day['heure'].apply(
        lambda x: x.strftime('%H%M'))

    ica(specific_day)
