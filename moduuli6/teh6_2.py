import random
def dice (x):
    for i in range(x):
        z = random.randint(1,x)
        print(z, end=" ")
    return

x = int(input("Anna nopan sivjen määrä:\n"))
dice (x)