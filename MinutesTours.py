import sys
def Hours(minute):
    if minute < 0:
        raise ValueError("input number cannot be negative")
    else:
        hour = minute//60
        minutes = minute%60
        print("{} H, {} M, ".format(hour, minutes))
    
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")



