import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

ENTRIES_PER_DAY = 1440
DAY = 0

if __name__ == "__main__":

    # Import as Dataframe
    df_one_year = pd.read_csv('Apt1_2016.csv', header=None, names=[
        'date', 'value'], index_col='date')

    df_one_day = df_one_year[DAY * ENTRIES_PER_DAY: DAY *
                             ENTRIES_PER_DAY + ENTRIES_PER_DAY]

    kmeans = KMeans(n_clusters=5, random_state=0).fit(df_one_day)

    df_one_day['label'] = 1
    df_one_day['label'] = kmeans.labels_
    print(df_one_day.head())

    plt.figure(figsize=(16, 5), dpi=100)
    plt.plot(df_one_day.index, df_one_day['value'], color='tab:red')
    plt.scatter(df_one_day.index, df_one_day['label'], color='tab:green')
    plt.show()
