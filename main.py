from check import *
from logs import *

mS = mark_time()
# add_log("Start")

m1 = mark_time()

num = get_last_num() + 1

while True:
    if checker(num):
        add_log(
            str(num) + "," +
            dif_time(m1, mark_time()) + "," +
            dif_time(mS, mark_time())
        )
        m1 = mark_time()
    num+=1
