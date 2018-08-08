#! /usr/bin/python3.7

# The Datetime Module
import time
import datetime

# Create a datetime object:
dt = datetime.datetime.now()
# the datetime methods:
print('year: ' + str(dt.year))
print('day: ' + str(dt.day))
print('time: ' + str(dt.hour) + ':' + str(dt.minute) + ':' + str(dt.second))

# Convert Unix epoch timestamp to datetime object
timestamp = time.time()
dt = datetime.datetime.fromtimestamp(timestamp)

# Comparing datetime objects:
dt_1 = datetime.datetime.now()
time.sleep(1)
dt_2 = datetime.datetime.now()
print(dt_1 < dt_2)

# The TimeDelta Data type
# represents a duration of time, instead of a moment.
t_delta=datetime.timedelta(weeks=1, days=1, hours=2, minutes=0, seconds=0, milliseconds=0, microseconds=0)
print(t_delta.total_seconds())

# using the timedelta data type we can perform basic math arithmetic's:
print(dt+t_delta)
print(dt-t_delta)
print(dt+t_delta*3)  # multiplying timedelta data types and not datetime objects

# we can use loops to make a program run until a specific date
end_dt = datetime.datetime.now() + datetime.timedelta(seconds=2)
while datetime.datetime.now() < end_dt:
    time.sleep(1)
    print('this is gonna take a while')

# strftime() formats datetime objects with directives (%Xx)
time_str=dt.strftime('%d/%m/%Y, %A - %H:%M:%S')
print(time_str)

# strptime() parses strings to datetime objects with directives (%Xx)
dt = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(dt)
dt = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt)

