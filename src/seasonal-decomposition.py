from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd

ENTRIES_PER_DAY = 1440
DAY = 1

if __name__ == '__main__':

    # Import as Dataframe
    df_one_year = pd.read_csv('Apt1_2016.csv', header=None, names=[
        'date', 'value'], index_col='date', parse_dates=True)

    df_one_day = df_one_year[DAY * ENTRIES_PER_DAY: DAY *
                             ENTRIES_PER_DAY + ENTRIES_PER_DAY]
    # Multiplicative Decomposition
    result_mul = seasonal_decompose(
        pd.Series(df_one_day['value']), model='multiplicative', freq=40)

    # Additive Decomposition
    result_add = seasonal_decompose(
        df_one_day['value'], model='additive', freq=40)

    # Plot
    plt.rcParams.update({'figure.figsize': (10, 10)})
    result_mul.plot().suptitle('Multiplicative Decompose', fontsize=22)
    result_add.plot().suptitle('Additive Decompose', fontsize=22)
    plt.show()
