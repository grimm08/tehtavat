import random
pc = random.randint(1,10)
player = int(input("guess the number:"))
while player != pc:
    if player < pc:
        print("Liian pieni arvaus")
    elif player > pc:
        print("Liian suuri arvaus")

    player = int(input("guess the number:"))

print("Oikein")