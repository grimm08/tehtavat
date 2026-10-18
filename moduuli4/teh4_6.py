import random
N = int(input("Anna pisteiden määrä: "))
in_point = 0
xpoint = 0
while xpoint < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x**2 + y**2) < 1:
        in_point += 1
    xpoint += 1

pical = 4* in_point / N
print()
print(f"Piin likiarvo: {pical}")
