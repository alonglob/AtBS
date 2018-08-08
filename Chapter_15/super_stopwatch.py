#! /usr/bin/python3.7

import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')

time_start = time.time()
lap_start = time_start
lap_num = 1

try:
    while True:
        input()
        lap_time =round(time.time() - lap_start)
        total_time = round(time.time() - time_start)
        print('Lap: #%s: %s (%s)' % (lap_num,total_time, lap_time))
        lap_num += 1
        lap_start = time.time()

except KeyboardInterrupt:
    print('\nDone')
