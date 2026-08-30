import random
dise = 0
sums = 0
times = int(input("how many dices you throw?\n"))
for i in range(times):
    dise = random.randint(1,6)
    print(dise, end=" ")
    sums += dise
    sums +=dise


print(f"\n{sums}")