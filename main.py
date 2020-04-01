from SleepData import SleepData
from data_processer import process_data
from typing import List, Tuple

import numpy as np
from numpy.polynomial.polynomial import Polynomial

import matplotlib
import matplotlib.pyplot as plt

with open('data.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    processed_data: List[SleepData] = process_data(content)

    hour_rating_list: List[Tuple[float, int]] = []
    last_three_days = []
    for datum in processed_data:
        last_three_days.append(datum.total_hours)
        if len(last_three_days) > 3:
            last_three_days.pop(0)

        hour_rating_list.append((datum.total_hours, np.average(last_three_days), datum.rating))

    hours, hours_last_three_days, ratings = zip(*hour_rating_list)

    hours_polynomial = Polynomial.fit(hours, ratings, 3)
    x2 = np.arange(min(hours), max(hours) + 0.5, 0.01)
    y2 = hours_polynomial(x2)

    plt.scatter(hours, ratings)
    plt.plot(x2, y2)
    plt.xlabel("Hours")
    plt.ylabel("Rating")
    plt.savefig('HoursSlept.png')
    plt.clf()

    hours_last_three_days_polynomial = Polynomial.fit(hours_last_three_days, ratings, 3)
    x2_last_three = np.arange(min(hours_last_three_days), max(hours_last_three_days) + 0.5, 0.01)
    y2_last_three = hours_last_three_days_polynomial(x2_last_three)

    plt.scatter(hours_last_three_days, ratings)
    plt.plot(x2_last_three, y2_last_three)
    plt.xlabel("Average Hours Over Three Days")
    plt.ylabel("Rating")
    plt.savefig('AverageHoursSlept.png')

    print(SleepData.header())
    for sleep_datum in processed_data:
        print(sleep_datum)
