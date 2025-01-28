def repeated(t, k):
    before_num = 0
    now_num = 0
    conunt_times = 0
    first = True
    while True: 
        now_num = next(t)
        if first is not True:
            if before_num == now_num:
                conunt_times += 1
                if conunt_times == k - 1:
                    return now_num
            if before_num != now_num:
                conunt_times = 0
            before_num = now_num
        if first is True:
            first = False
            before_num = now_num

s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
repeated(s, 2)