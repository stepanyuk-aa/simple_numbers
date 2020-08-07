def checker(num):
    is_simple = True
    simple_num = []
    for w in range(2, num):
        if num % w == 0:
            # print(w, " => ", num % w)
            is_simple = False
            break

    if is_simple: print(num, " is simple")
    # else: print(num, " is not simple")
