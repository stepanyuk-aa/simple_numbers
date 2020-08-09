from check import *
from logs import *

mS = mark_time()
add_log("Start")
m1 = mark_time()
for w in range(2,100000):
    if checker(w):
        add_log(str(dif_time(m1, mark_time())) + "\t" + str(w))
        m1 = mark_time()

add_log(str(dif_time(mS, mark_time())) + "\t Stop")
