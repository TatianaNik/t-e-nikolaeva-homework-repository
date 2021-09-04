def check_fib(data) -> bool:
    if len(data) == 0:
        return False
    if (len(data) == 1) & (data[0] == 0):
        return True
    elif (len(data) == 2) & (data[0] == 0) & (data[1] == 1):
        return True
    else:
        for i in range(2, len(data)-1):
            if data[i] != data[i-1] + data[i-2]:
                return False
        return True






