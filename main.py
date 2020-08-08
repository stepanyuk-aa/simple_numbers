from check import *
from logs import *

add_log("Start")
for w in range(2,100000):
    if checker(w): add_log(str(w) + ' is simple', True)

add_log("Stop")

