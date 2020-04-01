# Sleep Log Parser

Parses sleep log files

### Usage

In a file titled data.txt, have sleep information formatted like this:

```
June 1-2
23:30-08:00; 8:30 hours
7/10

June 2-3
00:30-08:00; 7:30 hours
5/10

...
```

Then run `python main.py`, using Python 3. 
This will create `AverageHoursSlept.png` and `HoursSlept.png`. 
In addition, it will print a csv format data table to the stdout.

The graphs chart only the recorded total hours, not the start and end times,
and there is no verification that the start and end times match the total sleep hours.

#### Timezones and Years

The script assumes that the first data point is from 2019 during daylight savings time.
In addition, it assumes that the time zone is in Eastern time.

You can change timezones by appending a timezone to the date line. Eg.

```
June 1-2 (CDT)
23:30-08:00; 8:30 hours
7/10
```

You can also change between daylight savings time and standard time with `(TZC)`:

```
November 2-3 (TZC)
23:00-06:30; 8:30 hours
7/10
```

#### Biphasic Sleep

If you wake up and then fall back asleep again, you can log both separate times:

```
June 1-2
23:30-02:00, 02:30-08:00; 8:00 hours
6/10
```

However, this currently only works for two separate sleep phases.

### Dependencies

Matplotlib, Numpy
