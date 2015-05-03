import gevent
from time import sleep
import random
from itertools import repeat


"""
Use gevent to create 3 simultaneous jobs. 
Each job sleeps for a random amount of time between 1 and 10 seconds 
before returning the time with millisecond resolution. 
Print the collected times in a single list.
"""

def sleep_function(delay_time):
	gevent.sleep(delay_time)
	return round(delay_time, 2)

def simultaneous_tasks(loops):
	delay_times = []
	for _ in repeat(None, loops):
		delay_time = random.uniform(1,10)
		delay_times.append(delay_time)
	delayed = [gevent.spawn(sleep_function, dt) for dt in delay_times]
	gevent.joinall(delayed)
	return [d.value for d in delayed]


# Run simultaneous_tasks(3) in the command line after importing sleep to test