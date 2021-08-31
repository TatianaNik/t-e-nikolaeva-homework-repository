def find_max_and_min(file_name: str):

    with open(file_name, "r") as fi:
        mx = 0
        mi = 0
        for line in fi:
            if int(line) < mi:
                mi = int(line)
            if int(line) > mx:
                mx = int(line)

    return [mi, mx]
