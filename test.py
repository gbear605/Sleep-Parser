import unittest
import datetime

from SleepData import SleepData
from data_processer import process_data


class ProcessDataTest(unittest.TestCase):
    def basic_process_data(self) -> None:
        data = [
            "June 1-2",
            "23:30-08:00; 8:30 hours",
            "3/10"
        ]
        processed = process_data(data)
        expected = SleepData(datetime.date(2019, 6, 1),
                             datetime.date(2019, 6, 2),
                             "EDT",
                             "3/10",
                             8.5,
                             [("23:30", "08:00")])

        self.assertEqual(len(processed), 1)
        self.assertEqual(processed[0], expected)


if __name__ == '__main__':
    unittest.main()
