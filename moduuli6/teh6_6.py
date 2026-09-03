import math
def cal_pizza(x,y):
    red = math.pi*math.sqrt(x)
    pris = red*y
    return pris

def komppi(x,y):
    if x < y:
        print(f"ensimäinen pizza on halvampaa, se maksa {x:.2f} € ja toinen maksa {y:.2f} €")
    elif x > y:
        print(f"toinen pizza on halvampaa, se maksa {y:.2f} € ja ensimäinen maksa {x:.2f} €")
    else:
        print(f"Molemmat maksavat saman verran.{x:.2f}€")
    return

p1 = int(input("pizza1 pitus: "))
m1 = int(input("paljonko: "))
t1 = cal_pizza(p1,m1)
p2 = int(input("pizza2 pitus: "))
m2 = int(input("paljonko: "))
t2 = cal_pizza(p2,m2)
komppi(t1,t2)


