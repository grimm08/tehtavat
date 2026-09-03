import random

def dice(x,y):
    z = random.randint(x,y)
    while z != 6:
        print(z)
        z  = random.randint(x,y)
    print(z)
    return
dice (1,6)
