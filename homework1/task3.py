def find_max_and_min(file_name: str):

    with open(file_name, "r") as fi:
        mx = int(fi.readline())
        mi = mx
        for line in fi:
            if int(line) < mi:
                mi = int(line)
            if int(line) > mx:
                mx = int(line)
    return mi, mx
