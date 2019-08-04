import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
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


def plotDendrogram(Z):
    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z,
        truncate_mode='lastp',
        p=12,  # show only the last pa merged clusters
        show_leaf_counts=False,  # otherwise numbers in brackets are counts
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
        # show_contracted=True,
    )
    plt.show()


INTERVAL = 'T'
ITEMSETS_PER_DAY = 10
if __name__ == '__main__':

    data = load_Data_Set('Apt1_2016.csv')

    data_interval = data.resample(INTERVAL).sum()

    consumption_table = split_Year_to_Days(data_interval)

    # print(consumption_table.head())

    Z = linkage(consumption_table.iloc[:, :], 'ward')
    plotDendrogram(Z)
