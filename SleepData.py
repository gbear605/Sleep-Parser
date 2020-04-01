import datetime
from datetime import date
from typing import List, Tuple


class SleepData:
    first_date: date
    second_date: date
    timezone: str
    rating: int
    total_hours: float
    times: List[Tuple[str, str]]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __init__(self,
                 first_date: datetime.date,
                 second_date: datetime.date,
                 timezone: str,
                 rating: str,
                 total_hours: float,
                 times: List[Tuple[str, str]]):
        self.first_date = first_date
        self.second_date = second_date
        self.timezone = timezone
        self.rating = int(rating.split('/')[0])  # get the number from #/10 format
        self.total_hours = total_hours
        self.times = times
        assert len(self.times) <= 2, "Header only set up for two times"

    def __str__(self) -> str:
        string = self.first_date.isoformat()
        string += ', ' + self.second_date.isoformat()
        string += ', ' + self.timezone
        string += ', ' + str(self.rating)
        string += ', ' + ('%05.2f' % self.total_hours)
        for time in self.times:
            string += ', ' + time[0] + ', ' + time[1]
        return string

    @staticmethod
    def header() -> str:
        return 'first date, ' \
               'second date, ' \
               'timezone, rating, ' \
               'total hours, ' \
               'start time, ' \
               'end time, ' \
               'second start time, ' \
               'second end time '
