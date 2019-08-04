from tsfresh import extract_features
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":

    ENTRIES_PER_DAY = 1440

    # import csv file
    apartment_csv = pd.read_csv('Apt1_2016.csv', header=None, names=[
                                'time', 'consumption'])

    # visualization
    # plt.plot(apartment_csv[:ENTRIES_PER_DAY])

    plt.plot(apartment_csv)
    plt.show()

    # extract features
    # day1 = apartment_csv['2016-01-01':'2016-01-02']

    # reduction of complexity
    df = pd.DataFrame(apartment_csv[:10000])

    number_of_rows = np.size(df, axis=0)

    # add a column and label the days
    df['day'] = 0
    number_of_days = int(number_of_rows / ENTRIES_PER_DAY)

    for day in range(number_of_days):
        df['day'][day * ENTRIES_PER_DAY: (day + 1) * ENTRIES_PER_DAY] = day + 1

    df['day'][number_of_days * ENTRIES_PER_DAY:] = number_of_days + 1

    extracted_features = extract_features(
        df, column_id="day", column_sort='consumption')
