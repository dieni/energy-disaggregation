# https://www.machinelearningplus.com/time-series/time-series-analysis-python/
import matplotlib.pyplot as plt
import pandas as pd

# Draw Plot


def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16, 5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


ENTRIES_PER_DAY = 1440
DAY = 0

if __name__ == "__main__":
    # Import as Dataframe
    df_one_year = pd.read_csv('Apt1_2016.csv', header=None, names=[
        'date', 'value'], index_col='date')

    df_one_day = df_one_year[DAY * ENTRIES_PER_DAY: DAY *
                             ENTRIES_PER_DAY + ENTRIES_PER_DAY]

    plot_df(df_one_day, x=df_one_day.index, y=df_one_day.value,
            title='Consumption of a household a day.')
