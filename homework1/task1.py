def check_power_of_2(a: int) -> bool:

    if a < 1:
        return False

    while (a > 1) & (a % 2 == 0):
        a = a / 2

    if a == 1:
        return True
    else:
        return False

 
