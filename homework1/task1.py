def check_power_of_2(a: int) -> bool:
    b = a ** 0.5
    if (b - int(b)) == 0:
        print ("True")
        return True
    else:
        print ("False")
        return False


 
