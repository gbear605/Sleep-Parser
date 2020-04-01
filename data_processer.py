import datetime
from typing import List, Tuple

from SleepData import SleepData


def hours_to_float(hours: int, minutes: int) -> float:
    return float(str(hours) + ('%.2f' % (minutes / 60))[1:])


def get_month(long_month: str):
    return {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }[long_month]


def extract_time(time_to_extract: str):
    return time_to_extract.split('-')[0], time_to_extract.split('-')[1]


def process_data(content: List[str]):
    data_processed_so_far = []
    year = 2019
    default_timezone = 'EDT'

    for i in range(0, len(content), 4):
        # extract values
        date = content[i + 0]
        time = content[i + 1]
        rating = content[i + 2]

        # handle timezone
        timezone = default_timezone
        if date[-1] == ')':
            new_timezone = date[-4:-1]
            if new_timezone == 'TZC':
                if default_timezone == 'EST':
                    default_timezone = 'EDT'
                elif default_timezone == 'EDT':
                    default_timezone = 'EST'
                else:
                    raise Exception("Invalid default timezone " + default_timezone)
                timezone = default_timezone
            else:
                timezone = new_timezone

            date = date[:-6]

        # handle date
        (first_date_string, second_date_string) = date.split('-')
        (first_month, first_day) = first_date_string.split(' ')
        first_date = datetime.date(year, get_month(first_month), int(first_day))
        second_date: datetime.date
        if ' ' in second_date_string:
            (second_month, second_day) = second_date_string.split(' ')
            if second_month == 'January' and first_month == 'December':
                year += 1
            second_date = datetime.date(year, get_month(second_month), int(second_day))
        else:
            second_date = datetime.date(year, get_month(first_month), int(second_date_string))

        # handle time
        (time_range, total_time_string) = time.split(';')
        time_range = time_range.strip()

        (hours, minutes) = total_time_string.strip(' hours').split(':')
        total_hours = hours_to_float(int(hours), int(minutes))

        times: List[Tuple[str, str]] = []
        if ',' in time_range:
            times = [extract_time(time) for time in time_range.split(', ')]
        else:
            times.append(extract_time(time_range))

        data_processed_so_far.append(SleepData(first_date, second_date, timezone, rating, total_hours, times))

    return data_processed_so_far
