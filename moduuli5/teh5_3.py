pre = int(input("Anna numero: "))

l= 0 #laskee kuinka monen kierroksen jakojäännös on 0
for num in range(1, pre +1):
    x = pre % num
    if x == 0:
        l += 1
if l > 2:
    print(f"{pre} ei ole alkuluku")

else:
    print(f"{pre} on alkuluku")
