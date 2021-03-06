import pandas as pd
import logs

def checker(num):
    is_simple = True
    simple_num = []
    for w in range(2, num):
        if num % w == 0:
            # print(w, " => ", num % w)
            is_simple = False
            break

    if is_simple:
        # print(num, " is simple")
        return True
    else:
        return False
    # else: print(num, " is not simple")

def get_last_num():
    try:
        df = pd.read_csv('logs.txt', ',')
        return int(df.iloc[[-1]]['Simple numbers'])
    except pd.errors.EmptyDataError:
        print('file is empty')
        logs.add_header();
        return 2

