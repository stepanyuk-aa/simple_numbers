from check import *
from logs import *

add_header(); mS = mark_time()
# add_log("Start")

m1 = mark_time()
for w in range(2,10000):
    if checker(w):
        add_log(
            str(w) + "," +
            dif_time(m1, mark_time()) + "," +
            dif_time(mS, mark_time())
        )
        m1 = mark_time()

# add_log( + "\t Stop")
